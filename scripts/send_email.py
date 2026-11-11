
import json
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

report_path = Path("test-report.json")

if not report_path.exists():
    raise FileNotFoundError("Test report was not generated.")

report = json.loads(report_path.read_text(encoding="utf-8"))

summary = report.get("summary", {})
tests = report.get("tests", [])

total = summary.get("total", len(tests))
passed = summary.get("passed", 0)
failed = summary.get("failed", 0) + summary.get("error", 0)

status = "FAILED" if failed > 0 else "PASSED"

username = os.environ["SMTP_USERNAME"]
password = os.environ["SMTP_PASSWORD"]

message = EmailMessage()
message["Subject"] = f"Assignment Portal CI: {status}"
message["From"] = username
message["To"] = username

body = f"""
Assignment Submission Portal - CI Test Report

Repository: {os.environ['REPO_NAME']}
Branch: {os.environ['BRANCH']}
Commit: {os.environ['COMMIT_SHA']}
Run ID: {os.environ['RUN_ID']}

Overall Status: {status}

Total Tests: {total}
Passed: {passed}
Failed: {failed}

Individual Test Results:
"""

for test in tests:
    body += f"\nTest: {test.get('nodeid', 'Unknown')}"
    body += f"\nResult: {test.get('outcome', 'unknown')}"

    for phase in ["setup", "call", "teardown"]:
        details = test.get(phase, {})
        if details.get("longrepr"):
            body += f"\nFailure: {details['longrepr']}"
            break

    body += "\n"

message.set_content(body)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(username, password)
    server.send_message(message)

print("Email notification sent successfully.")
