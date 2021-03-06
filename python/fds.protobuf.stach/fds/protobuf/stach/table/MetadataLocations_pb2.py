# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fds/protobuf/stach/table/MetadataLocations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fds.protobuf.stach.table import ListOfMetadata_pb2 as fds_dot_protobuf_dot_stach_dot_table_dot_ListOfMetadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fds/protobuf/stach/table/MetadataLocations.proto',
  package='factset.protobuf.stach.table',
  syntax='proto3',
  serialized_options=b'\n com.factset.protobuf.stach.tableB\026MetadataLocationsProtoZ=github.com/factset/stachschema/go/v2/fds/protobuf/stach/table\252\002\034FactSet.Protobuf.Stach.Table',
  serialized_pb=b'\n0fds/protobuf/stach/table/MetadataLocations.proto\x12\x1c\x66\x61\x63tset.protobuf.stach.table\x1a-fds/protobuf/stach/table/ListOfMetadata.proto\"\xe0\x06\n\x11MetadataLocations\x12\r\n\x05table\x18\x01 \x03(\t\x12M\n\x07\x63olumns\x18\x02 \x03(\x0b\x32<.factset.protobuf.stach.table.MetadataLocations.ColumnsEntry\x12G\n\x04rows\x18\x03 \x03(\x0b\x32\x39.factset.protobuf.stach.table.MetadataLocations.RowsEntry\x12M\n\x05\x63\x65lls\x18\x04 \x01(\x0b\x32>.factset.protobuf.stach.table.MetadataLocations.CellsColumnMap\x1a\xdb\x01\n\x0e\x43\x65llsColumnMap\x12\\\n\x07\x63olumns\x18\x01 \x03(\x0b\x32K.factset.protobuf.stach.table.MetadataLocations.CellsColumnMap.ColumnsEntry\x1ak\n\x0c\x43olumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b\x32;.factset.protobuf.stach.table.MetadataLocations.CellsRowMap:\x02\x38\x01\x1a\xbd\x01\n\x0b\x43\x65llsRowMap\x12S\n\x04rows\x18\x01 \x03(\x0b\x32\x45.factset.protobuf.stach.table.MetadataLocations.CellsRowMap.RowsEntry\x1aY\n\tRowsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.factset.protobuf.stach.table.ListOfMetadata:\x02\x38\x01\x1a\\\n\x0c\x43olumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.factset.protobuf.stach.table.ListOfMetadata:\x02\x38\x01\x1aY\n\tRowsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.factset.protobuf.stach.table.ListOfMetadata:\x02\x38\x01\x42\x98\x01\n com.factset.protobuf.stach.tableB\x16MetadataLocationsProtoZ=github.com/factset/stachschema/go/v2/fds/protobuf/stach/table\xaa\x02\x1c\x46\x61\x63tSet.Protobuf.Stach.Tableb\x06proto3'
  ,
  dependencies=[fds_dot_protobuf_dot_stach_dot_table_dot_ListOfMetadata__pb2.DESCRIPTOR,])




_METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY = _descriptor.Descriptor(
  name='ColumnsEntry',
  full_name='factset.protobuf.stach.table.MetadataLocations.CellsColumnMap.ColumnsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='factset.protobuf.stach.table.MetadataLocations.CellsColumnMap.ColumnsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='factset.protobuf.stach.table.MetadataLocations.CellsColumnMap.ColumnsEntry.value', index=1,
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
  serialized_start=510,
  serialized_end=617,
)

_METADATALOCATIONS_CELLSCOLUMNMAP = _descriptor.Descriptor(
  name='CellsColumnMap',
  full_name='factset.protobuf.stach.table.MetadataLocations.CellsColumnMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='factset.protobuf.stach.table.MetadataLocations.CellsColumnMap.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=617,
)

_METADATALOCATIONS_CELLSROWMAP_ROWSENTRY = _descriptor.Descriptor(
  name='RowsEntry',
  full_name='factset.protobuf.stach.table.MetadataLocations.CellsRowMap.RowsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='factset.protobuf.stach.table.MetadataLocations.CellsRowMap.RowsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='factset.protobuf.stach.table.MetadataLocations.CellsRowMap.RowsEntry.value', index=1,
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
  serialized_start=720,
  serialized_end=809,
)

_METADATALOCATIONS_CELLSROWMAP = _descriptor.Descriptor(
  name='CellsRowMap',
  full_name='factset.protobuf.stach.table.MetadataLocations.CellsRowMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='factset.protobuf.stach.table.MetadataLocations.CellsRowMap.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METADATALOCATIONS_CELLSROWMAP_ROWSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=809,
)

_METADATALOCATIONS_COLUMNSENTRY = _descriptor.Descriptor(
  name='ColumnsEntry',
  full_name='factset.protobuf.stach.table.MetadataLocations.ColumnsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='factset.protobuf.stach.table.MetadataLocations.ColumnsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='factset.protobuf.stach.table.MetadataLocations.ColumnsEntry.value', index=1,
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
  serialized_start=811,
  serialized_end=903,
)

_METADATALOCATIONS_ROWSENTRY = _descriptor.Descriptor(
  name='RowsEntry',
  full_name='factset.protobuf.stach.table.MetadataLocations.RowsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='factset.protobuf.stach.table.MetadataLocations.RowsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='factset.protobuf.stach.table.MetadataLocations.RowsEntry.value', index=1,
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
  serialized_start=720,
  serialized_end=809,
)

_METADATALOCATIONS = _descriptor.Descriptor(
  name='MetadataLocations',
  full_name='factset.protobuf.stach.table.MetadataLocations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='factset.protobuf.stach.table.MetadataLocations.table', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='factset.protobuf.stach.table.MetadataLocations.columns', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='factset.protobuf.stach.table.MetadataLocations.rows', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cells', full_name='factset.protobuf.stach.table.MetadataLocations.cells', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METADATALOCATIONS_CELLSCOLUMNMAP, _METADATALOCATIONS_CELLSROWMAP, _METADATALOCATIONS_COLUMNSENTRY, _METADATALOCATIONS_ROWSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=994,
)

_METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY.fields_by_name['value'].message_type = _METADATALOCATIONS_CELLSROWMAP
_METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY.containing_type = _METADATALOCATIONS_CELLSCOLUMNMAP
_METADATALOCATIONS_CELLSCOLUMNMAP.fields_by_name['columns'].message_type = _METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY
_METADATALOCATIONS_CELLSCOLUMNMAP.containing_type = _METADATALOCATIONS
_METADATALOCATIONS_CELLSROWMAP_ROWSENTRY.fields_by_name['value'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_ListOfMetadata__pb2._LISTOFMETADATA
_METADATALOCATIONS_CELLSROWMAP_ROWSENTRY.containing_type = _METADATALOCATIONS_CELLSROWMAP
_METADATALOCATIONS_CELLSROWMAP.fields_by_name['rows'].message_type = _METADATALOCATIONS_CELLSROWMAP_ROWSENTRY
_METADATALOCATIONS_CELLSROWMAP.containing_type = _METADATALOCATIONS
_METADATALOCATIONS_COLUMNSENTRY.fields_by_name['value'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_ListOfMetadata__pb2._LISTOFMETADATA
_METADATALOCATIONS_COLUMNSENTRY.containing_type = _METADATALOCATIONS
_METADATALOCATIONS_ROWSENTRY.fields_by_name['value'].message_type = fds_dot_protobuf_dot_stach_dot_table_dot_ListOfMetadata__pb2._LISTOFMETADATA
_METADATALOCATIONS_ROWSENTRY.containing_type = _METADATALOCATIONS
_METADATALOCATIONS.fields_by_name['columns'].message_type = _METADATALOCATIONS_COLUMNSENTRY
_METADATALOCATIONS.fields_by_name['rows'].message_type = _METADATALOCATIONS_ROWSENTRY
_METADATALOCATIONS.fields_by_name['cells'].message_type = _METADATALOCATIONS_CELLSCOLUMNMAP
DESCRIPTOR.message_types_by_name['MetadataLocations'] = _METADATALOCATIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetadataLocations = _reflection.GeneratedProtocolMessageType('MetadataLocations', (_message.Message,), {

  'CellsColumnMap' : _reflection.GeneratedProtocolMessageType('CellsColumnMap', (_message.Message,), {

    'ColumnsEntry' : _reflection.GeneratedProtocolMessageType('ColumnsEntry', (_message.Message,), {
      'DESCRIPTOR' : _METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY,
      '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
      # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations.CellsColumnMap.ColumnsEntry)
      })
    ,
    'DESCRIPTOR' : _METADATALOCATIONS_CELLSCOLUMNMAP,
    '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
    # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations.CellsColumnMap)
    })
  ,

  'CellsRowMap' : _reflection.GeneratedProtocolMessageType('CellsRowMap', (_message.Message,), {

    'RowsEntry' : _reflection.GeneratedProtocolMessageType('RowsEntry', (_message.Message,), {
      'DESCRIPTOR' : _METADATALOCATIONS_CELLSROWMAP_ROWSENTRY,
      '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
      # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations.CellsRowMap.RowsEntry)
      })
    ,
    'DESCRIPTOR' : _METADATALOCATIONS_CELLSROWMAP,
    '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
    # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations.CellsRowMap)
    })
  ,

  'ColumnsEntry' : _reflection.GeneratedProtocolMessageType('ColumnsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATALOCATIONS_COLUMNSENTRY,
    '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
    # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations.ColumnsEntry)
    })
  ,

  'RowsEntry' : _reflection.GeneratedProtocolMessageType('RowsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATALOCATIONS_ROWSENTRY,
    '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
    # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations.RowsEntry)
    })
  ,
  'DESCRIPTOR' : _METADATALOCATIONS,
  '__module__' : 'fds.protobuf.stach.table.MetadataLocations_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.MetadataLocations)
  })
_sym_db.RegisterMessage(MetadataLocations)
_sym_db.RegisterMessage(MetadataLocations.CellsColumnMap)
_sym_db.RegisterMessage(MetadataLocations.CellsColumnMap.ColumnsEntry)
_sym_db.RegisterMessage(MetadataLocations.CellsRowMap)
_sym_db.RegisterMessage(MetadataLocations.CellsRowMap.RowsEntry)
_sym_db.RegisterMessage(MetadataLocations.ColumnsEntry)
_sym_db.RegisterMessage(MetadataLocations.RowsEntry)


DESCRIPTOR._options = None
_METADATALOCATIONS_CELLSCOLUMNMAP_COLUMNSENTRY._options = None
_METADATALOCATIONS_CELLSROWMAP_ROWSENTRY._options = None
_METADATALOCATIONS_COLUMNSENTRY._options = None
_METADATALOCATIONS_ROWSENTRY._options = None
# @@protoc_insertion_point(module_scope)
