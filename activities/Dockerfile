FROM ubuntu:18.04
RUN mkdir /code
WORKDIR /code

ADD . /code

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-setuptools
RUN apt-get install -y build-essential cmake
RUN apt-get install -y libopenblas-dev liblapack-dev
RUN apt-get install -y libx11-dev libgtk-3-dev

ADD ./requirements.txt ./
RUN pip3 install -r requirements.txt
RUN chmod -R +x /code/
CMD ["./run.sh"]




