FROM ubuntu:16.04
WORKDIR /root
ADD . /Task
RUN apt-get update
RUN apt-get install python3 python3-pip -y 
RUN apt-get pip install -r /requirements.txt
ENTRYPOINT ["python", "greeter_server.py"]
