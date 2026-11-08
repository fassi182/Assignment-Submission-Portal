
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc

from .database import engine, get_db, Base
from . import models
from .schemas import SubmissionCreate, SubmissionResponse


# Create database tables automatically
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Assignment Submission Portal API",
    description="API for submitting and retrieving student assignments",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Assignment Submission Portal API is running"
    }


# Submit an assignment
@app.post(
    "/submissions",
    response_model=SubmissionResponse,
    status_code=201
)
def create_submission(
    submission: SubmissionCreate,
    db: Session = Depends(get_db)
):

    new_submission = models.Submission(
        student_name=submission.student_name,
        registration_number=submission.registration_number,
        assignment_title=submission.assignment_title,
        submission_url=str(submission.submission_url)
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return new_submission


# Retrieve all saved submissions
@app.get(
    "/submissions",
    response_model=list[SubmissionResponse]
)
def get_submissions(db: Session = Depends(get_db)):

    submissions = (
        db.query(models.Submission)
        .order_by(desc(models.Submission.id))
        .all()
    )

    return submissions
