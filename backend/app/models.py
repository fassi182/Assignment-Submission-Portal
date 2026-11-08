
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base


class Submission(Base):

    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    student_name = Column(String(100), nullable=False)

    registration_number = Column(
        String(50),
        nullable=False
    )

    assignment_title = Column(
        String(200),
        nullable=False
    )

    submission_url = Column(
        String(2048),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
