
FROM python:3.9.5-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8080
CMD ["python", "run.py"]
```