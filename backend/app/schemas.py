
from pydantic import BaseModel, Field, HttpUrl, ConfigDict, field_validator


class SubmissionCreate(BaseModel):

    student_name: str = Field(min_length=1, max_length=100)

    registration_number: str = Field(min_length=1, max_length=50)

    assignment_title: str = Field(min_length=1, max_length=200)

    submission_url: HttpUrl

    @field_validator(
        "student_name",
        "registration_number",
        "assignment_title",
        mode="before"
    )
    @classmethod
    def validate_required_fields(cls, value):
        if isinstance(value, str):
            value = value.strip()

            if not value:
                raise ValueError("This field is required.")

        return value


class SubmissionResponse(BaseModel):

    id: int
    student_name: str
    registration_number: str
    assignment_title: str
    submission_url: HttpUrl
    created_at: object

    model_config = ConfigDict(from_attributes=True)
