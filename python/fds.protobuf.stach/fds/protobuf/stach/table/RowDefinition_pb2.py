# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fds/protobuf/stach/table/RowDefinition.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fds.protobuf.stach.table import DataFormat_pb2 as fds_dot_protobuf_dot_stach_dot_table_dot_DataFormat__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fds/protobuf/stach/table/RowDefinition.proto',
  package='factset.protobuf.stach.table',
  syntax='proto3',
  serialized_options=b'\n com.factset.protobuf.stach.tableB\022RowDefinitionProtoZ=github.com/factset/stachschema/go/v2/fds/protobuf/stach/table\252\002\034FactSet.Protobuf.Stach.Table',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,fds/protobuf/stach/table/RowDefinition.proto\x12\x1c\x66\x61\x63tset.protobuf.stach.table\x1a)fds/protobuf/stach/table/DataFormat.proto\"U\n\rRowDefinition\x12\n\n\x02id\x18\x01 \x01(\t\x12\x38\n\x06\x66ormat\x18\x02 \x01(\x0b\x32(.factset.protobuf.stach.table.DataFormatB\x94\x01\n com.factset.protobuf.stach.tableB\x12RowDefinitionProtoZ=github.com/factset/stachschema/go/v2/fds/protobuf/stach/table\xaa\x02\x1c\x46\x61\x63tSet.Protobuf.Stach.Tableb\x06proto3'
  ,
  dependencies=[fds_dot_protobuf_dot_stach_dot_table_dot_DataFormat__pb2.DESCRIPTOR,])




_ROWDEFINITION = _descriptor.Descriptor(
  name='RowDefinition',
  full_name='factset.protobuf.stach.table.RowDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='factset.protobuf.stach.table.RowDefinition.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='factset.protobuf.stach.table.RowDefinition.format', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=121,
  serialized_end=206,
)

_ROWDEFINITION.fields_by_name['format'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_DataFormat__pb2._DATAFORMAT
DESCRIPTOR.message_types_by_name['RowDefinition'] = _ROWDEFINITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RowDefinition = _reflection.GeneratedProtocolMessageType('RowDefinition', (_message.Message,), {
  'DESCRIPTOR' : _ROWDEFINITION,
  '__module__' : 'fds.protobuf.stach.table.RowDefinition_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.RowDefinition)
  })
_sym_db.RegisterMessage(RowDefinition)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
