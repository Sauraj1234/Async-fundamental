import grpc 
import asyncio
import user_pb2_grpc
from grp_asyncio_app.core.async_db import init_db
from grp_asyncio_app.services.user_service import UserServiceServicer

    
async def serve():
    bind_addr = "[::]:50051"
    server = grpc.aio.server()    
    init_db()
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(),server=server)
    server.add_insecure_port(bind_addr)
    await server.start()
    print("gRPC server started on", bind_addr)
    await server.wait_for_termination()
    

if __name__ == '__main__':
    asyncio.run(serve())

