from db.data import jobs
from schemas.job_schema import JobResponse, JobCreate
from fastapi import HTTPException

def get_jobs() -> list[JobResponse]:
    return jobs

def create_job(job: JobCreate) -> JobResponse:
    new_job = JobResponse(
        id=len(jobs) + 1,
        **job.model_dump()
    )
    jobs.append(new_job)
    return new_job

def get_job(id: int) -> JobResponse:
    job_found = next((job for job in jobs if job.id == id), None)
    if job_found is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job_found

def update_job(id: int, job: JobCreate) -> JobResponse:
    job_found = next((job for job in jobs if job.id == id), None)
    if job_found is None:
        raise HTTPException(status_code=404, detail="Job not found")
    job_found.title = job.title
    job_found.company = job.company
    job_found.location = job.location
    job_found.salary = job.salary
    job_found.skills = job.skills
    job_found.remote = job.remote
    return job_found