import streamlit as st

# Initialize an empty list to store student grades
if 'grades' not in st.session_state:
    st.session_state.grades = []

# Title for the app
st.title("Student Grade Tracker")

# Input fields for student name and grade
student_name = st.text_input("Enter student name:")
student_grade = st.number_input("Enter grade:", min_value=0, max_value=100, value=0)

# Button to add grade
if st.button("Add Grade"):
    st.session_state.grades.append((student_name, student_grade))  # Add the name and grade
    st.write(f"Added grade for {student_name}: {student_grade}")

# Display all grades as a table
if st.session_state.grades:
    st.write("### All Grades:")
    st.dataframe(st.session_state.grades)  # Display the list of grades

    # Calculate the average grade
    average_grade = sum([grade for _, grade in st.session_state.grades]) / len(st.session_state.grades)
    st.write(f"### Average Grade: {average_grade:.2f}")
