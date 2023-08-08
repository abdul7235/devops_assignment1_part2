FROM python:latest

ADD . /devops_assignment1_part1

WORKDIR /devops_assignment1_part1

RUN pip install -r requirements.txt

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 8000 --workers 2
