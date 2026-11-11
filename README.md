
# Assignment Submission Portal

A web-based assignment submission portal built using **Streamlit, FastAPI, and SQLite**. The application allows students to submit assignments through URLs, validates submitted information, and stores submissions in a database.

The project also demonstrates automated testing, Continuous Integration and Continuous Deployment (CI/CD), automatic test reporting, email notifications, and GitHub Pages deployment.

## Features

- Submit assignments using a URL.
- Validate student name, registration number, assignment title, and submission URL.
- Store submissions in an SQLite database.
- Display previously submitted assignments.
- REST API developed using FastAPI.
- Streamlit frontend for user interaction.
- Automated API testing using Pytest.
- GitHub Actions CI pipeline triggered on every push.
- Automatic JSON test report generation.
- Automatic delivery of test reports to a local HTTP receiver.
- Email notifications for both passing and failing test runs.
- Conditional GitHub Pages deployment after successful tests on the `main` branch.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Reporting | Pytest JSON Report |
| Email | Python SMTP |
| Deployment | GitHub Pages |
| Language | Python 3.11 |

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/fassi182/Assignment-Submission-Portal.git
cd Assignment-Submission-Portal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Backend

```bash
uvicorn backend.app.main:app --reload
```

Backend API documentation:

http://127.0.0.1:8000/docs

### 5. Start the Frontend

Open another terminal, activate the virtual environment, and run:

```bash
streamlit run app/streamlit_app.py
```

The application will open in your browser.

### 6. Run Automated Tests

```bash
pytest -v
```

Generate a JSON test report:

```bash
pytest -v --json-report --json-report-file=test-report.json
```

## Automated Testing

The project includes three automated test cases:

1. **Valid submission:** Verifies that a valid assignment is saved and appears in the submissions list.
2. **Missing registration number:** Verifies that a submission without a registration number is rejected.
3. **Invalid submission URL:** Verifies that an invalid URL is rejected and not saved.

## CI/CD Pipeline

GitHub Actions automatically executes the following steps whenever code is pushed:

1. Check out the repository.
2. Install Python dependencies.
3. Execute automated tests.
4. Generate a JSON test report.
5. Send the report to the local HTTP receiver.
6. Send an email notification containing test results.
7. Mark the workflow as failed if any test fails.
8. Deploy the static demonstration to GitHub Pages only when tests succeed on `main`.

### Local Test Report Receiver

The local receiver accepts test reports from GitHub Actions and saves them as:

`report_receiver/test-report.json`

Start the receiver locally:

```bash
uvicorn report_receiver.receiver:app --reload --port 8001
```

Keep the receiver running during CI execution. The self-hosted GitHub Actions runner must also be online to deliver reports to the local machine.

### GitHub Actions Secrets

Configure the following repository secrets under:

**Settings → Secrets and variables → Actions**

- `SMTP_USERNAME`
- `SMTP_PASSWORD`

These credentials are used by the email notification script. Do not commit email credentials to the repository.

## GitHub Pages

The project includes a static demonstration deployed through GitHub Pages.

**Live demonstration:**

https://fassi182.github.io/Assignment-Submission-Portal/

**Note:** GitHub Pages hosts a static HTML demonstration. The actual Streamlit and FastAPI application runs separately and requires its backend.

## Project Structure

```text
Assignment-Submission-Portal/
├── app/
│   ├── api.py
│   └── streamlit_app.py
├── backend/
│   └── app/
│       ├── database.py
│       ├── main.py
│       ├── models.py
│       └── schemas.py
├── tests/
│   ├── conftest.py
│   └── test_submissions.py
├── report_receiver/
│   └── receiver.py
├── scripts/
│   └── send_email.py
├── docs/
│   └── pages-demo/
│       └── index.html
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
└── README.md

## Author

**Muhammad Fassi Ur Rehman**

BS Artificial Intelligence  
COMSATS University Islamabad
