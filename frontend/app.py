import streamlit as st
import requests

st.title("AI Resume Screening System")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files and st.button("Upload Resumes"):
    
    for file in uploaded_files:

        files = {
            "file": (
                file.name,
                file.getvalue(),
                file.type
            )
        }

        requests.post(
            "http://127.0.0.1:8000/upload_resume",
            files=files
        )

    st.success(
        f"{len(uploaded_files)} resumes uploaded"
    )


job_description = st.text_area(
    "Enter Job Description"
)

min_score = st.slider(
    "Minimum Score",
    0.0,
    1.0,
    0.0
)

required_skills = st.text_input(
    "Required Skills (comma seperated)"
)

if st.button("Analyze Resumes"):
    skills = [
        s.strip()
        for s in required_skills.split(",")
        if s.strip()
    ]

    payload = {
        "job_description":job_description,
        "min_score":min_score,
        "required_skills":skills
    }

    response = requests.post(
        "http://127.0.0.1:8000/rank_resumes",
        json=payload
    )

    results = response.json()

    st.success("Analysis Complete")

    for item in results["rankings"]:
        with st.expander(
            f" Rank {item['rank']} | Score {item['final_score']:.4f}"
        ):

            st.write("### Score Breakdown")
            st.json(item["score_breakdown"])

            st.write("### Matched Skills")
            st.write(item["skill_matched"])

            st.write("### Summary")
            st.success(item["summary"])

            st.write("### LLM Summary")
            st.info(item["llm_summary"])

            st.write("### Highlighted Resume")
            st.markdown(
                item["highlighted_resume"],
                unsafe_allow_html=True
            )