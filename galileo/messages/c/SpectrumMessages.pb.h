// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: SpectrumMessages.proto

#ifndef PROTOBUF_SpectrumMessages_2eproto__INCLUDED
#define PROTOBUF_SpectrumMessages_2eproto__INCLUDED

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
#include "ServiceInfrastructureCommon.pb.h"
// @@protoc_insertion_point(includes)

namespace fv {
namespace spectrums {
namespace protos {
namespace SpectrumsProtos {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_SpectrumMessages_2eproto();
void protobuf_AssignDesc_SpectrumMessages_2eproto();
void protobuf_ShutdownFile_SpectrumMessages_2eproto();

class SpectrumTopic;
class Spectrum;

// ===================================================================

class SpectrumTopic : public ::google::protobuf::Message {
 public:
  SpectrumTopic();
  virtual ~SpectrumTopic();

  SpectrumTopic(const SpectrumTopic& from);

  inline SpectrumTopic& operator=(const SpectrumTopic& from) {
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
  static const SpectrumTopic& default_instance();

  void Swap(SpectrumTopic* other);

  // implements Message ----------------------------------------------

  SpectrumTopic* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const SpectrumTopic& from);
  void MergeFrom(const SpectrumTopic& from);
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

  // optional .service_infrastructure.Header header = 100;
  inline bool has_header() const;
  inline void clear_header();
  static const int kHeaderFieldNumber = 100;
  inline const ::service_infrastructure::Header& header() const;
  inline ::service_infrastructure::Header* mutable_header();
  inline ::service_infrastructure::Header* release_header();
  inline void set_allocated_header(::service_infrastructure::Header* header);

  // optional .fv.spectrums.protos.SpectrumsProtos.Spectrum spectrum = 1;
  inline bool has_spectrum() const;
  inline void clear_spectrum();
  static const int kSpectrumFieldNumber = 1;
  inline const ::fv::spectrums::protos::SpectrumsProtos::Spectrum& spectrum() const;
  inline ::fv::spectrums::protos::SpectrumsProtos::Spectrum* mutable_spectrum();
  inline ::fv::spectrums::protos::SpectrumsProtos::Spectrum* release_spectrum();
  inline void set_allocated_spectrum(::fv::spectrums::protos::SpectrumsProtos::Spectrum* spectrum);

  // @@protoc_insertion_point(class_scope:fv.spectrums.protos.SpectrumsProtos.SpectrumTopic)
 private:
  inline void set_has_header();
  inline void clear_has_header();
  inline void set_has_spectrum();
  inline void clear_has_spectrum();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::service_infrastructure::Header* header_;
  ::fv::spectrums::protos::SpectrumsProtos::Spectrum* spectrum_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(2 + 31) / 32];

  friend void  protobuf_AddDesc_SpectrumMessages_2eproto();
  friend void protobuf_AssignDesc_SpectrumMessages_2eproto();
  friend void protobuf_ShutdownFile_SpectrumMessages_2eproto();

  void InitAsDefaultInstance();
  static SpectrumTopic* default_instance_;
};
// -------------------------------------------------------------------

class Spectrum : public ::google::protobuf::Message {
 public:
  Spectrum();
  virtual ~Spectrum();

  Spectrum(const Spectrum& from);

  inline Spectrum& operator=(const Spectrum& from) {
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
  static const Spectrum& default_instance();

  void Swap(Spectrum* other);

  // implements Message ----------------------------------------------

  Spectrum* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Spectrum& from);
  void MergeFrom(const Spectrum& from);
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

  // optional string msgName = 1 [default = "SPECTRUM"];
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

  // optional string hostname = 2 [default = "localhost"];
  inline bool has_hostname() const;
  inline void clear_hostname();
  static const int kHostnameFieldNumber = 2;
  inline const ::std::string& hostname() const;
  inline void set_hostname(const ::std::string& value);
  inline void set_hostname(const char* value);
  inline void set_hostname(const char* value, size_t size);
  inline ::std::string* mutable_hostname();
  inline ::std::string* release_hostname();
  inline void set_allocated_hostname(::std::string* hostname);

  // optional float wholesec = 3 [default = 0];
  inline bool has_wholesec() const;
  inline void clear_wholesec();
  static const int kWholesecFieldNumber = 3;
  inline float wholesec() const;
  inline void set_wholesec(float value);

  // optional float fracsec = 4 [default = 0];
  inline bool has_fracsec() const;
  inline void clear_fracsec();
  static const int kFracsecFieldNumber = 4;
  inline float fracsec() const;
  inline void set_fracsec(float value);

  // optional int32 framelength = 5 [default = 2048];
  inline bool has_framelength() const;
  inline void clear_framelength();
  static const int kFramelengthFieldNumber = 5;
  inline ::google::protobuf::int32 framelength() const;
  inline void set_framelength(::google::protobuf::int32 value);

  // optional float minfreq = 6;
  inline bool has_minfreq() const;
  inline void clear_minfreq();
  static const int kMinfreqFieldNumber = 6;
  inline float minfreq() const;
  inline void set_minfreq(float value);

  // optional float binres = 7;
  inline bool has_binres() const;
  inline void clear_binres();
  static const int kBinresFieldNumber = 7;
  inline float binres() const;
  inline void set_binres(float value);

  // optional int32 channel = 8;
  inline bool has_channel() const;
  inline void clear_channel();
  static const int kChannelFieldNumber = 8;
  inline ::google::protobuf::int32 channel() const;
  inline void set_channel(::google::protobuf::int32 value);

  // repeated float binvalue = 9;
  inline int binvalue_size() const;
  inline void clear_binvalue();
  static const int kBinvalueFieldNumber = 9;
  inline float binvalue(int index) const;
  inline void set_binvalue(int index, float value);
  inline void add_binvalue(float value);
  inline const ::google::protobuf::RepeatedField< float >&
      binvalue() const;
  inline ::google::protobuf::RepeatedField< float >*
      mutable_binvalue();

  // @@protoc_insertion_point(class_scope:fv.spectrums.protos.SpectrumsProtos.Spectrum)
 private:
  inline void set_has_msgname();
  inline void clear_has_msgname();
  inline void set_has_hostname();
  inline void clear_has_hostname();
  inline void set_has_wholesec();
  inline void clear_has_wholesec();
  inline void set_has_fracsec();
  inline void clear_has_fracsec();
  inline void set_has_framelength();
  inline void clear_has_framelength();
  inline void set_has_minfreq();
  inline void clear_has_minfreq();
  inline void set_has_binres();
  inline void clear_has_binres();
  inline void set_has_channel();
  inline void clear_has_channel();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::std::string* msgname_;
  static ::std::string* _default_msgname_;
  ::std::string* hostname_;
  static ::std::string* _default_hostname_;
  float wholesec_;
  float fracsec_;
  ::google::protobuf::int32 framelength_;
  float minfreq_;
  float binres_;
  ::google::protobuf::int32 channel_;
  ::google::protobuf::RepeatedField< float > binvalue_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(9 + 31) / 32];

  friend void  protobuf_AddDesc_SpectrumMessages_2eproto();
  friend void protobuf_AssignDesc_SpectrumMessages_2eproto();
  friend void protobuf_ShutdownFile_SpectrumMessages_2eproto();

  void InitAsDefaultInstance();
  static Spectrum* default_instance_;
};
// ===================================================================


// ===================================================================

// SpectrumTopic

// optional .service_infrastructure.Header header = 100;
inline bool SpectrumTopic::has_header() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void SpectrumTopic::set_has_header() {
  _has_bits_[0] |= 0x00000001u;
}
inline void SpectrumTopic::clear_has_header() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void SpectrumTopic::clear_header() {
  if (header_ != NULL) header_->::service_infrastructure::Header::Clear();
  clear_has_header();
}
inline const ::service_infrastructure::Header& SpectrumTopic::header() const {
  return header_ != NULL ? *header_ : *default_instance_->header_;
}
inline ::service_infrastructure::Header* SpectrumTopic::mutable_header() {
  set_has_header();
  if (header_ == NULL) header_ = new ::service_infrastructure::Header;
  return header_;
}
inline ::service_infrastructure::Header* SpectrumTopic::release_header() {
  clear_has_header();
  ::service_infrastructure::Header* temp = header_;
  header_ = NULL;
  return temp;
}
inline void SpectrumTopic::set_allocated_header(::service_infrastructure::Header* header) {
  delete header_;
  header_ = header;
  if (header) {
    set_has_header();
  } else {
    clear_has_header();
  }
}

// optional .fv.spectrums.protos.SpectrumsProtos.Spectrum spectrum = 1;
inline bool SpectrumTopic::has_spectrum() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void SpectrumTopic::set_has_spectrum() {
  _has_bits_[0] |= 0x00000002u;
}
inline void SpectrumTopic::clear_has_spectrum() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void SpectrumTopic::clear_spectrum() {
  if (spectrum_ != NULL) spectrum_->::fv::spectrums::protos::SpectrumsProtos::Spectrum::Clear();
  clear_has_spectrum();
}
inline const ::fv::spectrums::protos::SpectrumsProtos::Spectrum& SpectrumTopic::spectrum() const {
  return spectrum_ != NULL ? *spectrum_ : *default_instance_->spectrum_;
}
inline ::fv::spectrums::protos::SpectrumsProtos::Spectrum* SpectrumTopic::mutable_spectrum() {
  set_has_spectrum();
  if (spectrum_ == NULL) spectrum_ = new ::fv::spectrums::protos::SpectrumsProtos::Spectrum;
  return spectrum_;
}
inline ::fv::spectrums::protos::SpectrumsProtos::Spectrum* SpectrumTopic::release_spectrum() {
  clear_has_spectrum();
  ::fv::spectrums::protos::SpectrumsProtos::Spectrum* temp = spectrum_;
  spectrum_ = NULL;
  return temp;
}
inline void SpectrumTopic::set_allocated_spectrum(::fv::spectrums::protos::SpectrumsProtos::Spectrum* spectrum) {
  delete spectrum_;
  spectrum_ = spectrum;
  if (spectrum) {
    set_has_spectrum();
  } else {
    clear_has_spectrum();
  }
}

// -------------------------------------------------------------------

// Spectrum

// optional string msgName = 1 [default = "SPECTRUM"];
inline bool Spectrum::has_msgname() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Spectrum::set_has_msgname() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Spectrum::clear_has_msgname() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Spectrum::clear_msgname() {
  if (msgname_ != _default_msgname_) {
    msgname_->assign(*_default_msgname_);
  }
  clear_has_msgname();
}
inline const ::std::string& Spectrum::msgname() const {
  return *msgname_;
}
inline void Spectrum::set_msgname(const ::std::string& value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void Spectrum::set_msgname(const char* value) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(value);
}
inline void Spectrum::set_msgname(const char* value, size_t size) {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string;
  }
  msgname_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Spectrum::mutable_msgname() {
  set_has_msgname();
  if (msgname_ == _default_msgname_) {
    msgname_ = new ::std::string(*_default_msgname_);
  }
  return msgname_;
}
inline ::std::string* Spectrum::release_msgname() {
  clear_has_msgname();
  if (msgname_ == _default_msgname_) {
    return NULL;
  } else {
    ::std::string* temp = msgname_;
    msgname_ = const_cast< ::std::string*>(_default_msgname_);
    return temp;
  }
}
inline void Spectrum::set_allocated_msgname(::std::string* msgname) {
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

// optional string hostname = 2 [default = "localhost"];
inline bool Spectrum::has_hostname() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Spectrum::set_has_hostname() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Spectrum::clear_has_hostname() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Spectrum::clear_hostname() {
  if (hostname_ != _default_hostname_) {
    hostname_->assign(*_default_hostname_);
  }
  clear_has_hostname();
}
inline const ::std::string& Spectrum::hostname() const {
  return *hostname_;
}
inline void Spectrum::set_hostname(const ::std::string& value) {
  set_has_hostname();
  if (hostname_ == _default_hostname_) {
    hostname_ = new ::std::string;
  }
  hostname_->assign(value);
}
inline void Spectrum::set_hostname(const char* value) {
  set_has_hostname();
  if (hostname_ == _default_hostname_) {
    hostname_ = new ::std::string;
  }
  hostname_->assign(value);
}
inline void Spectrum::set_hostname(const char* value, size_t size) {
  set_has_hostname();
  if (hostname_ == _default_hostname_) {
    hostname_ = new ::std::string;
  }
  hostname_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Spectrum::mutable_hostname() {
  set_has_hostname();
  if (hostname_ == _default_hostname_) {
    hostname_ = new ::std::string(*_default_hostname_);
  }
  return hostname_;
}
inline ::std::string* Spectrum::release_hostname() {
  clear_has_hostname();
  if (hostname_ == _default_hostname_) {
    return NULL;
  } else {
    ::std::string* temp = hostname_;
    hostname_ = const_cast< ::std::string*>(_default_hostname_);
    return temp;
  }
}
inline void Spectrum::set_allocated_hostname(::std::string* hostname) {
  if (hostname_ != _default_hostname_) {
    delete hostname_;
  }
  if (hostname) {
    set_has_hostname();
    hostname_ = hostname;
  } else {
    clear_has_hostname();
    hostname_ = const_cast< ::std::string*>(_default_hostname_);
  }
}

// optional float wholesec = 3 [default = 0];
inline bool Spectrum::has_wholesec() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Spectrum::set_has_wholesec() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Spectrum::clear_has_wholesec() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Spectrum::clear_wholesec() {
  wholesec_ = 0;
  clear_has_wholesec();
}
inline float Spectrum::wholesec() const {
  return wholesec_;
}
inline void Spectrum::set_wholesec(float value) {
  set_has_wholesec();
  wholesec_ = value;
}

// optional float fracsec = 4 [default = 0];
inline bool Spectrum::has_fracsec() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void Spectrum::set_has_fracsec() {
  _has_bits_[0] |= 0x00000008u;
}
inline void Spectrum::clear_has_fracsec() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void Spectrum::clear_fracsec() {
  fracsec_ = 0;
  clear_has_fracsec();
}
inline float Spectrum::fracsec() const {
  return fracsec_;
}
inline void Spectrum::set_fracsec(float value) {
  set_has_fracsec();
  fracsec_ = value;
}

// optional int32 framelength = 5 [default = 2048];
inline bool Spectrum::has_framelength() const {
  return (_has_bits_[0] & 0x00000010u) != 0;
}
inline void Spectrum::set_has_framelength() {
  _has_bits_[0] |= 0x00000010u;
}
inline void Spectrum::clear_has_framelength() {
  _has_bits_[0] &= ~0x00000010u;
}
inline void Spectrum::clear_framelength() {
  framelength_ = 2048;
  clear_has_framelength();
}
inline ::google::protobuf::int32 Spectrum::framelength() const {
  return framelength_;
}
inline void Spectrum::set_framelength(::google::protobuf::int32 value) {
  set_has_framelength();
  framelength_ = value;
}

// optional float minfreq = 6;
inline bool Spectrum::has_minfreq() const {
  return (_has_bits_[0] & 0x00000020u) != 0;
}
inline void Spectrum::set_has_minfreq() {
  _has_bits_[0] |= 0x00000020u;
}
inline void Spectrum::clear_has_minfreq() {
  _has_bits_[0] &= ~0x00000020u;
}
inline void Spectrum::clear_minfreq() {
  minfreq_ = 0;
  clear_has_minfreq();
}
inline float Spectrum::minfreq() const {
  return minfreq_;
}
inline void Spectrum::set_minfreq(float value) {
  set_has_minfreq();
  minfreq_ = value;
}

// optional float binres = 7;
inline bool Spectrum::has_binres() const {
  return (_has_bits_[0] & 0x00000040u) != 0;
}
inline void Spectrum::set_has_binres() {
  _has_bits_[0] |= 0x00000040u;
}
inline void Spectrum::clear_has_binres() {
  _has_bits_[0] &= ~0x00000040u;
}
inline void Spectrum::clear_binres() {
  binres_ = 0;
  clear_has_binres();
}
inline float Spectrum::binres() const {
  return binres_;
}
inline void Spectrum::set_binres(float value) {
  set_has_binres();
  binres_ = value;
}

// optional int32 channel = 8;
inline bool Spectrum::has_channel() const {
  return (_has_bits_[0] & 0x00000080u) != 0;
}
inline void Spectrum::set_has_channel() {
  _has_bits_[0] |= 0x00000080u;
}
inline void Spectrum::clear_has_channel() {
  _has_bits_[0] &= ~0x00000080u;
}
inline void Spectrum::clear_channel() {
  channel_ = 0;
  clear_has_channel();
}
inline ::google::protobuf::int32 Spectrum::channel() const {
  return channel_;
}
inline void Spectrum::set_channel(::google::protobuf::int32 value) {
  set_has_channel();
  channel_ = value;
}

// repeated float binvalue = 9;
inline int Spectrum::binvalue_size() const {
  return binvalue_.size();
}
inline void Spectrum::clear_binvalue() {
  binvalue_.Clear();
}
inline float Spectrum::binvalue(int index) const {
  return binvalue_.Get(index);
}
inline void Spectrum::set_binvalue(int index, float value) {
  binvalue_.Set(index, value);
}
inline void Spectrum::add_binvalue(float value) {
  binvalue_.Add(value);
}
inline const ::google::protobuf::RepeatedField< float >&
Spectrum::binvalue() const {
  return binvalue_;
}
inline ::google::protobuf::RepeatedField< float >*
Spectrum::mutable_binvalue() {
  return &binvalue_;
}


// @@protoc_insertion_point(namespace_scope)

}  // namespace SpectrumsProtos
}  // namespace protos
}  // namespace spectrums
}  // namespace fv

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_SpectrumMessages_2eproto__INCLUDED
