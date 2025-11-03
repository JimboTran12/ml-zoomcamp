FROM python:3.13.5-slim-bookworm
WORKDIR /code
COPY pipeline_v2.bin .
RUN pip install uv
COPY ["pyproject.toml", "uv.lock", "main.py", "./"]
RUN uv sync
EXPOSE 8000
ENTRYPOINT ["uv", "run", "uvicorn",  "main:app", "--host", "0.0.0.0", "--port", "8000" ]

