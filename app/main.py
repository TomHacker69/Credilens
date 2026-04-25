import os
import streamlit as st

from app.parser import extract_resume_text
from app.utils import load_json
from app.analyzer import analyze_resume
from app.scorer import calculate_authenticity_score, get_score_label, generate_suggestions


st.set_page_config(page_title="ResumeTruth AI", layout="wide")

st.title("ResumeTruth AI")
st.subheader("Behavioral Resume Authenticity Detector")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    os.makedirs("resumes", exist_ok=True)

    file_path = os.path.join("resumes", uploaded_file.name)

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    try:
        resume_text = extract_resume_text(file_path)

        skills = load_json("data/skills.json")
        buzzwords = load_json("data/buzzwords.json")

        analysis = analyze_resume(resume_text, skills, buzzwords)

        score = calculate_authenticity_score(analysis)
        label = get_score_label(score)
        suggestions = generate_suggestions(analysis)

        st.success("Resume analyzed successfully.")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Authenticity Score", f"{score}/100")
            st.write(f"**Result:** {label}")

        with col2:
            st.write("### Extracted Skills")
            if analysis["skills"]:
                st.write(", ".join(analysis["skills"]))
            else:
                st.warning("No technical skills detected.")

        st.write("### Detected Buzzwords")
        if analysis["buzzwords"]:
            st.write(", ".join(analysis["buzzwords"]))
        else:
            st.success("No major buzzword stuffing detected.")

        st.write("### Red Flags")
        if analysis["red_flags"]:
            for flag in analysis["red_flags"]:
                st.error(flag)
        else:
            st.success("No major authenticity red flags found.")

        st.write("### Suggestions")
        for suggestion in suggestions:
            st.info(suggestion)

        with st.expander("View Extracted Resume Text"):
            st.write(resume_text)

    except Exception as error:
        st.error(f"Error: {error}")
