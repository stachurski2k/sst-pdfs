import grpc
from concurrent import futures
from grpc_api.controllers.register_controllers import register_controllers

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    register_controllers(server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()