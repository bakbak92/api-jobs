from schemas.job_schema import JobResponse
jobs: list[JobResponse] = [
    JobResponse(
        id=1,
        title="Software Engineer",
        company="Google",
        location="San Francisco",
        salary=100000,
        skills=["Python", "Java", "JavaScript"],
        remote=True
    ),
    JobResponse(
        id=2,
        title="Data Scientist",
        company="Amazon",
        location="New York",
        salary=120000,
        skills=["Python", "R", "SQL"],
        remote=False
    ),
    JobResponse(
        id=3,
        title="Product Manager",
        company="Facebook",
        location="Seattle",
        salary=110000,
        skills=["Python", "JavaScript", "SQL"],
        remote=True
    ),
]

