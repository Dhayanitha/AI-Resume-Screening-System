from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(vectors):
    jd_vectors = vectors[0:1]
    resume_vectors = vectors[1:]
    scores = cosine_similarity(jd_vectors,resume_vectors)[0]
    return scores