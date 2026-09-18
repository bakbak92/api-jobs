from fastapi import APIRouter
from services.job_service import get_jobs, create_job, get_job, update_job, delete_job
from schemas.job_schema import JobCreate, JobResponse

jobs_router = APIRouter(prefix="/jobs", tags=["jobs"])

@jobs_router.get("/", response_model=list[JobResponse], status_code=200)
def read_jobs():
    return get_jobs()

@jobs_router.get("/{id}", response_model=JobResponse, status_code=200)
def read_job(id: int):
    return get_job(id)  

@jobs_router.put("/{id}", response_model=JobResponse, status_code=200)
def put_job(id: int, job: JobCreate):
    return update_job(id, job)

@jobs_router.post("/", response_model=JobResponse, status_code=201)
def post_job(job: JobCreate):
    return create_job(job)

@jobs_router.delete("/{id}", response_model=JobResponse, status_code=200)
def remove_job(id: int):
    return delete_job(id)