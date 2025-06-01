import streamlit as st

# ------------------- CONFIG -------------------
st.set_page_config(
    page_title="Resume Screener J.A.R.V.I.S.",
    page_icon="🧠",
    layout="wide"
)

# ------------------- HEADER -------------------
st.markdown("""
    <style>
    .big-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-top: 2rem;
        color: #2c3e50;
    }
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🧠 Resume Screener — J.A.R.V.I.S.</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI assistant for fast and intelligent resume shortlisting</div>', unsafe_allow_html=True)

# ------------------- HOMEPAGE REDIRECTION -------------------
st.markdown("👉 Use the sidebar to begin. Start from **Home** to input your Job Description and Resumes.")
st.markdown("💡 The app will guide you through screening and detailed resume analysis.")

# Optionally, redirect to Home on app start
if "must_skills" in st.session_state and "resumes" in st.session_state:
    st.switch_page("pages/2_ScreeningResults.py")
else:
    st.switch_page("pages/1_Home.py")
