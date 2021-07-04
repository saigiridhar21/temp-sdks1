// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.25.0-devel
// 	protoc        v3.12.3
// source: fds/protobuf/stach/table/TableDefinition.proto

package table

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// A table definition
type TableDefinition struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The id of the headers table
	HeaderTableId string `protobuf:"bytes,1,opt,name=header_table_id,json=headerTableId,proto3" json:"header_table_id,omitempty"`
	// The array of column definitions
	Columns []*ColumnDefinition `protobuf:"bytes,2,rep,name=columns,proto3" json:"columns,omitempty"`
}

func (x *TableDefinition) Reset() {
	*x = TableDefinition{}
	if protoimpl.UnsafeEnabled {
		mi := &file_fds_protobuf_stach_table_TableDefinition_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TableDefinition) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TableDefinition) ProtoMessage() {}

func (x *TableDefinition) ProtoReflect() protoreflect.Message {
	mi := &file_fds_protobuf_stach_table_TableDefinition_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TableDefinition.ProtoReflect.Descriptor instead.
func (*TableDefinition) Descriptor() ([]byte, []int) {
	return file_fds_protobuf_stach_table_TableDefinition_proto_rawDescGZIP(), []int{0}
}

func (x *TableDefinition) GetHeaderTableId() string {
	if x != nil {
		return x.HeaderTableId
	}
	return ""
}

func (x *TableDefinition) GetColumns() []*ColumnDefinition {
	if x != nil {
		return x.Columns
	}
	return nil
}

var File_fds_protobuf_stach_table_TableDefinition_proto protoreflect.FileDescriptor

var file_fds_protobuf_stach_table_TableDefinition_proto_rawDesc = []byte{
	0x0a, 0x2e, 0x66, 0x64, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73,
	0x74, 0x61, 0x63, 0x68, 0x2f, 0x74, 0x61, 0x62, 0x6c, 0x65, 0x2f, 0x54, 0x61, 0x62, 0x6c, 0x65,
	0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x1c, 0x66, 0x61, 0x63, 0x74, 0x73, 0x65, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x73, 0x74, 0x61, 0x63, 0x68, 0x2e, 0x74, 0x61, 0x62, 0x6c, 0x65, 0x1a, 0x2f,
	0x66, 0x64, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x61,
	0x63, 0x68, 0x2f, 0x74, 0x61, 0x62, 0x6c, 0x65, 0x2f, 0x43, 0x6f, 0x6c, 0x75, 0x6d, 0x6e, 0x44,
	0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22,
	0x83, 0x01, 0x0a, 0x0f, 0x54, 0x61, 0x62, 0x6c, 0x65, 0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74,
	0x69, 0x6f, 0x6e, 0x12, 0x26, 0x0a, 0x0f, 0x68, 0x65, 0x61, 0x64, 0x65, 0x72, 0x5f, 0x74, 0x61,
	0x62, 0x6c, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x68, 0x65,
	0x61, 0x64, 0x65, 0x72, 0x54, 0x61, 0x62, 0x6c, 0x65, 0x49, 0x64, 0x12, 0x48, 0x0a, 0x07, 0x63,
	0x6f, 0x6c, 0x75, 0x6d, 0x6e, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2e, 0x2e, 0x66,
	0x61, 0x63, 0x74, 0x73, 0x65, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e,
	0x73, 0x74, 0x61, 0x63, 0x68, 0x2e, 0x74, 0x61, 0x62, 0x6c, 0x65, 0x2e, 0x43, 0x6f, 0x6c, 0x75,
	0x6d, 0x6e, 0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x07, 0x63, 0x6f,
	0x6c, 0x75, 0x6d, 0x6e, 0x73, 0x42, 0x96, 0x01, 0x0a, 0x20, 0x63, 0x6f, 0x6d, 0x2e, 0x66, 0x61,
	0x63, 0x74, 0x73, 0x65, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x73,
	0x74, 0x61, 0x63, 0x68, 0x2e, 0x74, 0x61, 0x62, 0x6c, 0x65, 0x42, 0x14, 0x54, 0x61, 0x62, 0x6c,
	0x65, 0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x50, 0x72, 0x6f, 0x74, 0x6f,
	0x5a, 0x3d, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x66, 0x61, 0x63,
	0x74, 0x73, 0x65, 0x74, 0x2f, 0x73, 0x74, 0x61, 0x63, 0x68, 0x73, 0x63, 0x68, 0x65, 0x6d, 0x61,
	0x2f, 0x67, 0x6f, 0x2f, 0x76, 0x32, 0x2f, 0x66, 0x64, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x61, 0x63, 0x68, 0x2f, 0x74, 0x61, 0x62, 0x6c, 0x65, 0xaa,
	0x02, 0x1c, 0x46, 0x61, 0x63, 0x74, 0x53, 0x65, 0x74, 0x2e, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x53, 0x74, 0x61, 0x63, 0x68, 0x2e, 0x54, 0x61, 0x62, 0x6c, 0x65, 0x62, 0x06,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_fds_protobuf_stach_table_TableDefinition_proto_rawDescOnce sync.Once
	file_fds_protobuf_stach_table_TableDefinition_proto_rawDescData = file_fds_protobuf_stach_table_TableDefinition_proto_rawDesc
)

func file_fds_protobuf_stach_table_TableDefinition_proto_rawDescGZIP() []byte {
	file_fds_protobuf_stach_table_TableDefinition_proto_rawDescOnce.Do(func() {
		file_fds_protobuf_stach_table_TableDefinition_proto_rawDescData = protoimpl.X.CompressGZIP(file_fds_protobuf_stach_table_TableDefinition_proto_rawDescData)
	})
	return file_fds_protobuf_stach_table_TableDefinition_proto_rawDescData
}

var file_fds_protobuf_stach_table_TableDefinition_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_fds_protobuf_stach_table_TableDefinition_proto_goTypes = []interface{}{
	(*TableDefinition)(nil),  // 0: factset.protobuf.stach.table.TableDefinition
	(*ColumnDefinition)(nil), // 1: factset.protobuf.stach.table.ColumnDefinition
}
var file_fds_protobuf_stach_table_TableDefinition_proto_depIdxs = []int32{
	1, // 0: factset.protobuf.stach.table.TableDefinition.columns:type_name -> factset.protobuf.stach.table.ColumnDefinition
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_fds_protobuf_stach_table_TableDefinition_proto_init() }
func file_fds_protobuf_stach_table_TableDefinition_proto_init() {
	if File_fds_protobuf_stach_table_TableDefinition_proto != nil {
		return
	}
	file_fds_protobuf_stach_table_ColumnDefinition_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_fds_protobuf_stach_table_TableDefinition_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TableDefinition); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_fds_protobuf_stach_table_TableDefinition_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_fds_protobuf_stach_table_TableDefinition_proto_goTypes,
		DependencyIndexes: file_fds_protobuf_stach_table_TableDefinition_proto_depIdxs,
		MessageInfos:      file_fds_protobuf_stach_table_TableDefinition_proto_msgTypes,
	}.Build()
	File_fds_protobuf_stach_table_TableDefinition_proto = out.File
	file_fds_protobuf_stach_table_TableDefinition_proto_rawDesc = nil
	file_fds_protobuf_stach_table_TableDefinition_proto_goTypes = nil
	file_fds_protobuf_stach_table_TableDefinition_proto_depIdxs = nil
}
