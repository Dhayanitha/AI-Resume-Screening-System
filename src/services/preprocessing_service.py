from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.skill_extractor import extract_skills

def preprocess_job(job_description):
    
    clean_job = clean_text(job_description)

    job_skills = extract_skills(clean_job)

    return {
        "clean_job": clean_job,
        "job_skills": job_skills
    }


def preprocess_resumes(resumes):

    clean_resumes = [clean_text(r) for r in resumes]

    return clean_resumes