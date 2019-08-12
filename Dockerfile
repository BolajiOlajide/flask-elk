FROM python:3

ADD requirements.txt /app/requirements.txt

WORKDIR /app/

RUN pip install pipenv

RUN pipenv install

ENTRYPOINT ["python"]

CMD ["./app.py", "--host=0.0.0.0"]
