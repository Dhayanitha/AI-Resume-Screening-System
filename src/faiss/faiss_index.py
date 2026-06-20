import faiss
import numpy as np 

def build_faiss_index(embeddings):

    vectors = np.array(
        embeddings,
        dtype=np.float32
    )

    dimension = vectors.shape[1]
    index = faiss.IndexFlatIP(dimension)
    faiss.normalize_L2(vectors)
    index.add(vectors)
    return index 

def search_similar(index, job_embedding,top_k=5):
    query = np.array(
        [job_embedding],
        dtype = np.float32
        )
    faiss.normalize_L2(query)
    scores , ids = index.search(
        query,top_k
    )
    return scores[0],ids[0]

