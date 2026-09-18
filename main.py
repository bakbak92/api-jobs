from fastapi import FastAPI
from routers.jobs import jobs_router
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(jobs_router)












