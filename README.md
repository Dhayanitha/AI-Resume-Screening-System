# AI Resume Screening System

An end-to-end NLP-powered Resume Screening System that automatically evaluates and ranks resumes against a job description using Machine Learning, Transformer Embeddings, FAISS Similarity Search, and Explainable AI.

The system helps recruiters identify the most relevant candidates by combining semantic similarity, keyword matching, and skill-based scoring.

---

## Features

### Resume Processing
- Upload resumes in PDF, DOCX, and TXT formats
- Automatic text extraction and parsing
- Resume preprocessing and cleaning

### NLP & Machine Learning
- Skill extraction from resumes
- TF-IDF similarity matching
- Sentence Transformer embeddings
- Semantic similarity scoring
- FAISS vector similarity search
- Hybrid ranking algorithm

### Explainable AI
- Skill match analysis
- Keyword match analysis
- Score breakdown
- AI-generated explanations
- Candidate summaries

### Application Layer
- FastAPI REST API
- Interactive Swagger Documentation
- Streamlit Web Interface
- SQLite Database Storage

---

## Tech Stack

### Backend
- FastAPI
- Python

### Machine Learning & NLP
- Scikit-Learn
- Sentence Transformers
- FAISS

### Database
- SQLite

### Frontend
- Streamlit

---

## Embedding Model

The system uses:

```text
all-MiniLM-L6-v2
```

This transformer model generates semantic embeddings that capture contextual meaning beyond simple keyword matching.

---

## Resume Ranking Workflow

```text
Resume Upload
      │
      ▼
Resume Parsing
      │
      ▼
Text Preprocessing
      │
      ▼
Skill Extraction
      │
      ▼
TF-IDF Similarity
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Similarity Search
      │
      ▼
Hybrid Scoring Engine
      │
      ▼
Resume Ranking
      │
      ▼
Explanation Generation
      │
      ▼
FastAPI API
      │
      ▼
Streamlit Dashboard
```

---

## Scoring Formula

The final ranking score is computed using a weighted combination of semantic similarity, keyword similarity, and skill matching.

```python
final_score = (
    0.6 * transformer_score
    + 0.2 * tfidf_score
    + 0.2 * skill_score
)
```

### Weight Distribution

| Component | Weight |
|------------|----------|
| Transformer Similarity | 60% |
| TF-IDF Similarity | 20% |
| Skill Matching | 20% |

Transformer similarity receives the highest weight because it captures semantic meaning more effectively than traditional keyword-based methods.

---

## Project Structure

```text
AI-Resume-Screening-System/

├── data/
├── frontend/
├── output/
├── scripts/

├── src/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── embeddings/
│   ├── explainability/
│   ├── faiss/
│   ├── loader/
│   ├── matching/
│   ├── models/
│   ├── preprocessing/
│   ├── repositories/
│   ├── services/
│   ├── storage/
│   └── utils/

├── requirements.txt
├── README.md
└── resume_screening.db
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Dhayanitha/AI-Resume-Screening-System.git

cd AI-Resume-Screening-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Start the FastAPI server:

```bash
uvicorn src.api.fastapi_app:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Launch the Streamlit application:

```bash
streamlit run frontend/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## API Endpoints

### Rank Resumes

**POST** `/rank_resumes`

Request Example:

```json
{
  "job_description": "Python NLP Engineer",
  "min_score": 0.3,
  "required_skills": [
    "python",
    "machine learning"
  ]
}
```

### Upload Resume

**POST** `/upload_resume`

Supported formats:

- PDF
- DOCX
- TXT

---

## Sample Output

The system returns:

- Candidate Rank
- Final Match Score
- TF-IDF Score
- Transformer Score
- Skill Match Score
- Matched Skills
- Matched Keywords
- Candidate Summary
- AI Explanation

---

## Application Screenshots

### Streamlit Frontend

<img width="960" height="1020" alt="image" src="https://github.com/user-attachments/assets/7e9bbfb9-fb67-448c-bf8f-5c9efe68d21d" />

### FastAPI Swagger Documentation

<img width="960" height="1020" alt="image" src="https://github.com/user-attachments/assets/fc113bd5-16e0-4ac3-97f0-c6d61683c5d3" />


---

## Future Improvements

- Docker Support
- Cloud Deployment
- User Authentication
- ATS Compatibility Scoring
- Resume Recommendation Engine
- Multi-Job Comparison
- Advanced Analytics Dashboard

---

## Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing (NLP)
- Information Retrieval
- Vector Databases
- Semantic Search
- Explainable AI
- REST API Development
- Machine Learning Pipelines
- Full-Stack AI Application Development

---

## Author

### Dhayanitha H

