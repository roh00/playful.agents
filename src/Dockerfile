FROM python:3.9-slim

WORKDIR /testApp

COPY requirement.txt .

RUN pip install -r requrement.txt

COPY . .

EXPOSE 8000

#CMD ["python", "app.py"]
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]