import logging
import time

from fastapi import FastAPI, Request
from routers.jobs import jobs_router

logger = logging.getLogger("uvicorn.access")
app = FastAPI()


@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000
    response.headers["X-Process-Time"] = f"{duration_ms:.2f}ms"
    logger.info("%s %s - %.2fms", request.method, request.url.path, duration_ms)
    return response


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(jobs_router)
