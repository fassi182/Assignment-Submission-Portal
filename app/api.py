
import requests

API_URL = "http://127.0.0.1:8000"


def submit_assignment(data):
    try:
        response = requests.post(
            f"{API_URL}/submissions",
            json=data,
            timeout=10
        )

        if response.status_code == 201:
            return True, response.json()

        if response.status_code == 422:
            return False, response.json()

        return False, {"detail": "Submission failed."}

    except requests.exceptions.ConnectionError:
        return False, {"detail": "Cannot connect to FastAPI backend."}

    except requests.exceptions.Timeout:
        return False, {"detail": "Backend request timed out."}


def get_submissions():
    try:
        response = requests.get(
            f"{API_URL}/submissions",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        return None
