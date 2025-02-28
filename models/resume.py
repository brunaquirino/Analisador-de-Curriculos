from pydantic import BaseModel

class Resume(BaseModel):
    id: str
    job_id: str
    content: str
    feedback: str
    file: str