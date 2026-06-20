from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def generate_explanation(job_text,resume_text,job_skills,resume_skills,score):
    matched_skills = list(set(job_skills).intersection(set(resume_skills)))
    job_words = set(job_text.split()) - set(ENGLISH_STOP_WORDS)
    resume_words = set(resume_text.split()) - set(ENGLISH_STOP_WORDS)
    matched_keywords = list(job_words.intersection(resume_words))
    matched_keywords = [w for w in matched_keywords if len(w)>3]
    summary = (
    f"Candidate matched {len(matched_skills)} important skills "
    f"including {', '.join(matched_skills[:3])}. "
    f"Resume also shows relevant experience in "
    f"{', '.join(matched_keywords[:3])}."
    )

    explanation = {
        "score":round(score,4),
        "matched_skills":matched_skills,
        "matched_keywords": matched_keywords[:8],
        "summary": summary
    }
    return explanation