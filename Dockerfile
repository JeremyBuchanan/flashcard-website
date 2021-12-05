FROM python:3.9

WORKDIR /flask-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./flask-website ./flask-website

CMD ["python", "./flask-website/run.py"]