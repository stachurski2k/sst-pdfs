import grpc_api.schemas.messages_pb2 as messages_pb2
import grpc_api.schemas.messages_pb2_grpc as messages_pb2_grpc

class GreeterController(messages_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        
        return messages_pb2.HelloReply(message=f'Hello, {request.name}!')