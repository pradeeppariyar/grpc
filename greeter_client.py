import logging
import grpc
import Task_pb2
import Task_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:9999')
    stub = Task_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(Task_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(Task_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()