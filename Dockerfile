FROM python:3.9-buster

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY data /usr/src/app/data
COPY ./database.py /usr/src/app/database.py

#EXPOSE 5000
#CMD ["python", "database.py"]


