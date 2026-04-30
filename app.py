import streamlit as st
from utils import get_similarity, extract_skills

st.title("📄 Resume Screening AI Tool")

job_desc = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True)

if uploaded_files and job_desc:

    results = []   # ✅ IMPORTANT: define before loop

    for file in uploaded_files:

        if file.name.endswith(".txt"):
            resume_text = file.read().decode("utf-8")

        else:
            st.error("Unsupported file format")
            continue

        score = get_similarity(resume_text, job_desc)
        skills = extract_skills(resume_text)

        results.append((file.name, score, skills))

    # ✅ Display results AFTER loop
    st.subheader("📊 Candidate Ranking")

    for name, score, skills in results:
        st.write(f"📄 {name}")
        st.write(f"✅ Match Score: {score}%")
        st.write(f"🧠 Skills Found: {', '.join(skills) if skills else 'No matching skills'}")
        st.write("---")
