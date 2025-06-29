FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir -r <(python - <<'PY'
import tomllib
import sys
with open('pyproject.toml','rb') as f:
    data=tomllib.load(f)
req=data['project']['dependencies']
print('\n'.join(req))
PY
)
COPY src/ ./src/
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
