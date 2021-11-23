
import logging
import Task_pb2
import Task_pb2_grpc
import grpc
from concurrent import futures


class Greeter(Task_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return Task_pb2.HelloReply(message='Hello, %s!' % request.name)
    def SayHelloAgain(self, request, context):
        return Task_pb2.HelloReply(message='Hello again, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Task_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:9999')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
