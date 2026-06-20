from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="AI Resume Screening System",
    description="""
    Resume ranking system using:
    - TF-IDF
    - Sentence Transformers
    - Skill Matching
    - FAISS Search
    - LLM Explanations
    """,
    version="1.0"
)
app.include_router(router)