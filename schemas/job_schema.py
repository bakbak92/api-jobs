from pydantic import BaseModel, Field

class JobCreate(BaseModel):
    title: str = Field(min_length=2)
    company: str
    location: str
    salary: int = Field(gt=0)
    skills: list[str]
    remote: bool

class JobUpdate(BaseModel):
    title: str = Field(min_length=2)
    company: str
    location: str
    salary: int = Field(gt=0)
    skills: list[str]
    remote: bool

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    salary: int
    skills: list[str]
    remote: bool