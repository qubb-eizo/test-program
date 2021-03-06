FROM python:3.9

RUN mkdir /opt/project
WORKDIR /opt/project

RUN apt-get update

COPY app/ ./
COPY commands/ ./
COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

CMD ["bash"]
