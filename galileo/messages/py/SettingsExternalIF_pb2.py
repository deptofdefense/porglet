# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SettingsExternalIF.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SettingsExternalIF.proto',
  package='settings_exif_msg',
  serialized_pb='\n\x18SettingsExternalIF.proto\x12\x11settings_exif_msg\"E\n\rRequestStatus\x12\x1f\n\x07msgName\x18\x01 \x01(\t:\x0eREQUEST_STATUS\x12\x13\n\x08msg_type\x18\x02 \x01(\x05:\x01\x30\"\x8c\x01\n\x0cStatusUpdate\x12\x1e\n\x07msgName\x18\x01 \x01(\t:\rSTATUS_UPDATE\x12\x0f\n\x07rf_freq\x18\x02 \x01(\x02\x12\x1b\n\x0cspectral_inv\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x18\n\tactivated\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x07if_freq\x18\x05 \x01(\x02:\x03\x31\x36\x30\x42\x15\n\x13\x66v.protos.kepsvisor')




_REQUESTSTATUS = _descriptor.Descriptor(
  name='RequestStatus',
  full_name='settings_exif_msg.RequestStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='settings_exif_msg.RequestStatus.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("REQUEST_STATUS", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='settings_exif_msg.RequestStatus.msg_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=47,
  serialized_end=116,
)


_STATUSUPDATE = _descriptor.Descriptor(
  name='StatusUpdate',
  full_name='settings_exif_msg.StatusUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='settings_exif_msg.StatusUpdate.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("STATUS_UPDATE", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rf_freq', full_name='settings_exif_msg.StatusUpdate.rf_freq', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spectral_inv', full_name='settings_exif_msg.StatusUpdate.spectral_inv', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activated', full_name='settings_exif_msg.StatusUpdate.activated', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='if_freq', full_name='settings_exif_msg.StatusUpdate.if_freq', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=160,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=119,
  serialized_end=259,
)

DESCRIPTOR.message_types_by_name['RequestStatus'] = _REQUESTSTATUS
DESCRIPTOR.message_types_by_name['StatusUpdate'] = _STATUSUPDATE

class RequestStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTSTATUS

  # @@protoc_insertion_point(class_scope:settings_exif_msg.RequestStatus)

class StatusUpdate(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATUSUPDATE

  # @@protoc_insertion_point(class_scope:settings_exif_msg.StatusUpdate)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\023fv.protos.kepsvisor')
# @@protoc_insertion_point(module_scope)
