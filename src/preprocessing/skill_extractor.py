import re

def load_skills(file_path="data/skills/skills.txt"):
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

SKILLS_DB = load_skills()
SKILL_SYNONYMS = {
    "ml": "machine learning",
    "nlp": "natural language processing",
    "dl": "deep learning"
}

def normalize_text(text):

    text = text.lower()

    for short, full in SKILL_SYNONYMS.items():
        text = text.replace(short, full)

    return text

def extract_skills(text):
    text = normalize_text(text)
    found_skills = []
    for skill in SKILLS_DB:
            if re.search(rf"\b{re.escape(skill)}\b",text):
                found_skills.append(skill)
    return list(set(found_skills))

def match_skill(job_skils,resume_skills):
    matched = set(job_skils).intersection(set(resume_skills))
    return list(matched)
