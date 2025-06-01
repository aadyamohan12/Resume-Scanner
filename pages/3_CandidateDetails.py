import streamlit as st
from modules import utils, screener


st.title("🧾 Candidate Details")

if "selected_resume" not in st.session_state or "ranked_resumes" not in st.session_state:
    st.warning("Please select a resume from the Screening Results page.")
    st.stop()

resume_name = st.session_state.selected_resume
resume_data = next((r for r in st.session_state.ranked_resumes if r["name"] == resume_name), None)

if not resume_data:
    st.error("Resume not found.")
    st.stop()

st.header(resume_data["name"])
st.markdown(f"**Match Score:** `{resume_data['score'] * 100:.2f}%`")
st.markdown(f"✅ **Must-Have Matches:** {', '.join(resume_data['must']) or 'None'}")
st.markdown(f"💡 **Nice-to-Have Matches:** {', '.join(resume_data['nice']) or 'None'}")
st.success("📝 Summary: " + screener.summarize_resume(resume_data["text"]))

ext = resume_data["file"].name.split(".")[-1].lower()
if ext == "pdf":
    images = utils.preview_pdf_all_pages(resume_data["file"])
    for i, img in enumerate(images):
        st.image(img, caption=f"Page {i + 1}", use_container_width=True)
else:
    st.image(utils.resume_to_image(resume_data["text"]), caption="Resume Preview", use_container_width=True)

st.markdown("### 💬 Message Candidate")
msg = st.text_area("Your Message", placeholder="Hi, we'd like to schedule a quick call with you...")
if msg:
    st.info(f"📩 Message ready to send:\n\n{msg}")

if st.button("🤖 Go to Chatbot"):
    st.switch_page("chatbot")  # assuming chatbot is an extra page you might build later
