
import grpc
from  grp_asyncio_app.protofiles import user_pb2 
from grp_asyncio_app.protofiles import user_pb2_grpc
from grp_asyncio_app.core.async_db import AsyncSessionLocal
from grp_asyncio_app.models.user import User


class UserService(user_pb2_grpc.UserServiceServicer):
    
    async def AddUser(self, request,context):
        try:
            user_id = await self.add_user(name=request.name)
            return user_pb2.UserResponse(id=user_id, 
                                         name=request.name)
        except Exception as error:
            await context.abort(grpc.StatusCode.INTERNAL, str(error)) 


    async def add_user(self,name: str) -> int:
        """Insert a user and return inserted id."""
        async with AsyncSessionLocal() as session:
            async with session.begin():  
                user = User(name=name)
                session.add(user)
            
            return user.id    
