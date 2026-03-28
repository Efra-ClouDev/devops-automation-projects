FROM python:3.11-slim

WORKDIR /app

COPY log_analyzer.py .
COPY server.log .

CMD ["python", "log_analyzer.py"]