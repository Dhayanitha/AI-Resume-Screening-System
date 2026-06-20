from pydantic import BaseModel

class JobRequest(BaseModel):
    job_description: str
    min_score:float =0.0
    required_skills:list[str] = []