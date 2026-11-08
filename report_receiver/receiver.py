
from pathlib import Path
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Local Test Report Receiver")

REPORT_PATH = Path(__file__).resolve().parent / "test-report.json"


@app.get("/")
def home():
    return {"message": "Local report receiver is running"}


@app.post("/report")
def receive_report(payload: dict):

    required_fields = [
        "repo_name",
        "branch",
        "commit_sha",
        "run_id",
        "pytest_report"
    ]

    for field in required_fields:
        if field not in payload:
            raise HTTPException(
                status_code=400,
                detail=f"Missing field: {field}"
            )

    pytest_report = payload["pytest_report"]

    if not isinstance(pytest_report, dict):
        raise HTTPException(
            status_code=400,
            detail="pytest_report must be a JSON object"
        )

    tests = []

    for test in pytest_report.get("tests", []):
        outcome = test.get("outcome", "unknown")

        failure_message = None

        for phase in ["setup", "call", "teardown"]:
            phase_data = test.get(phase, {})
            if phase_data.get("longrepr"):
                failure_message = str(phase_data["longrepr"])
                break

        tests.append({
            "test_name": test.get("nodeid", "Unknown test"),
            "result": outcome,
            "failure_message": failure_message
        })

    summary = pytest_report.get("summary", {})

    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0) + summary.get("error", 0)
    total = summary.get("total", len(tests))

    report = {
        "repo_name": payload["repo_name"],
        "branch": payload["branch"],
        "commit_sha": payload["commit_sha"],
        "run_id": payload["run_id"],
        "execution_timestamp": datetime.now(
            timezone.utc
        ).isoformat(),
        "total": total,
        "passed": passed,
        "failed": failed,
        "overall_status": "FAILED" if failed > 0 else "PASSED",
        "tests": tests
    }

    REPORT_PATH.write_text(
        __import__("json").dumps(report, indent=4),
        encoding="utf-8"
    )

    return {
        "message": "Report received and saved successfully",
        "file": str(REPORT_PATH),
        "overall_status": report["overall_status"]
    }
