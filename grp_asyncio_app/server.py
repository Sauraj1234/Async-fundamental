import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))


import grpc 
import asyncio
from grp_asyncio_app.protofiles import user_pb2_grpc
from grp_asyncio_app.core.async_db import init_db
from grp_asyncio_app.services.user_service import UserService

    
async def serve():
    bind_addr = "[::]:50051"
    server = grpc.aio.server()    
    await init_db()
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(),server=server)
    server.add_insecure_port(bind_addr)
    await server.start()
    print("gRPC server started on", bind_addr)
    await server.wait_for_termination()
    

if __name__ == '__main__':
    asyncio.run(serve())

