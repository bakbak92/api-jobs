from db.data import jobs
from schemas.job_schema import JobResponse, JobCreate, JobUpdate, JobFilter, JobAnalyzeRequest, JobAnalyzeResponse
from fastapi import HTTPException
from config import settings
from openai import AsyncOpenAI, APIError
import json

client = AsyncOpenAI(
    api_key=settings.openai_api_key,
)

def get_jobs(filter: JobFilter) -> list[JobResponse]:
    filtered_jobs = jobs
    if filter.title:
        filtered_jobs = [job for job in filtered_jobs if filter.title.lower() in job.title.lower()]
    if filter.company:
        filtered_jobs = [job for job in filtered_jobs if filter.company.lower() in job.company.lower()]
    if filter.location:
        filtered_jobs = [job for job in filtered_jobs if filter.location.lower() in job.location.lower()]
    if filter.salary_min:
        filtered_jobs = [job for job in filtered_jobs if job.salary >= filter.salary_min]
    if filter.skill:
        skill = filter.skill.lower()
        filtered_jobs = [job for job in filtered_jobs if any(skill in s.lower() for s in job.skills)]
    if filter.remote is not None:
        filtered_jobs = [job for job in filtered_jobs if job.remote == filter.remote]
    return filtered_jobs[:filter.limit]
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

def update_job(id: int, job: JobUpdate) -> JobResponse:
    job_found = next((existing for existing in jobs if existing.id == id), None)
    if job_found is None:
        raise HTTPException(status_code=404, detail="Job not found")
    updated_job = job_found.model_copy(update=job.model_dump(exclude_unset=True))
    jobs[jobs.index(job_found)] = updated_job
    return updated_job

def delete_job(id: int) -> JobResponse:
    job_found = next((job for job in jobs if job.id == id), None)
    if job_found is None:
        raise HTTPException(status_code=404, detail="Job not found")
    jobs.remove(job_found)
    return job_found

async def analyze_job(request: JobAnalyzeRequest) -> JobAnalyzeResponse:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You analyze job descriptions and extract the skills required for the job. "
                        'Respond only with a JSON object of the form: {"skills": ["skill1", "skill2"]}'
                    ),
                },
                {"role": "user", "content": request.description},
            ],
            max_tokens=300,
            temperature=0.2,
            response_format={"type": "json_object"},
        )
    except APIError as e:
        raise HTTPException(status_code=502, detail=f"OpenAI API error: {e.message}")

    content = response.choices[0].message.content or "{}"
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="Invalid JSON returned by OpenAI")

    skills = data.get("skills", [])
    if not isinstance(skills, list):
        raise HTTPException(status_code=502, detail="Unexpected response format from OpenAI")

    return JobAnalyzeResponse(skills=[s.strip() for s in skills if isinstance(s, str) and s.strip()])