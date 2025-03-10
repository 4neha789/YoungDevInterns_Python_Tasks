import streamlit as st

def main():
    st.title("Digital Resume")
    
    # Personal Information
    st.header("Personal Information")
    name = st.text_input("Name", "John Doe")
    email = st.text_input("Email", "johndoe@example.com")
    phone = st.text_input("Phone", "123-456-7890")
    linkedin = st.text_input("LinkedIn", "https://www.linkedin.com/in/johndoe")
    
    # Summary
    st.header("Summary")
    summary = st.text_area("Brief Summary", "Experienced software engineer with expertise in Python and web development.")
    
    # Skills
    st.header("Skills")
    skills = st.text_area("List your skills", "Python, Django, JavaScript, React, SQL")
    
    # Experience
    st.header("Experience")
    job_title = st.text_input("Job Title", "Software Engineer")
    company = st.text_input("Company", "Tech Corp")
    duration = st.text_input("Duration", "2020 - Present")
    job_desc = st.text_area("Job Description", "Developed and maintained web applications using Python and JavaScript.")
    
    # Education
    st.header("Education")
    degree = st.text_input("Degree", "B.Sc. in Computer Science")
    university = st.text_input("University", "XYZ University")
    grad_year = st.text_input("Graduation Year", "2019")
    
    # Display Resume
    st.header("Generated Resume")
    st.subheader(name)
    st.write(f"Email: {email}")
    st.write(f"Phone: {phone}")
    st.write(f"[LinkedIn]({linkedin})")
    st.write("\n**Summary:**", summary)
    st.write("\n**Skills:**", skills)
    st.write(f"\n**Experience:** {job_title} at {company} ({duration})")
    st.write(job_desc)
    st.write(f"\n**Education:** {degree} from {university}, {grad_year}")

if __name__ == "__main__":
    main()
