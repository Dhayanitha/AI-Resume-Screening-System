from fastapi import APIRouter

from src.models.request_models import (
    JobRequest
)

from src.services.resume_service import (
    process_resumes
)

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "AI Resume Screening System Running"
    }

@router.post("/rank_resumes")
async def rank_resumes_api(request: JobRequest):

    return await process_resumes(request)