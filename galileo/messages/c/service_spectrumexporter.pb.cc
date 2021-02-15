// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service_spectrumexporter.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "service_spectrumexporter.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace service_spectrum_exporter {

namespace {

const ::google::protobuf::Descriptor* SpectrumExporterConfig_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  SpectrumExporterConfig_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_service_5fspectrumexporter_2eproto() {
  protobuf_AddDesc_service_5fspectrumexporter_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "service_spectrumexporter.proto");
  GOOGLE_CHECK(file != NULL);
  SpectrumExporterConfig_descriptor_ = file->message_type(0);
  static const int SpectrumExporterConfig_offsets_[3] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SpectrumExporterConfig, msgname_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SpectrumExporterConfig, channel_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SpectrumExporterConfig, fftlength_),
  };
  SpectrumExporterConfig_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      SpectrumExporterConfig_descriptor_,
      SpectrumExporterConfig::default_instance_,
      SpectrumExporterConfig_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SpectrumExporterConfig, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SpectrumExporterConfig, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(SpectrumExporterConfig));
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_service_5fspectrumexporter_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    SpectrumExporterConfig_descriptor_, &SpectrumExporterConfig::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_service_5fspectrumexporter_2eproto() {
  delete SpectrumExporterConfig::default_instance_;
  delete SpectrumExporterConfig_reflection_;
  delete SpectrumExporterConfig::_default_msgname_;
}

void protobuf_AddDesc_service_5fspectrumexporter_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\036service_spectrumexporter.proto\022\031servic"
    "e_spectrum_exporter\"\211\001\n\026SpectrumExporter"
    "Config\022A\n\007msgName\030\001 \001(\t:0service_spectru"
    "m_exporter.SpectrumExporterConfig\022\023\n\007cha"
    "nnel\030\002 \001(\005:\00272\022\027\n\tfftLength\030\003 \001(\005:\0044096B"
    "\025\n\023fv.protos.kepsvisor", 222);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "service_spectrumexporter.proto", &protobuf_RegisterTypes);
  SpectrumExporterConfig::_default_msgname_ =
      new ::std::string("service_spectrum_exporter.SpectrumExporterConfig", 48);
  SpectrumExporterConfig::default_instance_ = new SpectrumExporterConfig();
  SpectrumExporterConfig::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_service_5fspectrumexporter_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_service_5fspectrumexporter_2eproto {
  StaticDescriptorInitializer_service_5fspectrumexporter_2eproto() {
    protobuf_AddDesc_service_5fspectrumexporter_2eproto();
  }
} static_descriptor_initializer_service_5fspectrumexporter_2eproto_;

// ===================================================================

::std::string* SpectrumExporterConfig::_default_msgname_ = NULL;
#ifndef _MSC_VER
const int SpectrumExporterConfig::kMsgNameFieldNumber;
const int SpectrumExporterConfig::kChannelFieldNumber;
const int SpectrumExporterConfig::kFftLengthFieldNumber;
#endif  // !_MSC_VER

SpectrumExporterConfig::SpectrumExporterConfig()
  : ::google::protobuf::Message() {
  SharedCtor();
}

void SpectrumExporterConfig::InitAsDefaultInstance() {
}

SpectrumExporterConfig::SpectrumExporterConfig(const SpectrumExporterConfig& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
}

void SpectrumExporterConfig::SharedCtor() {
  _cached_size_ = 0;
  msgname_ = const_cast< ::std::string*>(_default_msgname_);
  channel_ = 72;
  fftlength_ = 4096;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

SpectrumExporterConfig::~SpectrumExporterConfig() {
  SharedDtor();
}

void SpectrumExporterConfig::SharedDtor() {
  if (msgname_ != _default_msgname_) {
    delete msgname_;
  }
  if (this != default_instance_) {
  }
}

void SpectrumExporterConfig::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* SpectrumExporterConfig::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return SpectrumExporterConfig_descriptor_;
}

const SpectrumExporterConfig& SpectrumExporterConfig::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_service_5fspectrumexporter_2eproto();
  return *default_instance_;
}

SpectrumExporterConfig* SpectrumExporterConfig::default_instance_ = NULL;

SpectrumExporterConfig* SpectrumExporterConfig::New() const {
  return new SpectrumExporterConfig;
}

void SpectrumExporterConfig::Clear() {
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (has_msgname()) {
      if (msgname_ != _default_msgname_) {
        msgname_->assign(*_default_msgname_);
      }
    }
    channel_ = 72;
    fftlength_ = 4096;
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool SpectrumExporterConfig::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) return false
  ::google::protobuf::uint32 tag;
  while ((tag = input->ReadTag()) != 0) {
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional string msgName = 1 [default = "service_spectrum_exporter.SpectrumExporterConfig"];
      case 1: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_LENGTH_DELIMITED) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_msgname()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8String(
            this->msgname().data(), this->msgname().length(),
            ::google::protobuf::internal::WireFormat::PARSE);
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(16)) goto parse_channel;
        break;
      }

      // optional int32 channel = 2 [default = 72];
      case 2: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_VARINT) {
         parse_channel:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &channel_)));
          set_has_channel();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(24)) goto parse_fftLength;
        break;
      }

      // optional int32 fftLength = 3 [default = 4096];
      case 3: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_VARINT) {
         parse_fftLength:
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &fftlength_)));
          set_has_fftlength();
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectAtEnd()) return true;
        break;
      }

      default: {
      handle_uninterpreted:
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          return true;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
  return true;
#undef DO_
}

void SpectrumExporterConfig::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // optional string msgName = 1 [default = "service_spectrum_exporter.SpectrumExporterConfig"];
  if (has_msgname()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->msgname().data(), this->msgname().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    ::google::protobuf::internal::WireFormatLite::WriteString(
      1, this->msgname(), output);
  }

  // optional int32 channel = 2 [default = 72];
  if (has_channel()) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(2, this->channel(), output);
  }

  // optional int32 fftLength = 3 [default = 4096];
  if (has_fftlength()) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(3, this->fftlength(), output);
  }

  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
}

::google::protobuf::uint8* SpectrumExporterConfig::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // optional string msgName = 1 [default = "service_spectrum_exporter.SpectrumExporterConfig"];
  if (has_msgname()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->msgname().data(), this->msgname().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        1, this->msgname(), target);
  }

  // optional int32 channel = 2 [default = 72];
  if (has_channel()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(2, this->channel(), target);
  }

  // optional int32 fftLength = 3 [default = 4096];
  if (has_fftlength()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(3, this->fftlength(), target);
  }

  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  return target;
}

int SpectrumExporterConfig::ByteSize() const {
  int total_size = 0;

  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // optional string msgName = 1 [default = "service_spectrum_exporter.SpectrumExporterConfig"];
    if (has_msgname()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::StringSize(
          this->msgname());
    }

    // optional int32 channel = 2 [default = 72];
    if (has_channel()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::Int32Size(
          this->channel());
    }

    // optional int32 fftLength = 3 [default = 4096];
    if (has_fftlength()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::Int32Size(
          this->fftlength());
    }

  }
  if (!unknown_fields().empty()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void SpectrumExporterConfig::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const SpectrumExporterConfig* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const SpectrumExporterConfig*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void SpectrumExporterConfig::MergeFrom(const SpectrumExporterConfig& from) {
  GOOGLE_CHECK_NE(&from, this);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_msgname()) {
      set_msgname(from.msgname());
    }
    if (from.has_channel()) {
      set_channel(from.channel());
    }
    if (from.has_fftlength()) {
      set_fftlength(from.fftlength());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void SpectrumExporterConfig::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void SpectrumExporterConfig::CopyFrom(const SpectrumExporterConfig& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool SpectrumExporterConfig::IsInitialized() const {

  return true;
}

void SpectrumExporterConfig::Swap(SpectrumExporterConfig* other) {
  if (other != this) {
    std::swap(msgname_, other->msgname_);
    std::swap(channel_, other->channel_);
    std::swap(fftlength_, other->fftlength_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata SpectrumExporterConfig::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = SpectrumExporterConfig_descriptor_;
  metadata.reflection = SpectrumExporterConfig_reflection_;
  return metadata;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace service_spectrum_exporter

// @@protoc_insertion_point(global_scope)
