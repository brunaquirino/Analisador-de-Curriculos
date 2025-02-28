from pydantic import BaseModel
from typing import List

class Analysis(BaseModel):
    id: str
    job_id: str
    resume_id: str
    name: str
    skills: List[str]
    education: List[str]
    languages: List[str]
    score: float #número com ponto: 1.0