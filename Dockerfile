FROM python:3.9-alpine3.14

WORKDIR /app

COPY . . 

RUN pip install -r requirements.txt

EXPOSE 9000

RUN pytest

CMD ["python", "main.py"]