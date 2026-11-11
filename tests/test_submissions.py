
def test_valid_submission(client):
    """A valid submission must be saved and appear in the list."""

    submission = {
        "student_name": "Muhammad",
        "registration_number": "FA23-BAI-042",
        "assignment_title": "DevOps Lab Assignment",
        "submission_url": "https://github.com/fassi182"
    }

    # Submit assignment
    response = client.post("/submissions", json=submission)

    assert response.status_code == 201

    saved_submission = response.json()

    assert saved_submission["student_name"] == "Muhammad"
    assert saved_submission["registration_number"] == "FA23-BAI-042"

    # Retrieve submissions
    list_response = client.get("/submissions")

    assert list_response.status_code == 200

    submissions = list_response.json()

    assert len(submissions) == 1
    assert submissions[0]["id"] == saved_submission["id"]


def test_missing_registration_number(client):
    """A submission without registration number must be rejected."""

    submission = {
        "student_name": "Muhammad",
        "assignment_title": "DevOps Lab Assignment",
        "submission_url": "https://github.com/fassi182"
    }

    response = client.post("/submissions", json=submission)

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        "registration_number" in error["loc"]
        for error in errors
    )

    # Invalid submission must not be saved
    list_response = client.get("/submissions")

    assert list_response.json() == []


def test_invalid_submission_url(client):
    """An invalid URL must be rejected and not saved."""

    submission = {
        "student_name": "Muhammad",
        "registration_number": "FA23-BAI-042",
        "assignment_title": "DevOps Lab Assignment",
        "submission_url": "not-a-valid-url"
    }

    response = client.post("/submissions", json=submission)

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        "submission_url" in error["loc"]
        for error in errors
    )

    # Invalid submission must not be saved
    list_response = client.get("/submissions")

    assert list_response.json() == []
