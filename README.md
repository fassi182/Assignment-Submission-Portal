
# Assignment Submission Portal

A web-based assignment submission portal built with Streamlit, FastAPI, and SQLite.

## Features

- Submit assignments using a URL.
- Validate student information and submission URLs.
- Store submissions in an SQLite database.
- Display previously submitted assignments.
- Automated API testing using Pytest.
- CI pipeline using GitHub Actions.
- Automated JSON test reporting.

## Technology Stack

- Frontend: Streamlit
- Backend: FastAPI
- Database: SQLite
- Testing: Pytest
- CI/CD: GitHub Actions
- Language: Python 3.11

## Project Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Assignment-Submission-Portal
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend

```bash
uvicorn backend.app.main:app --reload
```

Backend documentation:

http://127.0.0.1:8000/docs

### 5. Start the frontend

Open another terminal:

```bash
streamlit run app/streamlit_app.py
```

### 6. Run automated tests

```bash
pytest -v
```

Generate a JSON test report:

```bash
pytest -v --json-report --json-report-file=test-report.json
```

## Project Structure

- `app/` - Streamlit frontend
- `backend/` - FastAPI backend and database
- `tests/` - Automated tests
- `report_receiver/` - Local test report receiver
- `docs/pages-demo/` - Static GitHub Pages demonstration
- `.github/workflows/` - GitHub Actions workflows

## Author

Muhammad Fassi Ur Rehman
