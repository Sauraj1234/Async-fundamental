# grpcio_async_app

An **async gRPC service built with Python**, showcasing **high-concurrency request handling** using `grpc.aio` and **async SQLAlchemy** with PostgreSQL.  
This project demonstrates **production-grade async patterns**, database connection pooling, and correct concurrent client/server behavior — suitable for backend, platform, and distributed systems roles.

---

## Key Highlights

- 🚀 **Fully asynchronous gRPC server** (`grpc.aio`)
- 🧵 **True concurrent RPC handling** using `asyncio`
- 🗄️ **Async SQLAlchemy + asyncpg** with tuned connection pooling
- 🧩 Clean **service / DB session separation**
- ⚙️ Demonstrates **correct async client concurrency** (`asyncio.gather`)
- 🧪 Easy to extend for load testing and benchmarking

---

## Tech Stack

- **Python 3.10+**
- **grpcio / grpcio-tools**
- **asyncio**
- **SQLAlchemy (async)**
- **PostgreSQL**
- **asyncpg**

---

## Project Structure


grpcio_async_app/
├── server.py          # Async gRPC server
├── client.py          # Concurrent async gRPC client
├── user.proto         # Protobuf definitions
├── user_pb2.py
├── user_pb2_grpc.py
├── README.md



---

## Architecture Overview

Async gRPC Client
│
│ (concurrent RPC calls)
▼
Async gRPC Server (grpc.aio)
│
│ (async DB sessions)
▼
PostgreSQL (asyncpg pool)



- Each RPC runs as an **independent asyncio Task**
- Each request gets a **dedicated async DB session**
- Database concurrency controlled via connection pool

---

## Database Model

```python
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "meta"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
```
## Setup Instructions

Follow the steps below to set up and run the **grpcio_async_app** locally.

---

### Prerequisites

- Python **3.10 or higher**
- PostgreSQL **13+**
- `pip` (or any Python package manager)
- Git

Verify installations:
```bash
python --version
psql --version


