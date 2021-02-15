// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service_mfel_interface.proto

package fv.protos.kepsvisor;

public final class ServiceMfelInterface {
  private ServiceMfelInterface() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
  }
  public interface mfelInterfaceConfigOrBuilder
      extends com.google.protobuf.MessageOrBuilder {

    // optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];
    /**
     * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
     */
    boolean hasMsgName();
    /**
     * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
     */
    java.lang.String getMsgName();
    /**
     * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
     */
    com.google.protobuf.ByteString
        getMsgNameBytes();

    // optional int32 portNum = 2 [default = 2702];
    /**
     * <code>optional int32 portNum = 2 [default = 2702];</code>
     */
    boolean hasPortNum();
    /**
     * <code>optional int32 portNum = 2 [default = 2702];</code>
     */
    int getPortNum();

    // optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];
    /**
     * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
     */
    boolean hasMfelHostName();
    /**
     * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
     */
    java.lang.String getMfelHostName();
    /**
     * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
     */
    com.google.protobuf.ByteString
        getMfelHostNameBytes();
  }
  /**
   * Protobuf type {@code service_mfel_interface.mfelInterfaceConfig}
   */
  public static final class mfelInterfaceConfig extends
      com.google.protobuf.GeneratedMessage
      implements mfelInterfaceConfigOrBuilder {
    // Use mfelInterfaceConfig.newBuilder() to construct.
    private mfelInterfaceConfig(com.google.protobuf.GeneratedMessage.Builder<?> builder) {
      super(builder);
      this.unknownFields = builder.getUnknownFields();
    }
    private mfelInterfaceConfig(boolean noInit) { this.unknownFields = com.google.protobuf.UnknownFieldSet.getDefaultInstance(); }

    private static final mfelInterfaceConfig defaultInstance;
    public static mfelInterfaceConfig getDefaultInstance() {
      return defaultInstance;
    }

    public mfelInterfaceConfig getDefaultInstanceForType() {
      return defaultInstance;
    }

    private final com.google.protobuf.UnknownFieldSet unknownFields;
    @java.lang.Override
    public final com.google.protobuf.UnknownFieldSet
        getUnknownFields() {
      return this.unknownFields;
    }
    private mfelInterfaceConfig(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      initFields();
      int mutable_bitField0_ = 0;
      com.google.protobuf.UnknownFieldSet.Builder unknownFields =
          com.google.protobuf.UnknownFieldSet.newBuilder();
      try {
        boolean done = false;
        while (!done) {
          int tag = input.readTag();
          switch (tag) {
            case 0:
              done = true;
              break;
            default: {
              if (!parseUnknownField(input, unknownFields,
                                     extensionRegistry, tag)) {
                done = true;
              }
              break;
            }
            case 10: {
              bitField0_ |= 0x00000001;
              msgName_ = input.readBytes();
              break;
            }
            case 16: {
              bitField0_ |= 0x00000002;
              portNum_ = input.readInt32();
              break;
            }
            case 26: {
              bitField0_ |= 0x00000004;
              mfelHostName_ = input.readBytes();
              break;
            }
          }
        }
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        throw e.setUnfinishedMessage(this);
      } catch (java.io.IOException e) {
        throw new com.google.protobuf.InvalidProtocolBufferException(
            e.getMessage()).setUnfinishedMessage(this);
      } finally {
        this.unknownFields = unknownFields.build();
        makeExtensionsImmutable();
      }
    }
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return fv.protos.kepsvisor.ServiceMfelInterface.internal_static_service_mfel_interface_mfelInterfaceConfig_descriptor;
    }

    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return fv.protos.kepsvisor.ServiceMfelInterface.internal_static_service_mfel_interface_mfelInterfaceConfig_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.class, fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.Builder.class);
    }

    public static com.google.protobuf.Parser<mfelInterfaceConfig> PARSER =
        new com.google.protobuf.AbstractParser<mfelInterfaceConfig>() {
      public mfelInterfaceConfig parsePartialFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws com.google.protobuf.InvalidProtocolBufferException {
        return new mfelInterfaceConfig(input, extensionRegistry);
      }
    };

    @java.lang.Override
    public com.google.protobuf.Parser<mfelInterfaceConfig> getParserForType() {
      return PARSER;
    }

    private int bitField0_;
    // optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];
    public static final int MSGNAME_FIELD_NUMBER = 1;
    private java.lang.Object msgName_;
    /**
     * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
     */
    public boolean hasMsgName() {
      return ((bitField0_ & 0x00000001) == 0x00000001);
    }
    /**
     * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
     */
    public java.lang.String getMsgName() {
      java.lang.Object ref = msgName_;
      if (ref instanceof java.lang.String) {
        return (java.lang.String) ref;
      } else {
        com.google.protobuf.ByteString bs = 
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        if (bs.isValidUtf8()) {
          msgName_ = s;
        }
        return s;
      }
    }
    /**
     * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
     */
    public com.google.protobuf.ByteString
        getMsgNameBytes() {
      java.lang.Object ref = msgName_;
      if (ref instanceof java.lang.String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        msgName_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }

    // optional int32 portNum = 2 [default = 2702];
    public static final int PORTNUM_FIELD_NUMBER = 2;
    private int portNum_;
    /**
     * <code>optional int32 portNum = 2 [default = 2702];</code>
     */
    public boolean hasPortNum() {
      return ((bitField0_ & 0x00000002) == 0x00000002);
    }
    /**
     * <code>optional int32 portNum = 2 [default = 2702];</code>
     */
    public int getPortNum() {
      return portNum_;
    }

    // optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];
    public static final int MFELHOSTNAME_FIELD_NUMBER = 3;
    private java.lang.Object mfelHostName_;
    /**
     * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
     */
    public boolean hasMfelHostName() {
      return ((bitField0_ & 0x00000004) == 0x00000004);
    }
    /**
     * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
     */
    public java.lang.String getMfelHostName() {
      java.lang.Object ref = mfelHostName_;
      if (ref instanceof java.lang.String) {
        return (java.lang.String) ref;
      } else {
        com.google.protobuf.ByteString bs = 
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        if (bs.isValidUtf8()) {
          mfelHostName_ = s;
        }
        return s;
      }
    }
    /**
     * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
     */
    public com.google.protobuf.ByteString
        getMfelHostNameBytes() {
      java.lang.Object ref = mfelHostName_;
      if (ref instanceof java.lang.String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        mfelHostName_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }

    private void initFields() {
      msgName_ = "service_mfel_interface.mfelInterfaceConfig";
      portNum_ = 2702;
      mfelHostName_ = "mfel01.realm.cfe.external";
    }
    private byte memoizedIsInitialized = -1;
    public final boolean isInitialized() {
      byte isInitialized = memoizedIsInitialized;
      if (isInitialized != -1) return isInitialized == 1;

      memoizedIsInitialized = 1;
      return true;
    }

    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (((bitField0_ & 0x00000001) == 0x00000001)) {
        output.writeBytes(1, getMsgNameBytes());
      }
      if (((bitField0_ & 0x00000002) == 0x00000002)) {
        output.writeInt32(2, portNum_);
      }
      if (((bitField0_ & 0x00000004) == 0x00000004)) {
        output.writeBytes(3, getMfelHostNameBytes());
      }
      getUnknownFields().writeTo(output);
    }

    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;

      size = 0;
      if (((bitField0_ & 0x00000001) == 0x00000001)) {
        size += com.google.protobuf.CodedOutputStream
          .computeBytesSize(1, getMsgNameBytes());
      }
      if (((bitField0_ & 0x00000002) == 0x00000002)) {
        size += com.google.protobuf.CodedOutputStream
          .computeInt32Size(2, portNum_);
      }
      if (((bitField0_ & 0x00000004) == 0x00000004)) {
        size += com.google.protobuf.CodedOutputStream
          .computeBytesSize(3, getMfelHostNameBytes());
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }

    private static final long serialVersionUID = 0L;
    @java.lang.Override
    protected java.lang.Object writeReplace()
        throws java.io.ObjectStreamException {
      return super.writeReplace();
    }

    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return PARSER.parseFrom(input);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return PARSER.parseFrom(input, extensionRegistry);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      return PARSER.parseDelimitedFrom(input);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return PARSER.parseDelimitedFrom(input, extensionRegistry);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return PARSER.parseFrom(input);
    }
    public static fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return PARSER.parseFrom(input, extensionRegistry);
    }

    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }

    @java.lang.Override
    protected Builder newBuilderForType(
        com.google.protobuf.GeneratedMessage.BuilderParent parent) {
      Builder builder = new Builder(parent);
      return builder;
    }
    /**
     * Protobuf type {@code service_mfel_interface.mfelInterfaceConfig}
     */
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder>
       implements fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfigOrBuilder {
      public static final com.google.protobuf.Descriptors.Descriptor
          getDescriptor() {
        return fv.protos.kepsvisor.ServiceMfelInterface.internal_static_service_mfel_interface_mfelInterfaceConfig_descriptor;
      }

      protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
          internalGetFieldAccessorTable() {
        return fv.protos.kepsvisor.ServiceMfelInterface.internal_static_service_mfel_interface_mfelInterfaceConfig_fieldAccessorTable
            .ensureFieldAccessorsInitialized(
                fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.class, fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.Builder.class);
      }

      // Construct using fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.newBuilder()
      private Builder() {
        maybeForceBuilderInitialization();
      }

      private Builder(
          com.google.protobuf.GeneratedMessage.BuilderParent parent) {
        super(parent);
        maybeForceBuilderInitialization();
      }
      private void maybeForceBuilderInitialization() {
        if (com.google.protobuf.GeneratedMessage.alwaysUseFieldBuilders) {
        }
      }
      private static Builder create() {
        return new Builder();
      }

      public Builder clear() {
        super.clear();
        msgName_ = "service_mfel_interface.mfelInterfaceConfig";
        bitField0_ = (bitField0_ & ~0x00000001);
        portNum_ = 2702;
        bitField0_ = (bitField0_ & ~0x00000002);
        mfelHostName_ = "mfel01.realm.cfe.external";
        bitField0_ = (bitField0_ & ~0x00000004);
        return this;
      }

      public Builder clone() {
        return create().mergeFrom(buildPartial());
      }

      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return fv.protos.kepsvisor.ServiceMfelInterface.internal_static_service_mfel_interface_mfelInterfaceConfig_descriptor;
      }

      public fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig getDefaultInstanceForType() {
        return fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.getDefaultInstance();
      }

      public fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig build() {
        fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return result;
      }

      public fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig buildPartial() {
        fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig result = new fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig(this);
        int from_bitField0_ = bitField0_;
        int to_bitField0_ = 0;
        if (((from_bitField0_ & 0x00000001) == 0x00000001)) {
          to_bitField0_ |= 0x00000001;
        }
        result.msgName_ = msgName_;
        if (((from_bitField0_ & 0x00000002) == 0x00000002)) {
          to_bitField0_ |= 0x00000002;
        }
        result.portNum_ = portNum_;
        if (((from_bitField0_ & 0x00000004) == 0x00000004)) {
          to_bitField0_ |= 0x00000004;
        }
        result.mfelHostName_ = mfelHostName_;
        result.bitField0_ = to_bitField0_;
        onBuilt();
        return result;
      }

      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig) {
          return mergeFrom((fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }

      public Builder mergeFrom(fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig other) {
        if (other == fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig.getDefaultInstance()) return this;
        if (other.hasMsgName()) {
          bitField0_ |= 0x00000001;
          msgName_ = other.msgName_;
          onChanged();
        }
        if (other.hasPortNum()) {
          setPortNum(other.getPortNum());
        }
        if (other.hasMfelHostName()) {
          bitField0_ |= 0x00000004;
          mfelHostName_ = other.mfelHostName_;
          onChanged();
        }
        this.mergeUnknownFields(other.getUnknownFields());
        return this;
      }

      public final boolean isInitialized() {
        return true;
      }

      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig parsedMessage = null;
        try {
          parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
        } catch (com.google.protobuf.InvalidProtocolBufferException e) {
          parsedMessage = (fv.protos.kepsvisor.ServiceMfelInterface.mfelInterfaceConfig) e.getUnfinishedMessage();
          throw e;
        } finally {
          if (parsedMessage != null) {
            mergeFrom(parsedMessage);
          }
        }
        return this;
      }
      private int bitField0_;

      // optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];
      private java.lang.Object msgName_ = "service_mfel_interface.mfelInterfaceConfig";
      /**
       * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
       */
      public boolean hasMsgName() {
        return ((bitField0_ & 0x00000001) == 0x00000001);
      }
      /**
       * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
       */
      public java.lang.String getMsgName() {
        java.lang.Object ref = msgName_;
        if (!(ref instanceof java.lang.String)) {
          java.lang.String s = ((com.google.protobuf.ByteString) ref)
              .toStringUtf8();
          msgName_ = s;
          return s;
        } else {
          return (java.lang.String) ref;
        }
      }
      /**
       * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
       */
      public com.google.protobuf.ByteString
          getMsgNameBytes() {
        java.lang.Object ref = msgName_;
        if (ref instanceof String) {
          com.google.protobuf.ByteString b = 
              com.google.protobuf.ByteString.copyFromUtf8(
                  (java.lang.String) ref);
          msgName_ = b;
          return b;
        } else {
          return (com.google.protobuf.ByteString) ref;
        }
      }
      /**
       * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
       */
      public Builder setMsgName(
          java.lang.String value) {
        if (value == null) {
    throw new NullPointerException();
  }
  bitField0_ |= 0x00000001;
        msgName_ = value;
        onChanged();
        return this;
      }
      /**
       * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
       */
      public Builder clearMsgName() {
        bitField0_ = (bitField0_ & ~0x00000001);
        msgName_ = getDefaultInstance().getMsgName();
        onChanged();
        return this;
      }
      /**
       * <code>optional string msgName = 1 [default = "service_mfel_interface.mfelInterfaceConfig"];</code>
       */
      public Builder setMsgNameBytes(
          com.google.protobuf.ByteString value) {
        if (value == null) {
    throw new NullPointerException();
  }
  bitField0_ |= 0x00000001;
        msgName_ = value;
        onChanged();
        return this;
      }

      // optional int32 portNum = 2 [default = 2702];
      private int portNum_ = 2702;
      /**
       * <code>optional int32 portNum = 2 [default = 2702];</code>
       */
      public boolean hasPortNum() {
        return ((bitField0_ & 0x00000002) == 0x00000002);
      }
      /**
       * <code>optional int32 portNum = 2 [default = 2702];</code>
       */
      public int getPortNum() {
        return portNum_;
      }
      /**
       * <code>optional int32 portNum = 2 [default = 2702];</code>
       */
      public Builder setPortNum(int value) {
        bitField0_ |= 0x00000002;
        portNum_ = value;
        onChanged();
        return this;
      }
      /**
       * <code>optional int32 portNum = 2 [default = 2702];</code>
       */
      public Builder clearPortNum() {
        bitField0_ = (bitField0_ & ~0x00000002);
        portNum_ = 2702;
        onChanged();
        return this;
      }

      // optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];
      private java.lang.Object mfelHostName_ = "mfel01.realm.cfe.external";
      /**
       * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
       */
      public boolean hasMfelHostName() {
        return ((bitField0_ & 0x00000004) == 0x00000004);
      }
      /**
       * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
       */
      public java.lang.String getMfelHostName() {
        java.lang.Object ref = mfelHostName_;
        if (!(ref instanceof java.lang.String)) {
          java.lang.String s = ((com.google.protobuf.ByteString) ref)
              .toStringUtf8();
          mfelHostName_ = s;
          return s;
        } else {
          return (java.lang.String) ref;
        }
      }
      /**
       * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
       */
      public com.google.protobuf.ByteString
          getMfelHostNameBytes() {
        java.lang.Object ref = mfelHostName_;
        if (ref instanceof String) {
          com.google.protobuf.ByteString b = 
              com.google.protobuf.ByteString.copyFromUtf8(
                  (java.lang.String) ref);
          mfelHostName_ = b;
          return b;
        } else {
          return (com.google.protobuf.ByteString) ref;
        }
      }
      /**
       * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
       */
      public Builder setMfelHostName(
          java.lang.String value) {
        if (value == null) {
    throw new NullPointerException();
  }
  bitField0_ |= 0x00000004;
        mfelHostName_ = value;
        onChanged();
        return this;
      }
      /**
       * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
       */
      public Builder clearMfelHostName() {
        bitField0_ = (bitField0_ & ~0x00000004);
        mfelHostName_ = getDefaultInstance().getMfelHostName();
        onChanged();
        return this;
      }
      /**
       * <code>optional string mfelHostName = 3 [default = "mfel01.realm.cfe.external"];</code>
       */
      public Builder setMfelHostNameBytes(
          com.google.protobuf.ByteString value) {
        if (value == null) {
    throw new NullPointerException();
  }
  bitField0_ |= 0x00000004;
        mfelHostName_ = value;
        onChanged();
        return this;
      }

      // @@protoc_insertion_point(builder_scope:service_mfel_interface.mfelInterfaceConfig)
    }

    static {
      defaultInstance = new mfelInterfaceConfig(true);
      defaultInstance.initFields();
    }

    // @@protoc_insertion_point(class_scope:service_mfel_interface.mfelInterfaceConfig)
  }

  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_service_mfel_interface_mfelInterfaceConfig_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_service_mfel_interface_mfelInterfaceConfig_fieldAccessorTable;

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\034service_mfel_interface.proto\022\026service_" +
      "mfel_interface\"\232\001\n\023mfelInterfaceConfig\022;" +
      "\n\007msgName\030\001 \001(\t:*service_mfel_interface." +
      "mfelInterfaceConfig\022\025\n\007portNum\030\002 \001(\005:\00427" +
      "02\022/\n\014mfelHostName\030\003 \001(\t:\031mfel01.realm.c" +
      "fe.externalB\025\n\023fv.protos.kepsvisor"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
      new com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner() {
        public com.google.protobuf.ExtensionRegistry assignDescriptors(
            com.google.protobuf.Descriptors.FileDescriptor root) {
          descriptor = root;
          internal_static_service_mfel_interface_mfelInterfaceConfig_descriptor =
            getDescriptor().getMessageTypes().get(0);
          internal_static_service_mfel_interface_mfelInterfaceConfig_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_service_mfel_interface_mfelInterfaceConfig_descriptor,
              new java.lang.String[] { "MsgName", "PortNum", "MfelHostName", });
          return null;
        }
      };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        }, assigner);
  }

  // @@protoc_insertion_point(outer_class_scope)
}
