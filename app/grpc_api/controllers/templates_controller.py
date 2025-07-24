import grpc_api.schemas.messages_pb2 as messages_pb2
import grpc_api.schemas.messages_pb2_grpc as messages_pb2_grpc

class GetAllTemplatesController(messages_pb2_grpc.AllTemplatesService):

    def __init__(self,log,templates_service):
        self.log=log
        self.templates=templates_service

    def GetAllTemplates(self, request, context):
        
        return messages_pb2.AllTemplatesReply(
            names = self.templates.get_all_templates()
        )