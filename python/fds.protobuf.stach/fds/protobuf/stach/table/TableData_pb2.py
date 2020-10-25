# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fds/protobuf/stach/table/TableData.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fds.protobuf.stach.table import ColumnData_pb2 as fds_dot_protobuf_dot_stach_dot_table_dot_ColumnData__pb2
from fds.protobuf.stach.table import MetadataCollection_pb2 as fds_dot_protobuf_dot_stach_dot_table_dot_MetadataCollection__pb2
from fds.protobuf.stach.table import RowDefinition_pb2 as fds_dot_protobuf_dot_stach_dot_table_dot_RowDefinition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fds/protobuf/stach/table/TableData.proto',
  package='factset.protobuf.stach.table',
  syntax='proto3',
  serialized_options=b'\n com.factset.protobuf.stach.tableB\016TableDataProtoZ=github.com/factset/stachschema/go/v2/fds/protobuf/stach/table\252\002\034FactSet.Protobuf.Stach.Table',
  serialized_pb=b'\n(fds/protobuf/stach/table/TableData.proto\x12\x1c\x66\x61\x63tset.protobuf.stach.table\x1a)fds/protobuf/stach/table/ColumnData.proto\x1a\x31\x66\x64s/protobuf/stach/table/MetadataCollection.proto\x1a,fds/protobuf/stach/table/RowDefinition.proto\"\xab\x02\n\tTableData\x12\x39\n\x04rows\x18\x01 \x03(\x0b\x32+.factset.protobuf.stach.table.RowDefinition\x12\x45\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x34.factset.protobuf.stach.table.TableData.ColumnsEntry\x12\x42\n\x08metadata\x18\x03 \x01(\x0b\x32\x30.factset.protobuf.stach.table.MetadataCollection\x1aX\n\x0c\x43olumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.factset.protobuf.stach.table.ColumnData:\x02\x38\x01\x42\x90\x01\n com.factset.protobuf.stach.tableB\x0eTableDataProtoZ=github.com/factset/stachschema/go/v2/fds/protobuf/stach/table\xaa\x02\x1c\x46\x61\x63tSet.Protobuf.Stach.Tableb\x06proto3'
  ,
  dependencies=[fds_dot_protobuf_dot_stach_dot_table_dot_ColumnData__pb2.DESCRIPTOR,fds_dot_protobuf_dot_stach_dot_table_dot_MetadataCollection__pb2.DESCRIPTOR,fds_dot_protobuf_dot_stach_dot_table_dot_RowDefinition__pb2.DESCRIPTOR,])




_TABLEDATA_COLUMNSENTRY = _descriptor.Descriptor(
  name='ColumnsEntry',
  full_name='factset.protobuf.stach.table.TableData.ColumnsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='factset.protobuf.stach.table.TableData.ColumnsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='factset.protobuf.stach.table.TableData.ColumnsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=514,
)

_TABLEDATA = _descriptor.Descriptor(
  name='TableData',
  full_name='factset.protobuf.stach.table.TableData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='factset.protobuf.stach.table.TableData.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='factset.protobuf.stach.table.TableData.columns', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='factset.protobuf.stach.table.TableData.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TABLEDATA_COLUMNSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=514,
)

_TABLEDATA_COLUMNSENTRY.fields_by_name['value'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_ColumnData__pb2._COLUMNDATA
_TABLEDATA_COLUMNSENTRY.containing_type = _TABLEDATA
_TABLEDATA.fields_by_name['rows'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_RowDefinition__pb2._ROWDEFINITION
_TABLEDATA.fields_by_name['columns'].message_type = _TABLEDATA_COLUMNSENTRY
_TABLEDATA.fields_by_name['metadata'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_MetadataCollection__pb2._METADATACOLLECTION
DESCRIPTOR.message_types_by_name['TableData'] = _TABLEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TableData = _reflection.GeneratedProtocolMessageType('TableData', (_message.Message,), {

  'ColumnsEntry' : _reflection.GeneratedProtocolMessageType('ColumnsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TABLEDATA_COLUMNSENTRY,
    '__module__' : 'fds.protobuf.stach.table.TableData_pb2'
    # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.TableData.ColumnsEntry)
    })
  ,
  'DESCRIPTOR' : _TABLEDATA,
  '__module__' : 'fds.protobuf.stach.table.TableData_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.TableData)
  })
_sym_db.RegisterMessage(TableData)
_sym_db.RegisterMessage(TableData.ColumnsEntry)


DESCRIPTOR._options = None
_TABLEDATA_COLUMNSENTRY._options = None
# @@protoc_insertion_point(module_scope)
