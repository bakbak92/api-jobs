from fastapi import APIRouter, Query
from services.job_service import get_jobs, create_job, get_job, update_job, delete_job, analyze_job
from schemas.job_schema import JobCreate, JobUpdate, JobResponse, JobFilter, JobAnalyzeRequest, JobAnalyzeResponse
from typing import Annotated

jobs_router = APIRouter(prefix="/jobs", tags=["jobs"])

@jobs_router.get("/", response_model=list[JobResponse], status_code=200)
def read_jobs(filter: Annotated[JobFilter, Query()]):
    return get_jobs(filter)

@jobs_router.get("/{id}", response_model=JobResponse, status_code=200)
def read_job(id: int):
    return get_job(id)  

@jobs_router.patch("/{id}", response_model=JobResponse, status_code=200)
def patch_job(id: int, job: JobUpdate):
    return update_job(id, job)

@jobs_router.post("/", response_model=JobResponse, status_code=201)
def post_job(job: JobCreate):
    return create_job(job)

@jobs_router.delete("/{id}", response_model=JobResponse, status_code=200)
def remove_job(id: int):
    return delete_job(id)

@jobs_router.post("/analyze", response_model=JobAnalyzeResponse, status_code=200)
async def post_analyze_job(request: JobAnalyzeRequest):
    return await analyze_job(request)