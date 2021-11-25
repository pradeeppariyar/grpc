

GRPC: gRPC is a modern open-source high performance Remote Procedure Call (RPC) framework that can run in any environment. 


Grpc details: For completion of given task, I have chosen the python as a programming language and followed the below steps:

•	 Create python environment by: python3 -m venv myenv (name user preference)
•	Source /bin/activate -> command for activate virtual environment
•	Need to install grpc package into machine as per requirement. (Strongly recommend that to follow the official document)
•	For more information follow the grpc official page: https://grpc.io/docs/languages/python/quickstart/
•	verify by command: pip list (show the list of packages inside the virtual environment)
•	need to install grpc tools from command prompt
•	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. Hello.proto (generate the grpc files for services which contain the all information of. proto method)
•	Task_pb2.py, Task_pb2_grpc.py}:
•	Tree -T (check the list of files)



Create server file using python:
Import the inheritance method from different _pb2.py and pb2_grpc.py proto generated file folder into server which contain the proto file method including Listening port for accept the request and return back to the requester like client.

Client file using python:

This file send the request and provoke the method inside the server also mapping the portnumber of client once verified that, then response the message.





Docker side: Dockerfile

This is the docker file which pull the images from docker hub and make container with Ubuntu OS for deployment.

Build Image command: Docker build .

FROM ubuntu:16.04
WORKDIR /root
ADD . /Task
RUN apt-get update
RUN apt-get install python3 python3-pip -y 
RUN apt-get pip install -r /requirements.txt
ENTRYPOINT ["python", "greeter_server.py"]



Compose file: To bind our local files to our container files and execute the program. all the program are configure into .yaml file.

This is the command for run .yaml file : docker compose up

 
Problem: 

The challenges which I have faced during the implementation is keep the track records of configured version into .Txt files. For that I must focused on some more advance research materials.
![image](https://user-images.githubusercontent.com/46217896/143418041-cf2de516-ae37-477f-905a-086df80f8cb7.png)
