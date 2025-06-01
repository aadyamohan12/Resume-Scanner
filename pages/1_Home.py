import streamlit as st
from modules import utils, parser



job_keywords = {
    "Data Analyst": ["SQL", "Python", "Excel", "Power BI", "Data Cleaning", "Statistics"],
    "Data Scientist": ["Python", "Machine Learning", "Pandas", "Deep Learning", "Scikit-learn"],
    "Software Engineer": ["Java", "Python", "Git", "React", "Node.js", "OOP"]
}

st.title("🏠 Home — Resume Screener J.A.R.V.I.S.")

with st.form("jd_form", clear_on_submit=False):
    job_role = st.text_input("👔 Enter Job Role")

    if job_role:
        jd_input_method = st.radio("📄 Upload JD or Paste Text", ["Upload File", "Paste Text"])
        jd_text = ""
        if jd_input_method == "Upload File":
            jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])
            if jd_file:
                ext = jd_file.name.split(".")[-1].lower()
                jd_text = utils.extract_text(jd_file, f".{ext}")
        else:
            jd_text = st.text_area("Paste Job Description", height=200)

    selected_keywords = []
    if job_role:
        default_keywords = job_keywords.get(job_role.strip(), [])
        selected_keywords = st.multiselect("✨ Add Extra Keywords", default_keywords)

    resume_files = st.file_uploader("📎 Upload Resumes", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    submitted = st.form_submit_button("🔍 Analyze Resumes")

if submitted and jd_text and resume_files:
    must_skills, nice_skills = parser.extract_skills_from_jd_by_section(jd_text)
    must_skills.extend(selected_keywords)

    st.session_state.job_role = job_role
    st.session_state.jd_text = jd_text
    st.session_state.must_skills = list(set(must_skills))
    st.session_state.nice_skills = list(set(nice_skills))
    st.session_state.resumes = resume_files
    st.switch_page("pages/2_ScreeningResults.py")
