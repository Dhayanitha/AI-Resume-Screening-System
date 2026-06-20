from src.loader.data_loader import load_resumes,load_job_description
from src.preprocessing.text_cleaner import clean_text,download_nltk_resources

from src.embeddings.tfidf_vectorizer import create_tfidf_vectors
from src.matching.similarity_engine import compute_similarity
from src.ranking.ranking_engine import rank_resumes

from src.explainability.keyword_match import extract_keywords,find_keyword_matches

from src.preprocessing.skill_extractor import extract_skills,match_skill

from src.embeddings.transformers_embeddings import get_embeddings,compute_transformer_similarity


download_nltk_resources()

resume_folder = "data/resumes"
job_file = "data/job_description/job.txt"

resumes = load_resumes(resume_folder)
job_description = load_job_description(job_file)

print("Loaded Resumes:",len(resumes))

clean_job = clean_text(job_description)
clean_resumes = [clean_text(resume) for resume in resumes]
job_skills = extract_skills(clean_job)

print("\nClean Job Description:\n", clean_job)

print("\nCleaned Resumes:")

for r in clean_resumes:
    print("-",r)

vectorizer, vectors = create_tfidf_vectors(clean_job,clean_resumes)
tfidf_scores = compute_similarity(vectors=vectors)

embeddings = get_embeddings(clean_job,clean_resumes)
transformer_scores = compute_transformer_similarity(embeddings)

final_scores = []

for i in range(len(resumes)):

    resume_skills = extract_skills(clean_resumes[i])
    skill_matches = match_skill(job_skills, resume_skills)
    skill_score = len(skill_matches) / (len(job_skills) + 1)
    score = (
        0.5 * transformer_scores[i] +
        0.3 * tfidf_scores[i] +
        0.2 * skill_score
    )
    final_scores.append(score)

ranked_resumes = rank_resumes(resumes,clean_resumes,final_scores)
jd_keywords = extract_keywords(clean_job)

print("\n   Final Ranking with Explaination:\n")

for i,(resume,clean_resume,score) in enumerate(ranked_resumes,1):
    resume_keywords = extract_keywords(clean_resume)
    matches = find_keyword_matches(jd_keywords,resume_keywords)

    resume_skills = extract_skills(clean_resume)
    skill_matches = match_skill(job_skills,resume_skills)

    tfidf_score = tfidf_scores[i - 1]
    transformer_score = transformer_scores[i-1]

    print(f"{i}. Final Score: {score:.4f}")
    print(f"   TF-IDF:{tfidf_score:.4f}|Transformer: {transformer_score:.4f}")
    print(f"   Resumes: {resume[:100]}....\n")

    print("    Skills Found:",resume_skills)
    if skill_matches:
        print("    Skill Match:",skill_matches)
    else:
        print("    No strong skill match")

    if matches:
        print("   Matched Keywords:", matches[:5])
    else:
        print("   No strong keyword match")

    print()

best_resume,_,best_score = ranked_resumes[0]
print("BEST MATCH:")
print(best_resume[:150],"....")
print("Score:",round(best_score,4))

