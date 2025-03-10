# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bentoml/grpc/v1/service_test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bentoml/grpc/v1/service_test.proto',
  package='bentoml.testing.v1',
  syntax='proto3',
  serialized_options=b'H\001Z\035github.com/bentoml/testing/v1\220\001\001\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"bentoml/grpc/v1/service_test.proto\x12\x12\x62\x65ntoml.testing.v1\"\x1f\n\x0e\x45xecuteRequest\x12\r\n\x05input\x18\x01 \x01(\t\"!\n\x0f\x45xecuteResponse\x12\x0e\n\x06output\x18\x01 \x01(\t2a\n\x0bTestService\x12R\n\x07\x45xecute\x12\".bentoml.testing.v1.ExecuteRequest\x1a#.bentoml.testing.v1.ExecuteResponseB\'H\x01Z\x1dgithub.com/bentoml/testing/v1\x90\x01\x01\xf8\x01\x01\x62\x06proto3'
)




_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='bentoml.testing.v1.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='bentoml.testing.v1.ExecuteRequest.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=89,
)


_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='bentoml.testing.v1.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='bentoml.testing.v1.ExecuteResponse.output', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=124,
)

DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'bentoml.grpc.v1.service_test_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.testing.v1.ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTERESPONSE,
  '__module__' : 'bentoml.grpc.v1.service_test_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.testing.v1.ExecuteResponse)
  })
_sym_db.RegisterMessage(ExecuteResponse)


DESCRIPTOR._options = None

_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='bentoml.testing.v1.TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=126,
  serialized_end=223,
  methods=[
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='bentoml.testing.v1.TestService.Execute',
    index=0,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_EXECUTERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

TestService = service_reflection.GeneratedServiceType('TestService', (_service.Service,), dict(
  DESCRIPTOR = _TESTSERVICE,
  __module__ = 'bentoml.grpc.v1.service_test_pb2'
  ))

TestService_Stub = service_reflection.GeneratedServiceStubType('TestService_Stub', (TestService,), dict(
  DESCRIPTOR = _TESTSERVICE,
  __module__ = 'bentoml.grpc.v1.service_test_pb2'
  ))


# @@protoc_insertion_point(module_scope)
