from pydantic import BaseModel

class Files(BaseModel):
    file_id: str
    job_id: str
