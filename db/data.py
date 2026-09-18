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
        skills=["Roadmapping", "Agile", "User Research"],
        remote=True
    ),
    JobResponse(
        id=4,
        title="Marketing Manager",
        company="Twitter",
        location="Los Angeles",
        salary=100000,
        skills=["SEO", "Content Strategy", "Analytics"],
        remote=False
    ),
    JobResponse(
        id=5,
        title="Sales Manager",
        company="LinkedIn",
        location="New York",
        salary=100000,
        skills=["CRM", "Negotiation", "Lead Generation"],
        remote=False
    ),
    JobResponse(
        id=6,
        title="HR Manager",
        company="Google",
        location="San Francisco",
        salary=100000,
        skills=["Recruiting", "Employee Relations", "Talent Management"],
        remote=True
    ),
    JobResponse(
        id=7,
        title="IT Manager",
        company="Google",
        location="San Francisco",
        salary=100000,
        skills=["Cloud Infrastructure", "Networking", "Cybersecurity"],
        remote=True
    ),
    JobResponse(
        id=8,
        title="Finance Manager",
        company="Google",
        location="San Francisco",
        salary=100000,
        skills=["Financial Analysis", "Budgeting", "Excel"],
        remote=True
    ),
    JobResponse(
        id=9,
        title="Legal Manager",
        company="Google",
        location="San Francisco",
        salary=100000,
        skills=["Contract Law", "Compliance", "Corporate Law"],
        remote=True
    ),
    JobResponse(
        id=10,
        title="Customer Service Manager",
        company="Google",
        location="San Francisco",
        salary=100000,
        skills=["Zendesk", "Conflict Resolution", "Customer Success"],
        remote=True
    ),
]

