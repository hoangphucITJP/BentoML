"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import bentoml.grpc.v1.service_test_pb2
import grpc

class TestServiceStub:
    """Use for testing interceptors per RPC call."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Execute: grpc.UnaryUnaryMultiCallable[
        bentoml.grpc.v1.service_test_pb2.ExecuteRequest,
        bentoml.grpc.v1.service_test_pb2.ExecuteResponse,
    ]
    """Unary API"""

class TestServiceServicer(metaclass=abc.ABCMeta):
    """Use for testing interceptors per RPC call."""

    @abc.abstractmethod
    def Execute(
        self,
        request: bentoml.grpc.v1.service_test_pb2.ExecuteRequest,
        context: grpc.ServicerContext,
    ) -> bentoml.grpc.v1.service_test_pb2.ExecuteResponse:
        """Unary API"""

def add_TestServiceServicer_to_server(servicer: TestServiceServicer, server: grpc.Server) -> None: ...
