// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: SettingsExternalIF.proto

#ifndef PROTOBUF_SettingsExternalIF_2eproto__INCLUDED
#define PROTOBUF_SettingsExternalIF_2eproto__INCLUDED

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
// @@protoc_insertion_point(includes)

namespace settings_exif_msg {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_SettingsExternalIF_2eproto();
void protobuf_AssignDesc_SettingsExternalIF_2eproto();
void protobuf_ShutdownFile_SettingsExternalIF_2eproto();

class RequestStatus;
class StatusUpdate;

// ===================================================================

class RequestStatus : public ::google::protobuf::Message {
 public:
  RequestStatus();
  virtual ~RequestStatus();

  RequestStatus(const RequestStatus& from);

  inline RequestStatus& operator=(const RequestStatus& from) {
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
  static const RequestStatus& default_instance();

  void Swap(RequestStatus* other);

  // implements Message ----------------------------------------------

  RequestStatus* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const RequestStatus& from);
  void MergeFrom(const RequestStatus& from);
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

  // optional string msgName = 1 [default = "REQUEST_STATUS"];
  inline bool has_msgname() const;
  inline void clear_msgname();
  static const int kMsgNameFieldNumber = 1;
  inline const ::std::string& msgname() const;
  inline void set_msgname(const ::std::string& value);
  inline void set_msgname(const char* value);
  inline void set_msgname(const char* value, size_t size);
  inline ::std::string* mutable_msgname();
  inline ::std::string* release_msgname();
  inline void set_allocated_msgname(::std::string* msgname);

  // optional int32 msg_type = 2 [default = 0];
  inline bool has_msg_type() const;
  inline void clear_msg_type();
  static const int kMsgTypeFieldNumber = 2;
  inline ::google::protobuf::int32 msg_type() const;
  inline void set_msg_type(::google::protobuf::int32 value);

  // @@protoc_insertion_point(class_scope:settings_exif_msg.RequestStatus)
 private:
  inline void set_has_msgname();
  inline void clear_has_msgname();
  inline void set_has_msg_type();
  inline void clear_has_msg_type();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::std::string* msgname_;
  static ::std::string* _default_msgname_;
  ::google::protobuf::int32 msg_type_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(2 + 31) / 32];

  friend void  protobuf_AddDesc_SettingsExternalIF_2eproto();
  friend void protobuf_AssignDesc_SettingsExternalIF_2eproto();
  friend void protobuf_ShutdownFile_SettingsExternalIF_2eproto();

  void InitAsDefaultInstance();
  static RequestStatus* default_instance_;
};
// -------------------------------------------------------------------

class StatusUpdate : public ::google::protobuf::Message {
 public:
  StatusUpdate();
  virtual ~StatusUpdate();

  StatusUpdate(const StatusUpdate& from);

  inline StatusUpdate& operator=(const StatusUpdate& from) {
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
  static const StatusUpdate& default_instance();

  void Swap(StatusUpdate* other);

  // implements Message ----------------------------------------------

  StatusUpdate* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const StatusUpdate& from);
  void MergeFrom(const StatusUpdate& from);
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

  // optional string msgName = 1 [default = "STATUS_UPDATE"];
  inline bool has_msgname() const;
  inline void clear_msgname();
  static const int kMsgNameFieldNumber = 1;
  inline const ::std::string& msgname() const;
  inline void set_msgname(const ::std::string& value);
  inline void set_msgname(const char* value);
  inline void set_msgname(const char* value, size_t size);
  inline ::std::string* mutable_msgname();
  inline ::std::string* release_msgname();
  inline void set_allocated_msgname(::std::string* msgname);

  // optional float rf_freq = 2;
  inline bool has_rf_freq() const;
  inline void clear_rf_freq();
  static const int kRfFreqFieldNumber = 2;
  inline float rf_freq() const;
  inline void set_rf_freq(float value);

  // optional bool spectral_inv = 3 [default = false];
  inline bool has_spectral_inv() const;
  inline void clear_spectral_inv();
  static const int kSpectralInvFieldNumber = 3;
  inline bool spectral_inv() const;
  inline void set_spectral_inv(bool value);

  // optional bool activated = 4 [default = false];
  inline bool has_activated() const;
  inline void clear_activated();
  static const int kActivatedFieldNumber = 4;
  inline bool activated() const;
  inline void set_activated(bool value);

  // optional float if_freq = 5 [default = 160];
  inline bool has_if_freq() const;
  inline void clear_if_freq();
  static const int kIfFreqFieldNumber = 5;
  inline float if_freq() const;
  inline void set_if_freq(float value);

  // @@protoc_insertion_point(class_scope:settings_exif_msg.StatusUpdate)
 private:
  inline void set_has_msgname();
  inline void clear_has_msgname();
  inline void set_has_rf_freq();
  inline void clear_has_rf_freq();
  inline void set_has_spectral_inv();
  inline void clear_has_spectral_inv();
  inline void set_has_activated();
  inline void clear_has_activated();
  inline void set_has_if_freq();
  inline void clear_has_if_freq();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::std::string* msgname_;
  static ::std::string* _default_msgname_;
  float rf_freq_;
  bool spectral_inv_;
  bool activated_;
  float if_freq_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(5 + 31) / 32];

  friend void  protobuf_AddDesc_SettingsExternalIF_2eproto();
  friend void protobuf_AssignDesc_SettingsExternalIF_2eproto();
  friend void protobuf_ShutdownFile_SettingsExternalIF_2eproto();

  void InitAsDefaultInstance();
  static StatusUpdate* default_instance_;
};
// ===================================================================


// ===================================================================

// RequestStatus

// optional string msgName = 1 [default = "REQUEST_STATUS"];
inline bool RequestStatus::has_msgname() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void RequestStatus::set_has_msgname() {
  _has_bits_[0] |= 0x00000001u;
}
inline void RequestStatus::clear_has_msgname() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void RequestStatus::clear_msgname() {
  if (msgname_ != _default_msgname_) {
    msgname_->assign(*_default_msgname_);
  }
  clear_has_msgname();
}
inline const ::std::string& RequestStatus::msgname() const {
  return *msgname_;
}
inline void RequestStatus::set_msgname(const ::std::string& value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void RequestStatus::set_msgname(const char* value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void RequestStatus::set_msgname(const char* value, size_t size) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* RequestStatus::mutable_msgname() {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string(*_default_msgname_);
  }
  return msgname_;
}
inline ::std::string* RequestStatus::release_msgname() {
  clear_has_msgname();
  if (msgname_ == _default_msgname_) {
    return NULL;
  } else {
    ::std::string* temp = msgname_;
    msgname_ = const_cast< ::std::string*>(_default_msgname_);
    return temp;
  }
}
inline void RequestStatus::set_allocated_msgname(::std::string* msgname) {
  if (msgname_ != _default_msgname_) {
    delete msgname_;
  }
  if (msgname) {
    set_has_msgname();
    msgname_ = msgname;
  } else {
    clear_has_msgname();
    msgname_ = const_cast< ::std::string*>(_default_msgname_);
  }
}

// optional int32 msg_type = 2 [default = 0];
inline bool RequestStatus::has_msg_type() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void RequestStatus::set_has_msg_type() {
  _has_bits_[0] |= 0x00000002u;
}
inline void RequestStatus::clear_has_msg_type() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void RequestStatus::clear_msg_type() {
  msg_type_ = 0;
  clear_has_msg_type();
}
inline ::google::protobuf::int32 RequestStatus::msg_type() const {
  return msg_type_;
}
inline void RequestStatus::set_msg_type(::google::protobuf::int32 value) {
  set_has_msg_type();
  msg_type_ = value;
}

// -------------------------------------------------------------------

// StatusUpdate

// optional string msgName = 1 [default = "STATUS_UPDATE"];
inline bool StatusUpdate::has_msgname() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void StatusUpdate::set_has_msgname() {
  _has_bits_[0] |= 0x00000001u;
}
inline void StatusUpdate::clear_has_msgname() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void StatusUpdate::clear_msgname() {
  if (msgname_ != _default_msgname_) {
    msgname_->assign(*_default_msgname_);
  }
  clear_has_msgname();
}
inline const ::std::string& StatusUpdate::msgname() const {
  return *msgname_;
}
inline void StatusUpdate::set_msgname(const ::std::string& value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void StatusUpdate::set_msgname(const char* value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void StatusUpdate::set_msgname(const char* value, size_t size) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* StatusUpdate::mutable_msgname() {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string(*_default_msgname_);
  }
  return msgname_;
}
inline ::std::string* StatusUpdate::release_msgname() {
  clear_has_msgname();
  if (msgname_ == _default_msgname_) {
    return NULL;
  } else {
    ::std::string* temp = msgname_;
    msgname_ = const_cast< ::std::string*>(_default_msgname_);
    return temp;
  }
}
inline void StatusUpdate::set_allocated_msgname(::std::string* msgname) {
  if (msgname_ != _default_msgname_) {
    delete msgname_;
  }
  if (msgname) {
    set_has_msgname();
    msgname_ = msgname;
  } else {
    clear_has_msgname();
    msgname_ = const_cast< ::std::string*>(_default_msgname_);
  }
}

// optional float rf_freq = 2;
inline bool StatusUpdate::has_rf_freq() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void StatusUpdate::set_has_rf_freq() {
  _has_bits_[0] |= 0x00000002u;
}
inline void StatusUpdate::clear_has_rf_freq() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void StatusUpdate::clear_rf_freq() {
  rf_freq_ = 0;
  clear_has_rf_freq();
}
inline float StatusUpdate::rf_freq() const {
  return rf_freq_;
}
inline void StatusUpdate::set_rf_freq(float value) {
  set_has_rf_freq();
  rf_freq_ = value;
}

// optional bool spectral_inv = 3 [default = false];
inline bool StatusUpdate::has_spectral_inv() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void StatusUpdate::set_has_spectral_inv() {
  _has_bits_[0] |= 0x00000004u;
}
inline void StatusUpdate::clear_has_spectral_inv() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void StatusUpdate::clear_spectral_inv() {
  spectral_inv_ = false;
  clear_has_spectral_inv();
}
inline bool StatusUpdate::spectral_inv() const {
  return spectral_inv_;
}
inline void StatusUpdate::set_spectral_inv(bool value) {
  set_has_spectral_inv();
  spectral_inv_ = value;
}

// optional bool activated = 4 [default = false];
inline bool StatusUpdate::has_activated() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void StatusUpdate::set_has_activated() {
  _has_bits_[0] |= 0x00000008u;
}
inline void StatusUpdate::clear_has_activated() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void StatusUpdate::clear_activated() {
  activated_ = false;
  clear_has_activated();
}
inline bool StatusUpdate::activated() const {
  return activated_;
}
inline void StatusUpdate::set_activated(bool value) {
  set_has_activated();
  activated_ = value;
}

// optional float if_freq = 5 [default = 160];
inline bool StatusUpdate::has_if_freq() const {
  return (_has_bits_[0] & 0x00000010u) != 0;
}
inline void StatusUpdate::set_has_if_freq() {
  _has_bits_[0] |= 0x00000010u;
}
inline void StatusUpdate::clear_has_if_freq() {
  _has_bits_[0] &= ~0x00000010u;
}
inline void StatusUpdate::clear_if_freq() {
  if_freq_ = 160;
  clear_has_if_freq();
}
inline float StatusUpdate::if_freq() const {
  return if_freq_;
}
inline void StatusUpdate::set_if_freq(float value) {
  set_has_if_freq();
  if_freq_ = value;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace settings_exif_msg

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_SettingsExternalIF_2eproto__INCLUDED
