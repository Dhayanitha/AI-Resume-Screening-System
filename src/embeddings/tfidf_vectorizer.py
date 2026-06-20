from sklearn.feature_extraction.text import TfidfVectorizer
def create_tfidf_vectors(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    return vectorizer,vectors
