// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: fds/protobuf/stach/table/VerticalAlignment.proto

package com.factset.protobuf.stach.table;

public final class VerticalAlignmentProto {
  private VerticalAlignmentProto() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  /**
   * <pre>
   * A vertical alignment
   * </pre>
   *
   * Protobuf enum {@code factset.protobuf.stach.table.VerticalAlignment}
   */
  public enum VerticalAlignment
      implements com.google.protobuf.ProtocolMessageEnum {
    /**
     * <pre>
     * This value should never be used, but exists to ensure that a value is specified
     * </pre>
     *
     * <code>UNKNOWN_VALIGN = 0;</code>
     */
    UNKNOWN_VALIGN(0),
    /**
     * <pre>
     * Value is vertically aligned to the top of the cell
     * </pre>
     *
     * <code>TOP = 1;</code>
     */
    TOP(1),
    /**
     * <pre>
     * Value is vertically aligned to the middle of the cell
     * </pre>
     *
     * <code>MIDDLE = 2;</code>
     */
    MIDDLE(2),
    /**
     * <pre>
     * Value is vertically aligned to the bottom of the cell
     * </pre>
     *
     * <code>BOTTOM = 3;</code>
     */
    BOTTOM(3),
    UNRECOGNIZED(-1),
    ;

    /**
     * <pre>
     * This value should never be used, but exists to ensure that a value is specified
     * </pre>
     *
     * <code>UNKNOWN_VALIGN = 0;</code>
     */
    public static final int UNKNOWN_VALIGN_VALUE = 0;
    /**
     * <pre>
     * Value is vertically aligned to the top of the cell
     * </pre>
     *
     * <code>TOP = 1;</code>
     */
    public static final int TOP_VALUE = 1;
    /**
     * <pre>
     * Value is vertically aligned to the middle of the cell
     * </pre>
     *
     * <code>MIDDLE = 2;</code>
     */
    public static final int MIDDLE_VALUE = 2;
    /**
     * <pre>
     * Value is vertically aligned to the bottom of the cell
     * </pre>
     *
     * <code>BOTTOM = 3;</code>
     */
    public static final int BOTTOM_VALUE = 3;


    public final int getNumber() {
      if (this == UNRECOGNIZED) {
        throw new java.lang.IllegalArgumentException(
            "Can't get the number of an unknown enum value.");
      }
      return value;
    }

    /**
     * @param value The numeric wire value of the corresponding enum entry.
     * @return The enum associated with the given numeric wire value.
     * @deprecated Use {@link #forNumber(int)} instead.
     */
    @java.lang.Deprecated
    public static VerticalAlignment valueOf(int value) {
      return forNumber(value);
    }

    /**
     * @param value The numeric wire value of the corresponding enum entry.
     * @return The enum associated with the given numeric wire value.
     */
    public static VerticalAlignment forNumber(int value) {
      switch (value) {
        case 0: return UNKNOWN_VALIGN;
        case 1: return TOP;
        case 2: return MIDDLE;
        case 3: return BOTTOM;
        default: return null;
      }
    }

    public static com.google.protobuf.Internal.EnumLiteMap<VerticalAlignment>
        internalGetValueMap() {
      return internalValueMap;
    }
    private static final com.google.protobuf.Internal.EnumLiteMap<
        VerticalAlignment> internalValueMap =
          new com.google.protobuf.Internal.EnumLiteMap<VerticalAlignment>() {
            public VerticalAlignment findValueByNumber(int number) {
              return VerticalAlignment.forNumber(number);
            }
          };

    public final com.google.protobuf.Descriptors.EnumValueDescriptor
        getValueDescriptor() {
      if (this == UNRECOGNIZED) {
        throw new java.lang.IllegalStateException(
            "Can't get the descriptor of an unrecognized enum value.");
      }
      return getDescriptor().getValues().get(ordinal());
    }
    public final com.google.protobuf.Descriptors.EnumDescriptor
        getDescriptorForType() {
      return getDescriptor();
    }
    public static final com.google.protobuf.Descriptors.EnumDescriptor
        getDescriptor() {
      return com.factset.protobuf.stach.table.VerticalAlignmentProto.getDescriptor().getEnumTypes().get(0);
    }

    private static final VerticalAlignment[] VALUES = values();

    public static VerticalAlignment valueOf(
        com.google.protobuf.Descriptors.EnumValueDescriptor desc) {
      if (desc.getType() != getDescriptor()) {
        throw new java.lang.IllegalArgumentException(
          "EnumValueDescriptor is not for this type.");
      }
      if (desc.getIndex() == -1) {
        return UNRECOGNIZED;
      }
      return VALUES[desc.getIndex()];
    }

    private final int value;

    private VerticalAlignment(int value) {
      this.value = value;
    }

    // @@protoc_insertion_point(enum_scope:factset.protobuf.stach.table.VerticalAlignment)
  }


  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n0fds/protobuf/stach/table/VerticalAlign" +
      "ment.proto\022\034factset.protobuf.stach.table" +
      "*H\n\021VerticalAlignment\022\022\n\016UNKNOWN_VALIGN\020" +
      "\000\022\007\n\003TOP\020\001\022\n\n\006MIDDLE\020\002\022\n\n\006BOTTOM\020\003B\230\001\n c" +
      "om.factset.protobuf.stach.tableB\026Vertica" +
      "lAlignmentProtoZ=github.com/factset/stac" +
      "hschema/go/v2/fds/protobuf/stach/table\252\002" +
      "\034FactSet.Protobuf.Stach.Tableb\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        });
  }

  // @@protoc_insertion_point(outer_class_scope)
}
