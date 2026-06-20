from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(job_description,resumes):
    documents = [job_description]+resumes
    embeddings = model.encode(documents)
    return embeddings

def compute_transformer_similarity(embeddings):
    jd_embedding= embeddings[0].reshape(1,-1)
    resume_embeddings = embeddings[1:]
    scores = cosine_similarity(jd_embedding,resume_embeddings)[0]
    return scores