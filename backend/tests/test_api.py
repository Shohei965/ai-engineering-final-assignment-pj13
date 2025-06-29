import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_search_and_result():
    resp = client.post("/api/search", json={"keywords": ["test"]})
    assert resp.status_code == 200
    job_id = resp.json()["job_id"]
    for _ in range(5):
        res = client.get(f"/api/result/{job_id}")
        if res.json().get("summary"):
            break
        asyncio.sleep(0.1)
    assert "summary" in res.json()
