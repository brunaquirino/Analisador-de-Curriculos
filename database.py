from tinydb import TinyDB, Query

class AnalyzeDatabase(TinyDB):
    def __init__(self, db_path='db.json'):
        super().__init__(db_path)
        self.jobs = self.table('jobs')
        self.resume = self.table('resume')
        self.analysis = self.table('analysis')
        self.files = self.table('files')

    def get_job_by_name(self, name):
        job = Query()
        result = self.jobs.search(job.name == name)
        return result[0] if result else None
    
    def get_resume_by_id(self, id):
        resume = Query()
        result = self.resume.search(resume.id == id)
        return result[0] if result else None
    
    def get_analysis_by_job_id(self, job_id):
        analysis = Query()
        result = self.analysis.search(analysis.job_id == job_id)
        return result
    
    def get_resume_by_job_id(self, job_id):
        resume = Query()
        result = self.resume.search(resume.job_id == job_id)
        return result
    
    def delete_all_resumes_by_job_id(self, job_id):
        resume = Query()
        self.resume.remove(resume.job_id == job_id)

    def delete_all_analysis_by_job_id(self, job_id):
        analysis = Query()
        self.analysis.remove(analysis.job_id == job_id)

    def delete_all_files_by_job_id(self, job_id):
        files = Query()
        self.files.remove(files.job_id == job_id)