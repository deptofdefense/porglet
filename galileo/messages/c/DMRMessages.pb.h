// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: DMRMessages.proto

#ifndef PROTOBUF_DMRMessages_2eproto__INCLUDED
#define PROTOBUF_DMRMessages_2eproto__INCLUDED

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

namespace fv {
namespace tb {
namespace protos {
namespace DMRProtos {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_DMRMessages_2eproto();
void protobuf_AssignDesc_DMRMessages_2eproto();
void protobuf_ShutdownFile_DMRMessages_2eproto();

class DmrMeta;

// ===================================================================

class DmrMeta : public ::google::protobuf::Message {
 public:
  DmrMeta();
  virtual ~DmrMeta();

  DmrMeta(const DmrMeta& from);

  inline DmrMeta& operator=(const DmrMeta& from) {
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
  static const DmrMeta& default_instance();

  void Swap(DmrMeta* other);

  // implements Message ----------------------------------------------

  DmrMeta* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const DmrMeta& from);
  void MergeFrom(const DmrMeta& from);
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

  // optional string msgName = 1 [default = "DMRMETA"];
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

  // optional double cffreq = 2;
  inline bool has_cffreq() const;
  inline void clear_cffreq();
  static const int kCffreqFieldNumber = 2;
  inline double cffreq() const;
  inline void set_cffreq(double value);

  // optional string srcType = 3;
  inline bool has_srctype() const;
  inline void clear_srctype();
  static const int kSrcTypeFieldNumber = 3;
  inline const ::std::string& srctype() const;
  inline void set_srctype(const ::std::string& value);
  inline void set_srctype(const char* value);
  inline void set_srctype(const char* value, size_t size);
  inline ::std::string* mutable_srctype();
  inline ::std::string* release_srctype();
  inline void set_allocated_srctype(::std::string* srctype);

  // optional int32 srcAddr = 4;
  inline bool has_srcaddr() const;
  inline void clear_srcaddr();
  static const int kSrcAddrFieldNumber = 4;
  inline ::google::protobuf::int32 srcaddr() const;
  inline void set_srcaddr(::google::protobuf::int32 value);

  // optional string destType = 5;
  inline bool has_desttype() const;
  inline void clear_desttype();
  static const int kDestTypeFieldNumber = 5;
  inline const ::std::string& desttype() const;
  inline void set_desttype(const ::std::string& value);
  inline void set_desttype(const char* value);
  inline void set_desttype(const char* value, size_t size);
  inline ::std::string* mutable_desttype();
  inline ::std::string* release_desttype();
  inline void set_allocated_desttype(::std::string* desttype);

  // optional int32 destAddr = 6;
  inline bool has_destaddr() const;
  inline void clear_destaddr();
  static const int kDestAddrFieldNumber = 6;
  inline ::google::protobuf::int32 destaddr() const;
  inline void set_destaddr(::google::protobuf::int32 value);

  // optional int32 timeSlot = 7;
  inline bool has_timeslot() const;
  inline void clear_timeslot();
  static const int kTimeSlotFieldNumber = 7;
  inline ::google::protobuf::int32 timeslot() const;
  inline void set_timeslot(::google::protobuf::int32 value);

  // optional string callType = 8;
  inline bool has_calltype() const;
  inline void clear_calltype();
  static const int kCallTypeFieldNumber = 8;
  inline const ::std::string& calltype() const;
  inline void set_calltype(const ::std::string& value);
  inline void set_calltype(const char* value);
  inline void set_calltype(const char* value, size_t size);
  inline ::std::string* mutable_calltype();
  inline ::std::string* release_calltype();
  inline void set_allocated_calltype(::std::string* calltype);

  // optional int32 colorCode = 9;
  inline bool has_colorcode() const;
  inline void clear_colorcode();
  static const int kColorCodeFieldNumber = 9;
  inline ::google::protobuf::int32 colorcode() const;
  inline void set_colorcode(::google::protobuf::int32 value);

  // optional string text = 10 [default = "None"];
  inline bool has_text() const;
  inline void clear_text();
  static const int kTextFieldNumber = 10;
  inline const ::std::string& text() const;
  inline void set_text(const ::std::string& value);
  inline void set_text(const char* value);
  inline void set_text(const char* value, size_t size);
  inline ::std::string* mutable_text();
  inline ::std::string* release_text();
  inline void set_allocated_text(::std::string* text);

  // optional string geo = 11 [default = "None"];
  inline bool has_geo() const;
  inline void clear_geo();
  static const int kGeoFieldNumber = 11;
  inline const ::std::string& geo() const;
  inline void set_geo(const ::std::string& value);
  inline void set_geo(const char* value);
  inline void set_geo(const char* value, size_t size);
  inline ::std::string* mutable_geo();
  inline ::std::string* release_geo();
  inline void set_allocated_geo(::std::string* geo);

  // @@protoc_insertion_point(class_scope:fv.tb.protos.DMRProtos.DmrMeta)
 private:
  inline void set_has_msgname();
  inline void clear_has_msgname();
  inline void set_has_cffreq();
  inline void clear_has_cffreq();
  inline void set_has_srctype();
  inline void clear_has_srctype();
  inline void set_has_srcaddr();
  inline void clear_has_srcaddr();
  inline void set_has_desttype();
  inline void clear_has_desttype();
  inline void set_has_destaddr();
  inline void clear_has_destaddr();
  inline void set_has_timeslot();
  inline void clear_has_timeslot();
  inline void set_has_calltype();
  inline void clear_has_calltype();
  inline void set_has_colorcode();
  inline void clear_has_colorcode();
  inline void set_has_text();
  inline void clear_has_text();
  inline void set_has_geo();
  inline void clear_has_geo();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::std::string* msgname_;
  static ::std::string* _default_msgname_;
  double cffreq_;
  ::std::string* srctype_;
  ::std::string* desttype_;
  ::google::protobuf::int32 srcaddr_;
  ::google::protobuf::int32 destaddr_;
  ::std::string* calltype_;
  ::google::protobuf::int32 timeslot_;
  ::google::protobuf::int32 colorcode_;
  ::std::string* text_;
  static ::std::string* _default_text_;
  ::std::string* geo_;
  static ::std::string* _default_geo_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(11 + 31) / 32];

  friend void  protobuf_AddDesc_DMRMessages_2eproto();
  friend void protobuf_AssignDesc_DMRMessages_2eproto();
  friend void protobuf_ShutdownFile_DMRMessages_2eproto();

  void InitAsDefaultInstance();
  static DmrMeta* default_instance_;
};
// ===================================================================


// ===================================================================

// DmrMeta

// optional string msgName = 1 [default = "DMRMETA"];
inline bool DmrMeta::has_msgname() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void DmrMeta::set_has_msgname() {
  _has_bits_[0] |= 0x00000001u;
}
inline void DmrMeta::clear_has_msgname() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void DmrMeta::clear_msgname() {
  if (msgname_ != _default_msgname_) {
    msgname_->assign(*_default_msgname_);
  }
  clear_has_msgname();
}
inline const ::std::string& DmrMeta::msgname() const {
  return *msgname_;
}
inline void DmrMeta::set_msgname(const ::std::string& value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void DmrMeta::set_msgname(const char* value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void DmrMeta::set_msgname(const char* value, size_t size) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* DmrMeta::mutable_msgname() {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string(*_default_msgname_);
  }
  return msgname_;
}
inline ::std::string* DmrMeta::release_msgname() {
  clear_has_msgname();
  if (msgname_ == _default_msgname_) {
    return NULL;
  } else {
    ::std::string* temp = msgname_;
    msgname_ = const_cast< ::std::string*>(_default_msgname_);
    return temp;
  }
}
inline void DmrMeta::set_allocated_msgname(::std::string* msgname) {
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

// optional double cffreq = 2;
inline bool DmrMeta::has_cffreq() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void DmrMeta::set_has_cffreq() {
  _has_bits_[0] |= 0x00000002u;
}
inline void DmrMeta::clear_has_cffreq() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void DmrMeta::clear_cffreq() {
  cffreq_ = 0;
  clear_has_cffreq();
}
inline double DmrMeta::cffreq() const {
  return cffreq_;
}
inline void DmrMeta::set_cffreq(double value) {
  set_has_cffreq();
  cffreq_ = value;
}

// optional string srcType = 3;
inline bool DmrMeta::has_srctype() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void DmrMeta::set_has_srctype() {
  _has_bits_[0] |= 0x00000004u;
}
inline void DmrMeta::clear_has_srctype() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void DmrMeta::clear_srctype() {
  if (srctype_ != &::google::protobuf::internal::kEmptyString) {
    srctype_->clear();
  }
  clear_has_srctype();
}
inline const ::std::string& DmrMeta::srctype() const {
  return *srctype_;
}
inline void DmrMeta::set_srctype(const ::std::string& value) {
  set_has_srctype();
  if (srctype_ == &::google::protobuf::internal::kEmptyString) {
    srctype_ = new ::std::string;
  }
  srctype_->assign(value);
}
inline void DmrMeta::set_srctype(const char* value) {
  set_has_srctype();
  if (srctype_ == &::google::protobuf::internal::kEmptyString) {
    srctype_ = new ::std::string;
  }
  srctype_->assign(value);
}
inline void DmrMeta::set_srctype(const char* value, size_t size) {
  set_has_srctype();
  if (srctype_ == &::google::protobuf::internal::kEmptyString) {
    srctype_ = new ::std::string;
  }
  srctype_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* DmrMeta::mutable_srctype() {
  set_has_srctype();
  if (srctype_ == &::google::protobuf::internal::kEmptyString) {
    srctype_ = new ::std::string;
  }
  return srctype_;
}
inline ::std::string* DmrMeta::release_srctype() {
  clear_has_srctype();
  if (srctype_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = srctype_;
    srctype_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void DmrMeta::set_allocated_srctype(::std::string* srctype) {
  if (srctype_ != &::google::protobuf::internal::kEmptyString) {
    delete srctype_;
  }
  if (srctype) {
    set_has_srctype();
    srctype_ = srctype;
  } else {
    clear_has_srctype();
    srctype_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// optional int32 srcAddr = 4;
inline bool DmrMeta::has_srcaddr() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void DmrMeta::set_has_srcaddr() {
  _has_bits_[0] |= 0x00000008u;
}
inline void DmrMeta::clear_has_srcaddr() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void DmrMeta::clear_srcaddr() {
  srcaddr_ = 0;
  clear_has_srcaddr();
}
inline ::google::protobuf::int32 DmrMeta::srcaddr() const {
  return srcaddr_;
}
inline void DmrMeta::set_srcaddr(::google::protobuf::int32 value) {
  set_has_srcaddr();
  srcaddr_ = value;
}

// optional string destType = 5;
inline bool DmrMeta::has_desttype() const {
  return (_has_bits_[0] & 0x00000010u) != 0;
}
inline void DmrMeta::set_has_desttype() {
  _has_bits_[0] |= 0x00000010u;
}
inline void DmrMeta::clear_has_desttype() {
  _has_bits_[0] &= ~0x00000010u;
}
inline void DmrMeta::clear_desttype() {
  if (desttype_ != &::google::protobuf::internal::kEmptyString) {
    desttype_->clear();
  }
  clear_has_desttype();
}
inline const ::std::string& DmrMeta::desttype() const {
  return *desttype_;
}
inline void DmrMeta::set_desttype(const ::std::string& value) {
  set_has_desttype();
  if (desttype_ == &::google::protobuf::internal::kEmptyString) {
    desttype_ = new ::std::string;
  }
  desttype_->assign(value);
}
inline void DmrMeta::set_desttype(const char* value) {
  set_has_desttype();
  if (desttype_ == &::google::protobuf::internal::kEmptyString) {
    desttype_ = new ::std::string;
  }
  desttype_->assign(value);
}
inline void DmrMeta::set_desttype(const char* value, size_t size) {
  set_has_desttype();
  if (desttype_ == &::google::protobuf::internal::kEmptyString) {
    desttype_ = new ::std::string;
  }
  desttype_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* DmrMeta::mutable_desttype() {
  set_has_desttype();
  if (desttype_ == &::google::protobuf::internal::kEmptyString) {
    desttype_ = new ::std::string;
  }
  return desttype_;
}
inline ::std::string* DmrMeta::release_desttype() {
  clear_has_desttype();
  if (desttype_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = desttype_;
    desttype_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void DmrMeta::set_allocated_desttype(::std::string* desttype) {
  if (desttype_ != &::google::protobuf::internal::kEmptyString) {
    delete desttype_;
  }
  if (desttype) {
    set_has_desttype();
    desttype_ = desttype;
  } else {
    clear_has_desttype();
    desttype_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// optional int32 destAddr = 6;
inline bool DmrMeta::has_destaddr() const {
  return (_has_bits_[0] & 0x00000020u) != 0;
}
inline void DmrMeta::set_has_destaddr() {
  _has_bits_[0] |= 0x00000020u;
}
inline void DmrMeta::clear_has_destaddr() {
  _has_bits_[0] &= ~0x00000020u;
}
inline void DmrMeta::clear_destaddr() {
  destaddr_ = 0;
  clear_has_destaddr();
}
inline ::google::protobuf::int32 DmrMeta::destaddr() const {
  return destaddr_;
}
inline void DmrMeta::set_destaddr(::google::protobuf::int32 value) {
  set_has_destaddr();
  destaddr_ = value;
}

// optional int32 timeSlot = 7;
inline bool DmrMeta::has_timeslot() const {
  return (_has_bits_[0] & 0x00000040u) != 0;
}
inline void DmrMeta::set_has_timeslot() {
  _has_bits_[0] |= 0x00000040u;
}
inline void DmrMeta::clear_has_timeslot() {
  _has_bits_[0] &= ~0x00000040u;
}
inline void DmrMeta::clear_timeslot() {
  timeslot_ = 0;
  clear_has_timeslot();
}
inline ::google::protobuf::int32 DmrMeta::timeslot() const {
  return timeslot_;
}
inline void DmrMeta::set_timeslot(::google::protobuf::int32 value) {
  set_has_timeslot();
  timeslot_ = value;
}

// optional string callType = 8;
inline bool DmrMeta::has_calltype() const {
  return (_has_bits_[0] & 0x00000080u) != 0;
}
inline void DmrMeta::set_has_calltype() {
  _has_bits_[0] |= 0x00000080u;
}
inline void DmrMeta::clear_has_calltype() {
  _has_bits_[0] &= ~0x00000080u;
}
inline void DmrMeta::clear_calltype() {
  if (calltype_ != &::google::protobuf::internal::kEmptyString) {
    calltype_->clear();
  }
  clear_has_calltype();
}
inline const ::std::string& DmrMeta::calltype() const {
  return *calltype_;
}
inline void DmrMeta::set_calltype(const ::std::string& value) {
  set_has_calltype();
  if (calltype_ == &::google::protobuf::internal::kEmptyString) {
    calltype_ = new ::std::string;
  }
  calltype_->assign(value);
}
inline void DmrMeta::set_calltype(const char* value) {
  set_has_calltype();
  if (calltype_ == &::google::protobuf::internal::kEmptyString) {
    calltype_ = new ::std::string;
  }
  calltype_->assign(value);
}
inline void DmrMeta::set_calltype(const char* value, size_t size) {
  set_has_calltype();
  if (calltype_ == &::google::protobuf::internal::kEmptyString) {
    calltype_ = new ::std::string;
  }
  calltype_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* DmrMeta::mutable_calltype() {
  set_has_calltype();
  if (calltype_ == &::google::protobuf::internal::kEmptyString) {
    calltype_ = new ::std::string;
  }
  return calltype_;
}
inline ::std::string* DmrMeta::release_calltype() {
  clear_has_calltype();
  if (calltype_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = calltype_;
    calltype_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void DmrMeta::set_allocated_calltype(::std::string* calltype) {
  if (calltype_ != &::google::protobuf::internal::kEmptyString) {
    delete calltype_;
  }
  if (calltype) {
    set_has_calltype();
    calltype_ = calltype;
  } else {
    clear_has_calltype();
    calltype_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// optional int32 colorCode = 9;
inline bool DmrMeta::has_colorcode() const {
  return (_has_bits_[0] & 0x00000100u) != 0;
}
inline void DmrMeta::set_has_colorcode() {
  _has_bits_[0] |= 0x00000100u;
}
inline void DmrMeta::clear_has_colorcode() {
  _has_bits_[0] &= ~0x00000100u;
}
inline void DmrMeta::clear_colorcode() {
  colorcode_ = 0;
  clear_has_colorcode();
}
inline ::google::protobuf::int32 DmrMeta::colorcode() const {
  return colorcode_;
}
inline void DmrMeta::set_colorcode(::google::protobuf::int32 value) {
  set_has_colorcode();
  colorcode_ = value;
}

// optional string text = 10 [default = "None"];
inline bool DmrMeta::has_text() const {
  return (_has_bits_[0] & 0x00000200u) != 0;
}
inline void DmrMeta::set_has_text() {
  _has_bits_[0] |= 0x00000200u;
}
inline void DmrMeta::clear_has_text() {
  _has_bits_[0] &= ~0x00000200u;
}
inline void DmrMeta::clear_text() {
  if (text_ != _default_text_) {
    text_->assign(*_default_text_);
  }
  clear_has_text();
}
inline const ::std::string& DmrMeta::text() const {
  return *text_;
}
inline void DmrMeta::set_text(const ::std::string& value) {
  set_has_text();
  if (text_ == _default_text_) {
    text_ = new ::std::string;
  }
  text_->assign(value);
}
inline void DmrMeta::set_text(const char* value) {
  set_has_text();
  if (text_ == _default_text_) {
    text_ = new ::std::string;
  }
  text_->assign(value);
}
inline void DmrMeta::set_text(const char* value, size_t size) {
  set_has_text();
  if (text_ == _default_text_) {
    text_ = new ::std::string;
  }
  text_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* DmrMeta::mutable_text() {
  set_has_text();
  if (text_ == _default_text_) {
    text_ = new ::std::string(*_default_text_);
  }
  return text_;
}
inline ::std::string* DmrMeta::release_text() {
  clear_has_text();
  if (text_ == _default_text_) {
    return NULL;
  } else {
    ::std::string* temp = text_;
    text_ = const_cast< ::std::string*>(_default_text_);
    return temp;
  }
}
inline void DmrMeta::set_allocated_text(::std::string* text) {
  if (text_ != _default_text_) {
    delete text_;
  }
  if (text) {
    set_has_text();
    text_ = text;
  } else {
    clear_has_text();
    text_ = const_cast< ::std::string*>(_default_text_);
  }
}

// optional string geo = 11 [default = "None"];
inline bool DmrMeta::has_geo() const {
  return (_has_bits_[0] & 0x00000400u) != 0;
}
inline void DmrMeta::set_has_geo() {
  _has_bits_[0] |= 0x00000400u;
}
inline void DmrMeta::clear_has_geo() {
  _has_bits_[0] &= ~0x00000400u;
}
inline void DmrMeta::clear_geo() {
  if (geo_ != _default_geo_) {
    geo_->assign(*_default_geo_);
  }
  clear_has_geo();
}
inline const ::std::string& DmrMeta::geo() const {
  return *geo_;
}
inline void DmrMeta::set_geo(const ::std::string& value) {
  set_has_geo();
  if (geo_ == _default_geo_) {
    geo_ = new ::std::string;
  }
  geo_->assign(value);
}
inline void DmrMeta::set_geo(const char* value) {
  set_has_geo();
  if (geo_ == _default_geo_) {
    geo_ = new ::std::string;
  }
  geo_->assign(value);
}
inline void DmrMeta::set_geo(const char* value, size_t size) {
  set_has_geo();
  if (geo_ == _default_geo_) {
    geo_ = new ::std::string;
  }
  geo_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* DmrMeta::mutable_geo() {
  set_has_geo();
  if (geo_ == _default_geo_) {
    geo_ = new ::std::string(*_default_geo_);
  }
  return geo_;
}
inline ::std::string* DmrMeta::release_geo() {
  clear_has_geo();
  if (geo_ == _default_geo_) {
    return NULL;
  } else {
    ::std::string* temp = geo_;
    geo_ = const_cast< ::std::string*>(_default_geo_);
    return temp;
  }
}
inline void DmrMeta::set_allocated_geo(::std::string* geo) {
  if (geo_ != _default_geo_) {
    delete geo_;
  }
  if (geo) {
    set_has_geo();
    geo_ = geo;
  } else {
    clear_has_geo();
    geo_ = const_cast< ::std::string*>(_default_geo_);
  }
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace DMRProtos
}  // namespace protos
}  // namespace tb
}  // namespace fv

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_DMRMessages_2eproto__INCLUDED
