// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: IQData.proto

#ifndef PROTOBUF_IQData_2eproto__INCLUDED
#define PROTOBUF_IQData_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2005000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
#include "TunerMessages.pb.h"
#include "ServiceInfrastructureCommon.pb.h"
// @@protoc_insertion_point(includes)

namespace public_topics {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_IQData_2eproto();
void protobuf_AssignDesc_IQData_2eproto();
void protobuf_ShutdownFile_IQData_2eproto();

class IQDataTopic;

// ===================================================================

class IQDataTopic : public ::google::protobuf::Message {
 public:
  IQDataTopic();
  virtual ~IQDataTopic();

  IQDataTopic(const IQDataTopic& from);

  inline IQDataTopic& operator=(const IQDataTopic& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const IQDataTopic& default_instance();

  void Swap(IQDataTopic* other);

  // implements Message ----------------------------------------------

  IQDataTopic* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const IQDataTopic& from);
  void MergeFrom(const IQDataTopic& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // optional .service_infrastructure.Header header = 1;
  inline bool has_header() const;
  inline void clear_header();
  static const int kHeaderFieldNumber = 1;
  inline const ::service_infrastructure::Header& header() const;
  inline ::service_infrastructure::Header* mutable_header();
  inline ::service_infrastructure::Header* release_header();
  inline void set_allocated_header(::service_infrastructure::Header* header);

  // optional .tuner_msg.SnapInfo snap_info = 2;
  inline bool has_snap_info() const;
  inline void clear_snap_info();
  static const int kSnapInfoFieldNumber = 2;
  inline const ::tuner_msg::SnapInfo& snap_info() const;
  inline ::tuner_msg::SnapInfo* mutable_snap_info();
  inline ::tuner_msg::SnapInfo* release_snap_info();
  inline void set_allocated_snap_info(::tuner_msg::SnapInfo* snap_info);

  // @@protoc_insertion_point(class_scope:public_topics.IQDataTopic)
 private:
  inline void set_has_header();
  inline void clear_has_header();
  inline void set_has_snap_info();
  inline void clear_has_snap_info();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::service_infrastructure::Header* header_;
  ::tuner_msg::SnapInfo* snap_info_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(2 + 31) / 32];

  friend void  protobuf_AddDesc_IQData_2eproto();
  friend void protobuf_AssignDesc_IQData_2eproto();
  friend void protobuf_ShutdownFile_IQData_2eproto();

  void InitAsDefaultInstance();
  static IQDataTopic* default_instance_;
};
// ===================================================================


// ===================================================================

// IQDataTopic

// optional .service_infrastructure.Header header = 1;
inline bool IQDataTopic::has_header() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void IQDataTopic::set_has_header() {
  _has_bits_[0] |= 0x00000001u;
}
inline void IQDataTopic::clear_has_header() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void IQDataTopic::clear_header() {
  if (header_ != NULL) header_->::service_infrastructure::Header::Clear();
  clear_has_header();
}
inline const ::service_infrastructure::Header& IQDataTopic::header() const {
  return header_ != NULL ? *header_ : *default_instance_->header_;
}
inline ::service_infrastructure::Header* IQDataTopic::mutable_header() {
  set_has_header();
  if (header_ == NULL) header_ = new ::service_infrastructure::Header;
  return header_;
}
inline ::service_infrastructure::Header* IQDataTopic::release_header() {
  clear_has_header();
  ::service_infrastructure::Header* temp = header_;
  header_ = NULL;
  return temp;
}
inline void IQDataTopic::set_allocated_header(::service_infrastructure::Header* header) {
  delete header_;
  header_ = header;
  if (header) {
    set_has_header();
  } else {
    clear_has_header();
  }
}

// optional .tuner_msg.SnapInfo snap_info = 2;
inline bool IQDataTopic::has_snap_info() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void IQDataTopic::set_has_snap_info() {
  _has_bits_[0] |= 0x00000002u;
}
inline void IQDataTopic::clear_has_snap_info() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void IQDataTopic::clear_snap_info() {
  if (snap_info_ != NULL) snap_info_->::tuner_msg::SnapInfo::Clear();
  clear_has_snap_info();
}
inline const ::tuner_msg::SnapInfo& IQDataTopic::snap_info() const {
  return snap_info_ != NULL ? *snap_info_ : *default_instance_->snap_info_;
}
inline ::tuner_msg::SnapInfo* IQDataTopic::mutable_snap_info() {
  set_has_snap_info();
  if (snap_info_ == NULL) snap_info_ = new ::tuner_msg::SnapInfo;
  return snap_info_;
}
inline ::tuner_msg::SnapInfo* IQDataTopic::release_snap_info() {
  clear_has_snap_info();
  ::tuner_msg::SnapInfo* temp = snap_info_;
  snap_info_ = NULL;
  return temp;
}
inline void IQDataTopic::set_allocated_snap_info(::tuner_msg::SnapInfo* snap_info) {
  delete snap_info_;
  snap_info_ = snap_info;
  if (snap_info) {
    set_has_snap_info();
  } else {
    clear_has_snap_info();
  }
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace public_topics

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_IQData_2eproto__INCLUDED
