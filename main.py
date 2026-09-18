from fastapi import FastAPI
from services.job_service import get_jobs, create_job, get_job, update_job
from schemas.job_schema import JobCreate
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/jobs")
def read_jobs():
    return get_jobs()

@app.post("/jobs")
def post_job(job: JobCreate):
    return create_job(job)

@app.get("/jobs/{id}")
def read_job(id: int):
    return get_job(id)  

@app.put("/jobs/{id}")
def put_job(id: int, job: JobCreate):
    return update_job(id, job)













