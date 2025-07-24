from rest.entry_point import run as run_http
from grpc_api.entry_point import run as run_grpc


if __name__ == "__main__":
    run_grpc()
    #run_http()