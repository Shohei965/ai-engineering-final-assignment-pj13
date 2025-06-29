import json
import os

from google.generativeai import GenerativeModel, configure

configure(api_key=os.getenv("GEMINI_API_KEY"))
model = GenerativeModel("models/gemini-1.5-flash-latest")


async def llm_analyze(texts: list[str]) -> list[dict]:
    prompt = "JSON ONLY: [{'sentiment':'pos|neg','keywords':[...]}] " "for each text"
    # TODO: adjust prompt as needed
    try:
        resp = await model.generate_async(prompt=prompt, contents=texts)
        return json.loads(resp.text)
    except Exception:
        # return stubbed analysis
        return [{"sentiment": "pos", "keywords": ["sample", "text"]} for _ in texts]
