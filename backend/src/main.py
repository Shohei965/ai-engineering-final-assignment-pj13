import asyncio
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel

from .graph import runner

app = FastAPI()

jobs: dict[str, dict] = {}


class SearchRequest(BaseModel):
    keywords: list[str]


@app.post("/api/search")
async def search(req: SearchRequest):
    job_id = str(uuid4())

    async def task():
        result = await runner(req.keywords)
        jobs[job_id] = result

    asyncio.create_task(task())
    return {"job_id": job_id}


@app.get("/api/result/{job_id}")
async def result(job_id: str):
    if job_id not in jobs:
        return {"status": "running"}
    return jobs[job_id]
