# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/TiraHostMessages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/TiraHostMessages.proto',
  package='tira.generated',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1asrc/TiraHostMessages.proto\x12\x0etira.generated\"\x15\n\x05Input\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x16\n\x06Output\x12\x0c\n\x04text\x18\x01 \x01(\t\"\xca\x01\n\x07Request\x12\x0e\n\x06vmName\x18\x01 \x01(\t\x12\x0f\n\x07ovaFile\x18\x02 \x01(\t\x12\x10\n\x08userName\x18\x03 \x01(\t\x12\x16\n\x0esubmissionFile\x18\x04 \x01(\t\x12\x18\n\x10inputDatasetName\x18\x05 \x01(\t\x12\x14\n\x0cinputRunPath\x18\x06 \x01(\t\x12\x15\n\routputDirName\x18\x07 \x01(\t\x12\x11\n\tsandboxed\x18\x08 \x01(\t\x12\x1a\n\x12optionalParameters\x18\t \x01(\t\"\x1a\n\x08Response\x12\x0e\n\x06output\x18\x01 \x01(\t2\xa9\x07\n\x0fTiraHostService\x12\x37\n\x04test\x12\x15.tira.generated.Input\x1a\x16.tira.generated.Output\"\x00\x12\x42\n\rshell_command\x12\x17.tira.generated.Request\x1a\x16.tira.generated.Output\"\x00\x12@\n\tvm_backup\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12@\n\tvm_create\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12@\n\tvm_delete\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12>\n\x07vm_info\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12>\n\x07vm_list\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12\x41\n\nvm_sandbox\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12\x42\n\x0bvm_shutdown\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12\x42\n\x0bvm_snapshot\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12?\n\x08vm_start\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12>\n\x07vm_stop\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12\x43\n\x0cvm_unsandbox\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x12\x42\n\x0brun_execute\x12\x17.tira.generated.Request\x1a\x18.tira.generated.Response\"\x00\x62\x06proto3'
)




_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='tira.generated.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='tira.generated.Input.text', index=0,
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
  serialized_start=46,
  serialized_end=67,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='tira.generated.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='tira.generated.Output.text', index=0,
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
  serialized_start=69,
  serialized_end=91,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='tira.generated.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vmName', full_name='tira.generated.Request.vmName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ovaFile', full_name='tira.generated.Request.ovaFile', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userName', full_name='tira.generated.Request.userName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submissionFile', full_name='tira.generated.Request.submissionFile', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputDatasetName', full_name='tira.generated.Request.inputDatasetName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputRunPath', full_name='tira.generated.Request.inputRunPath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputDirName', full_name='tira.generated.Request.outputDirName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sandboxed', full_name='tira.generated.Request.sandboxed', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optionalParameters', full_name='tira.generated.Request.optionalParameters', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=94,
  serialized_end=296,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='tira.generated.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='tira.generated.Response.output', index=0,
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
  serialized_start=298,
  serialized_end=324,
)

DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'src.TiraHostMessages_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.Input)
  })
_sym_db.RegisterMessage(Input)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'src.TiraHostMessages_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.Output)
  })
_sym_db.RegisterMessage(Output)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'src.TiraHostMessages_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'src.TiraHostMessages_pb2'
  # @@protoc_insertion_point(class_scope:tira.generated.Response)
  })
_sym_db.RegisterMessage(Response)



_TIRAHOSTSERVICE = _descriptor.ServiceDescriptor(
  name='TiraHostService',
  full_name='tira.generated.TiraHostService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=327,
  serialized_end=1264,
  methods=[
  _descriptor.MethodDescriptor(
    name='test',
    full_name='tira.generated.TiraHostService.test',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='shell_command',
    full_name='tira.generated.TiraHostService.shell_command',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_backup',
    full_name='tira.generated.TiraHostService.vm_backup',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_create',
    full_name='tira.generated.TiraHostService.vm_create',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_delete',
    full_name='tira.generated.TiraHostService.vm_delete',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_info',
    full_name='tira.generated.TiraHostService.vm_info',
    index=5,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_list',
    full_name='tira.generated.TiraHostService.vm_list',
    index=6,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_sandbox',
    full_name='tira.generated.TiraHostService.vm_sandbox',
    index=7,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_shutdown',
    full_name='tira.generated.TiraHostService.vm_shutdown',
    index=8,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_snapshot',
    full_name='tira.generated.TiraHostService.vm_snapshot',
    index=9,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_start',
    full_name='tira.generated.TiraHostService.vm_start',
    index=10,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_stop',
    full_name='tira.generated.TiraHostService.vm_stop',
    index=11,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='vm_unsandbox',
    full_name='tira.generated.TiraHostService.vm_unsandbox',
    index=12,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='run_execute',
    full_name='tira.generated.TiraHostService.run_execute',
    index=13,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIRAHOSTSERVICE)

DESCRIPTOR.services_by_name['TiraHostService'] = _TIRAHOSTSERVICE

# @@protoc_insertion_point(module_scope)
