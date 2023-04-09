FROM python:3

RUN pip install --upgrade pip

COPY domainer.py .
COPY domainer domainer

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update 
RUN apt-get install -y iputils-ping

ENTRYPOINT [ "python", "domainer.py" ]