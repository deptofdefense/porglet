// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service_snapex_servers.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "service_snapex_servers.pb.h"

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

namespace service_snapex_servers {

namespace {

const ::google::protobuf::Descriptor* SESConfigMess_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  SESConfigMess_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_service_5fsnapex_5fservers_2eproto() {
  protobuf_AddDesc_service_5fsnapex_5fservers_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "service_snapex_servers.proto");
  GOOGLE_CHECK(file != NULL);
  SESConfigMess_descriptor_ = file->message_type(0);
  static const int SESConfigMess_offsets_[3] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SESConfigMess, msgname_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SESConfigMess, snapex_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SESConfigMess, script_),
  };
  SESConfigMess_reflection_ =
    new ::google::protobuf::internal::GeneratedMessageReflection(
      SESConfigMess_descriptor_,
      SESConfigMess::default_instance_,
      SESConfigMess_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SESConfigMess, _has_bits_[0]),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(SESConfigMess, _unknown_fields_),
      -1,
      ::google::protobuf::DescriptorPool::generated_pool(),
      ::google::protobuf::MessageFactory::generated_factory(),
      sizeof(SESConfigMess));
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_service_5fsnapex_5fservers_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
    SESConfigMess_descriptor_, &SESConfigMess::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_service_5fsnapex_5fservers_2eproto() {
  delete SESConfigMess::default_instance_;
  delete SESConfigMess_reflection_;
  delete SESConfigMess::_default_msgname_;
  delete SESConfigMess::_default_snapex_;
  delete SESConfigMess::_default_script_;
}

void protobuf_AddDesc_service_5fsnapex_5fservers_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\034service_snapex_servers.proto\022\026service_"
    "snapex_servers\"\260\001\n\rSESConfigMess\022\036\n\007msgN"
    "ame\030\001 \001(\t:\rSESCONFIGMESS\022D\n\006snapex\030\002 \001(\t"
    ":4/apps/m2extra/ext/src/snapextra/python"
    "/snap_extra.py\0229\n\006script\030\003 \001(\t:)/user/co"
    "nfig/snap_extra/snap_extra_ht.cfg", 233);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "service_snapex_servers.proto", &protobuf_RegisterTypes);
  SESConfigMess::_default_msgname_ =
      new ::std::string("SESCONFIGMESS", 13);
  SESConfigMess::_default_snapex_ =
      new ::std::string("/apps/m2extra/ext/src/snapextra/python/snap_extra.py", 52);
  SESConfigMess::_default_script_ =
      new ::std::string("/user/config/snap_extra/snap_extra_ht.cfg", 41);
  SESConfigMess::default_instance_ = new SESConfigMess();
  SESConfigMess::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_service_5fsnapex_5fservers_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_service_5fsnapex_5fservers_2eproto {
  StaticDescriptorInitializer_service_5fsnapex_5fservers_2eproto() {
    protobuf_AddDesc_service_5fsnapex_5fservers_2eproto();
  }
} static_descriptor_initializer_service_5fsnapex_5fservers_2eproto_;

// ===================================================================

::std::string* SESConfigMess::_default_msgname_ = NULL;
::std::string* SESConfigMess::_default_snapex_ = NULL;
::std::string* SESConfigMess::_default_script_ = NULL;
#ifndef _MSC_VER
const int SESConfigMess::kMsgNameFieldNumber;
const int SESConfigMess::kSnapexFieldNumber;
const int SESConfigMess::kScriptFieldNumber;
#endif  // !_MSC_VER

SESConfigMess::SESConfigMess()
  : ::google::protobuf::Message() {
  SharedCtor();
}

void SESConfigMess::InitAsDefaultInstance() {
}

SESConfigMess::SESConfigMess(const SESConfigMess& from)
  : ::google::protobuf::Message() {
  SharedCtor();
  MergeFrom(from);
}

void SESConfigMess::SharedCtor() {
  _cached_size_ = 0;
  msgname_ = const_cast< ::std::string*>(_default_msgname_);
  snapex_ = const_cast< ::std::string*>(_default_snapex_);
  script_ = const_cast< ::std::string*>(_default_script_);
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

SESConfigMess::~SESConfigMess() {
  SharedDtor();
}

void SESConfigMess::SharedDtor() {
  if (msgname_ != _default_msgname_) {
    delete msgname_;
  }
  if (snapex_ != _default_snapex_) {
    delete snapex_;
  }
  if (script_ != _default_script_) {
    delete script_;
  }
  if (this != default_instance_) {
  }
}

void SESConfigMess::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* SESConfigMess::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return SESConfigMess_descriptor_;
}

const SESConfigMess& SESConfigMess::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_service_5fsnapex_5fservers_2eproto();
  return *default_instance_;
}

SESConfigMess* SESConfigMess::default_instance_ = NULL;

SESConfigMess* SESConfigMess::New() const {
  return new SESConfigMess;
}

void SESConfigMess::Clear() {
  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (has_msgname()) {
      if (msgname_ != _default_msgname_) {
        msgname_->assign(*_default_msgname_);
      }
    }
    if (has_snapex()) {
      if (snapex_ != _default_snapex_) {
        snapex_->assign(*_default_snapex_);
      }
    }
    if (has_script()) {
      if (script_ != _default_script_) {
        script_->assign(*_default_script_);
      }
    }
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  mutable_unknown_fields()->Clear();
}

bool SESConfigMess::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!(EXPRESSION)) return false
  ::google::protobuf::uint32 tag;
  while ((tag = input->ReadTag()) != 0) {
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional string msgName = 1 [default = "SESCONFIGMESS"];
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
        if (input->ExpectTag(18)) goto parse_snapex;
        break;
      }

      // optional string snapex = 2 [default = "/apps/m2extra/ext/src/snapextra/python/snap_extra.py"];
      case 2: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_LENGTH_DELIMITED) {
         parse_snapex:
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_snapex()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8String(
            this->snapex().data(), this->snapex().length(),
            ::google::protobuf::internal::WireFormat::PARSE);
        } else {
          goto handle_uninterpreted;
        }
        if (input->ExpectTag(26)) goto parse_script;
        break;
      }

      // optional string script = 3 [default = "/user/config/snap_extra/snap_extra_ht.cfg"];
      case 3: {
        if (::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_LENGTH_DELIMITED) {
         parse_script:
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_script()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8String(
            this->script().data(), this->script().length(),
            ::google::protobuf::internal::WireFormat::PARSE);
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

void SESConfigMess::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // optional string msgName = 1 [default = "SESCONFIGMESS"];
  if (has_msgname()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->msgname().data(), this->msgname().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    ::google::protobuf::internal::WireFormatLite::WriteString(
      1, this->msgname(), output);
  }

  // optional string snapex = 2 [default = "/apps/m2extra/ext/src/snapextra/python/snap_extra.py"];
  if (has_snapex()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->snapex().data(), this->snapex().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    ::google::protobuf::internal::WireFormatLite::WriteString(
      2, this->snapex(), output);
  }

  // optional string script = 3 [default = "/user/config/snap_extra/snap_extra_ht.cfg"];
  if (has_script()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->script().data(), this->script().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    ::google::protobuf::internal::WireFormatLite::WriteString(
      3, this->script(), output);
  }

  if (!unknown_fields().empty()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
}

::google::protobuf::uint8* SESConfigMess::SerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // optional string msgName = 1 [default = "SESCONFIGMESS"];
  if (has_msgname()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->msgname().data(), this->msgname().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        1, this->msgname(), target);
  }

  // optional string snapex = 2 [default = "/apps/m2extra/ext/src/snapextra/python/snap_extra.py"];
  if (has_snapex()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->snapex().data(), this->snapex().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        2, this->snapex(), target);
  }

  // optional string script = 3 [default = "/user/config/snap_extra/snap_extra_ht.cfg"];
  if (has_script()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8String(
      this->script().data(), this->script().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE);
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        3, this->script(), target);
  }

  if (!unknown_fields().empty()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  return target;
}

int SESConfigMess::ByteSize() const {
  int total_size = 0;

  if (_has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    // optional string msgName = 1 [default = "SESCONFIGMESS"];
    if (has_msgname()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::StringSize(
          this->msgname());
    }

    // optional string snapex = 2 [default = "/apps/m2extra/ext/src/snapextra/python/snap_extra.py"];
    if (has_snapex()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::StringSize(
          this->snapex());
    }

    // optional string script = 3 [default = "/user/config/snap_extra/snap_extra_ht.cfg"];
    if (has_script()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::StringSize(
          this->script());
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

void SESConfigMess::MergeFrom(const ::google::protobuf::Message& from) {
  GOOGLE_CHECK_NE(&from, this);
  const SESConfigMess* source =
    ::google::protobuf::internal::dynamic_cast_if_available<const SESConfigMess*>(
      &from);
  if (source == NULL) {
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
    MergeFrom(*source);
  }
}

void SESConfigMess::MergeFrom(const SESConfigMess& from) {
  GOOGLE_CHECK_NE(&from, this);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_msgname()) {
      set_msgname(from.msgname());
    }
    if (from.has_snapex()) {
      set_snapex(from.snapex());
    }
    if (from.has_script()) {
      set_script(from.script());
    }
  }
  mutable_unknown_fields()->MergeFrom(from.unknown_fields());
}

void SESConfigMess::CopyFrom(const ::google::protobuf::Message& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void SESConfigMess::CopyFrom(const SESConfigMess& from) {
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool SESConfigMess::IsInitialized() const {

  return true;
}

void SESConfigMess::Swap(SESConfigMess* other) {
  if (other != this) {
    std::swap(msgname_, other->msgname_);
    std::swap(snapex_, other->snapex_);
    std::swap(script_, other->script_);
    std::swap(_has_bits_[0], other->_has_bits_[0]);
    _unknown_fields_.Swap(&other->_unknown_fields_);
    std::swap(_cached_size_, other->_cached_size_);
  }
}

::google::protobuf::Metadata SESConfigMess::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = SESConfigMess_descriptor_;
  metadata.reflection = SESConfigMess_reflection_;
  return metadata;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace service_snapex_servers

// @@protoc_insertion_point(global_scope)
