import uuid
from helper import extract_data_analysis, get_pdf_paths, read_pdf
from database import AnalyzeDatabase
from ai import GroqClient
from models.resume import Resume
from models.files import Files
from models.analysis import Analysis

database = AnalyzeDatabase()
ai = GroqClient()
job = database.get_job_by_name("Vaga de Gestor Comercial de B2B")

cv_paths = get_pdf_paths(directory = 'curriculos')

for path in cv_paths:
    content = read_pdf(path)
    summary = ai.summarize_cv(content)
    print(summary)
    feedback = ai.generate_feedback(content, job)
    print(feedback)
    score = ai.generate_score(content, job)
    print(score)

    resume_schema = Resume(
        id=str(uuid.uuid4()),
        job_id=job.get('id'), 
        content=summary,
        file=str(path),
        feedback=feedback
    )

    files_schema = Files(
        file_id=str(uuid.uuid4()),
        job_id=job.get('id')
    )

    analysis_schema = extract_data_analysis(summary, resume_schema.job_id, resume_schema.id, score)

    database.resume.insert(resume_schema.model_dump())
    database.analysis.insert(analysis_schema.model_dump())
    database.files.insert(files_schema.model_dump())
    