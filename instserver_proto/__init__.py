"""instserver-proto: gRPC proto stubs for InstServer ↔ LabMaster4 communication."""

from importlib.metadata import version as _pkg_version

# Read from the installed distribution's metadata (set from pyproject.toml's [project]
# version at build time) instead of a second hardcoded string -- a duplicated literal
# here is exactly the bug that let InstServer_grpc's setup.py/setup_wheel.py versions
# drift apart (see instserver-grpc-package-build task).
__version__ = _pkg_version("instserver-proto")

from .instserver_pb2 import *  # noqa: F401,F403
from . import instserver_pb2 as pb2
from . import instserver_pb2_grpc as pb2_grpc

__all__ = ["__version__", "pb2", "pb2_grpc"]
