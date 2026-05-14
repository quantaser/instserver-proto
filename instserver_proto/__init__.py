"""instserver-proto: gRPC proto stubs for InstServer ↔ LabMaster4 communication."""

__version__ = "0.1.0"

from .instserver_pb2 import *  # noqa: F401,F403
from . import instserver_pb2 as pb2
from . import instserver_pb2_grpc as pb2_grpc

__all__ = ["__version__", "pb2", "pb2_grpc"]
