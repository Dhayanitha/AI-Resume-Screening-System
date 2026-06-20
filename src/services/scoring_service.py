from src.embeddings.tfidf_vectorizer import create_tfidf_vectors
from src.matching.similarity_engine import compute_similarity

from src.embeddings.transformers_embeddings import (
    get_embeddings,
    compute_transformer_similarity
)

from src.preprocessing.skill_extractor import (
    extract_skills,
    match_skill
)

from src.faiss.faiss_index import (
    build_faiss_index,search_similar
)

def calculate_scores(clean_job, clean_resumes, job_skills):

    # TF-IDF
    _, vectors = create_tfidf_vectors(clean_job, clean_resumes)

    tfidf_scores = compute_similarity(vectors)

    # Transformer
    embeddings = get_embeddings(clean_job, clean_resumes)

    job_embedding = embeddings[0]
    resume_embeddings = embeddings[1:]
    index = build_faiss_index(resume_embeddings)
    fiass_scores, fiass_ids = search_similar(index, job_embedding,top_k= min(5,len(clean_resumes)))
    print("\n FIASS Top Matches")
    for score, idx in zip(fiass_scores,fiass_ids):
        print(f"Resume {idx} -> {score:.4f}")
        
    transformer_scores = compute_transformer_similarity(embeddings)

    processed = []

    for i in range(len(clean_resumes)):

        resume_skills = extract_skills(clean_resumes[i])

        skill_matches = match_skill(
            job_skills,
            resume_skills
        )

        skill_score = len(skill_matches) / (len(job_skills) + 1)

        final_score = (
            0.6 * transformer_scores[i]
            + 0.2 * tfidf_scores[i]
            + 0.2 * skill_score
        )

        processed.append({
            "clean_resume": clean_resumes[i],
            "transformer": transformer_scores[i],
            "tfidf": tfidf_scores[i],
            "skill_score": skill_score,
            "final_score": final_score,
            "skills": resume_skills,
            "skill_matches": skill_matches
        })

    return processed