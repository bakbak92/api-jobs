from pydantic import BaseModel, Field

class JobCreate(BaseModel):
    title: str = Field(min_length=2)
    company: str
    location: str
    salary: int = Field(gt=0)
    skills: list[str]
    remote: bool

class JobUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2)
    company: str | None = None
    location: str | None = None
    salary: int | None = Field(default=None, gt=0)
    skills: list[str] | None = None
    remote: bool | None = None

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    salary: int
    skills: list[str]
    remote: bool

class JobFilter(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None
    salary_min: int = Field(default=0, ge=0)
    skill: str | None = None
    remote: bool | None = None
    limit: int = Field(default=10, ge=10, le=100)