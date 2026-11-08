
import streamlit as st

from api import submit_assignment, get_submissions


st.set_page_config(
    page_title="Assignment Submission Portal",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Assignment Submission Portal")

st.write(
    "Submit your assignment using its URL. "
    "Your submission will be saved automatically."
)

st.divider()

# Submission form
st.subheader("Submit Your Assignment")

with st.form("submission_form"):

    student_name = st.text_input("Student Name")

    registration_number = st.text_input(
        "Registration Number"
    )

    assignment_title = st.text_input(
        "Assignment Title"
    )

    submission_url = st.text_input(
        "Submission URL",
        placeholder="https://github.com/username/repository"
    )

    submitted = st.form_submit_button(
        "Submit Assignment",
        use_container_width=True
    )

    if submitted:

        # Frontend required-field validation
        if not student_name.strip():
            st.error("Student name is required.")

        elif not registration_number.strip():
            st.error("Registration number is required.")

        elif not assignment_title.strip():
            st.error("Assignment title is required.")

        elif not submission_url.strip():
            st.error("Submission URL is required.")

        else:

            data = {
                "student_name": student_name.strip(),
                "registration_number": registration_number.strip(),
                "assignment_title": assignment_title.strip(),
                "submission_url": submission_url.strip()
            }

            success, result = submit_assignment(data)

            if success:
                st.success("Assignment submitted successfully!")
                st.rerun()

            else:
                details = result.get("detail", "Submission failed.")

                if isinstance(details, list):
                    for error in details:
                        message = error.get("msg", "Invalid input")
                        st.error(message)
                else:
                    st.error(str(details))


st.divider()

# Display saved submissions
st.subheader("📋 Saved Submissions")

submissions = get_submissions()

if submissions is None:

    st.error(
        "Cannot retrieve submissions. "
        "Please make sure the FastAPI backend is running."
    )

elif not submissions:

    st.info("No submissions have been received yet.")

else:

    st.write(f"Total submissions: {len(submissions)}")

    for submission in submissions:

        with st.container(border=True):

            st.write(
                f"**{submission['student_name']}**"
            )

            st.write(
                f"Registration: {submission['registration_number']}"
            )

            st.write(
                f"Assignment: {submission['assignment_title']}"
            )

            st.link_button(
                "View Submission",
                submission["submission_url"]
            )

            st.caption(
                f"Submission ID: {submission['id']} | "
                f"Submitted: {submission['created_at']}"
            )
