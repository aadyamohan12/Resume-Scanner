import streamlit as st
from modules import utils, screener



st.title("📊 Screening Results")

if not all(k in st.session_state for k in ["must_skills", "nice_skills", "resumes"]):
    st.warning("Please complete the steps on the Home page first.")
    st.stop()

must_skills = st.session_state.must_skills
nice_skills = st.session_state.nice_skills
resumes = st.session_state.resumes

ranked_resumes = []

for resume in resumes:
    ext = resume.name.split(".")[-1].lower()
    text = utils.clean_text(utils.extract_text(resume, f".{ext}"))
    score, must_match, nice_match = screener.calculate_weighted_score(must_skills, nice_skills, text)
    ranked_resumes.append({
        "name": resume.name,
        "file": resume,
        "text": text,
        "score": score,
        "must": must_match,
        "nice": nice_match
    })

ranked_resumes.sort(key=lambda r: r["score"], reverse=True)
st.session_state.ranked_resumes = ranked_resumes

for idx, r in enumerate(ranked_resumes):
    with st.container():
        col1, col2 = st.columns([5, 1])
        with col1:
            st.subheader(f"📄 {r['name']}")
            st.markdown(f"**Match Score:** `{r['score'] * 100:.2f}%`")
            st.progress(r["score"])
            st.markdown(f"✅ **Must-Have Matches**: {', '.join(r['must']) or 'None'}")
            st.markdown(f"💡 **Nice-to-Have Matches**: {', '.join(r['nice']) or 'None'}")
        with col2:
            if st.button("🔍 View", key=f"view_{idx}"):
                st.session_state.selected_resume = r["name"]
                st.switch_page("pages/3_CandidateDetails.py")
