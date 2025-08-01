FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -e .

EXPOSE 6006

CMD [ "python", "application.py" ]
