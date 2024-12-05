FROM python:3.10-alpine

WORKDIR /code

COPY . /code

RUN pip install pdm
RUN pdm install

CMD ["pdm", "run", "fastapi", "run", "app/main.py", "--port", "80"]
