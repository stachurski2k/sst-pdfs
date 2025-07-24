import grpc_api.schemas.messages_pb2_grpc as messages_pb2_grpc
from .greeter_controller import GreeterController
from .templates_controller import GetAllTemplatesController
from dependencies import *

def register_controllers(server):
    messages_pb2_grpc.add_GreeterServicer_to_server(GreeterController(), server)
    messages_pb2_grpc.add_AllTemplatesServiceServicer_to_server(GetAllTemplatesController(get_logger(),get_templates_service()), server)