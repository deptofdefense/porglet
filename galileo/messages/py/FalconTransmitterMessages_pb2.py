# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FalconTransmitterMessages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FalconTransmitterMessages.proto',
  package='falcon_transmitter_msg',
  serialized_pb='\n\x1f\x46\x61lconTransmitterMessages.proto\x12\x16\x66\x61lcon_transmitter_msg\"\xca\x02\n\x12TransmitterRequest\x12$\n\x07msgName\x18\x01 \x01(\t:\x13TRANSMITTER_REQUEST\x12\r\n\x05resID\x18\x02 \x01(\t\x12\r\n\x05\x61ppID\x18\x03 \x01(\x05\x12\x41\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x31.falcon_transmitter_msg.TransmitterRequest.Action\x12\x45\n\x08property\x18\x05 \x01(\x0e\x32\x33.falcon_transmitter_msg.TransmitterRequest.Property\x12\r\n\x05value\x18\x06 \x01(\x02\"\x1a\n\x06\x41\x63tion\x12\x07\n\x03SET\x10\x00\x12\x07\n\x03GET\x10\x01\";\n\x08Property\x12\r\n\tFREQUENCY\x10\x00\x12\r\n\tBANDWIDTH\x10\x01\x12\x08\n\x04GAIN\x10\x02\x12\x07\n\x03REF\x10\x03\"\xb8\x02\n\x13TransmitterResponse\x12%\n\x07msgName\x18\x01 \x01(\t:\x14TRANSMITTER_RESPONSE\x12\r\n\x05resID\x18\x02 \x01(\t\x12\r\n\x05\x61ppID\x18\x03 \x01(\x05\x12\x42\n\x06status\x18\x04 \x01(\x0e\x32\x32.falcon_transmitter_msg.TransmitterResponse.Status\x12\x45\n\x08property\x18\x05 \x01(\x0e\x32\x33.falcon_transmitter_msg.TransmitterRequest.Property\x12\r\n\x05value\x18\x06 \x01(\x02\"B\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x12\x10\n\x0c\x44ISCONNECTED\x10\x02\x12\x0f\n\x0bPERMISSIONS\x10\x03\"\xba\x01\n\x11UniqueTXIDRequest\x12$\n\x07msgName\x18\x01 \x01(\t:\x13UNIQUE_TXID_REQUEST\x12\r\n\x05resID\x18\x02 \x01(\t\x12\x45\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x30.falcon_transmitter_msg.UniqueTXIDRequest.Action:\x03GET\x12\r\n\x05value\x18\x04 \x01(\t\"\x1a\n\x06\x41\x63tion\x12\x07\n\x03SET\x10\x00\x12\x07\n\x03GET\x10\x01\"Y\n\x12UniqueTXIDResponse\x12%\n\x07msgName\x18\x01 \x01(\t:\x14UNIQUE_TXID_RESPONSE\x12\r\n\x05resID\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"C\n\x16TransmitterInfoRequest\x12)\n\x07msgName\x18\x01 \x01(\t:\x18TRANSMITTER_INFO_REQUEST\"\xa6\x01\n\x17TransmitterInfoResponse\x12*\n\x07msgName\x18\x01 \x01(\t:\x19TRANSMITTER_INFO_RESPONSE\x12\r\n\x05resID\x18\x02 \x01(\t\x12\x0b\n\x03ntp\x18\x03 \x01(\t\x12\x0b\n\x03ref\x18\x04 \x01(\t\x12\x0b\n\x03pps\x18\x05 \x01(\t\x12\r\n\x05\x63omms\x18\x06 \x01(\t\x12\x0c\n\x04ping\x18\x07 \x01(\t\x12\x0c\n\x04raid\x18\x08 \x01(\tB\x15\n\x13\x66v.protos.kepsvisor')



_TRANSMITTERREQUEST_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='falcon_transmitter_msg.TransmitterRequest.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=303,
  serialized_end=329,
)

_TRANSMITTERREQUEST_PROPERTY = _descriptor.EnumDescriptor(
  name='Property',
  full_name='falcon_transmitter_msg.TransmitterRequest.Property',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FREQUENCY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANDWIDTH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAIN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REF', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=331,
  serialized_end=390,
)

_TRANSMITTERRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='falcon_transmitter_msg.TransmitterResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSIONS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=639,
  serialized_end=705,
)

_UNIQUETXIDREQUEST_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='falcon_transmitter_msg.UniqueTXIDRequest.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=303,
  serialized_end=329,
)


_TRANSMITTERREQUEST = _descriptor.Descriptor(
  name='TransmitterRequest',
  full_name='falcon_transmitter_msg.TransmitterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='falcon_transmitter_msg.TransmitterRequest.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("TRANSMITTER_REQUEST", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resID', full_name='falcon_transmitter_msg.TransmitterRequest.resID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appID', full_name='falcon_transmitter_msg.TransmitterRequest.appID', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='falcon_transmitter_msg.TransmitterRequest.action', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='falcon_transmitter_msg.TransmitterRequest.property', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='falcon_transmitter_msg.TransmitterRequest.value', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSMITTERREQUEST_ACTION,
    _TRANSMITTERREQUEST_PROPERTY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=60,
  serialized_end=390,
)


_TRANSMITTERRESPONSE = _descriptor.Descriptor(
  name='TransmitterResponse',
  full_name='falcon_transmitter_msg.TransmitterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='falcon_transmitter_msg.TransmitterResponse.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("TRANSMITTER_RESPONSE", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resID', full_name='falcon_transmitter_msg.TransmitterResponse.resID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appID', full_name='falcon_transmitter_msg.TransmitterResponse.appID', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='falcon_transmitter_msg.TransmitterResponse.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='falcon_transmitter_msg.TransmitterResponse.property', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='falcon_transmitter_msg.TransmitterResponse.value', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSMITTERRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=393,
  serialized_end=705,
)


_UNIQUETXIDREQUEST = _descriptor.Descriptor(
  name='UniqueTXIDRequest',
  full_name='falcon_transmitter_msg.UniqueTXIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='falcon_transmitter_msg.UniqueTXIDRequest.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("UNIQUE_TXID_REQUEST", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resID', full_name='falcon_transmitter_msg.UniqueTXIDRequest.resID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='falcon_transmitter_msg.UniqueTXIDRequest.action', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='falcon_transmitter_msg.UniqueTXIDRequest.value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UNIQUETXIDREQUEST_ACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=708,
  serialized_end=894,
)


_UNIQUETXIDRESPONSE = _descriptor.Descriptor(
  name='UniqueTXIDResponse',
  full_name='falcon_transmitter_msg.UniqueTXIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='falcon_transmitter_msg.UniqueTXIDResponse.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("UNIQUE_TXID_RESPONSE", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resID', full_name='falcon_transmitter_msg.UniqueTXIDResponse.resID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='falcon_transmitter_msg.UniqueTXIDResponse.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=896,
  serialized_end=985,
)


_TRANSMITTERINFOREQUEST = _descriptor.Descriptor(
  name='TransmitterInfoRequest',
  full_name='falcon_transmitter_msg.TransmitterInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='falcon_transmitter_msg.TransmitterInfoRequest.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("TRANSMITTER_INFO_REQUEST", "utf-8"),
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
  serialized_start=987,
  serialized_end=1054,
)


_TRANSMITTERINFORESPONSE = _descriptor.Descriptor(
  name='TransmitterInfoResponse',
  full_name='falcon_transmitter_msg.TransmitterInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='falcon_transmitter_msg.TransmitterInfoResponse.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("TRANSMITTER_INFO_RESPONSE", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resID', full_name='falcon_transmitter_msg.TransmitterInfoResponse.resID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ntp', full_name='falcon_transmitter_msg.TransmitterInfoResponse.ntp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ref', full_name='falcon_transmitter_msg.TransmitterInfoResponse.ref', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pps', full_name='falcon_transmitter_msg.TransmitterInfoResponse.pps', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comms', full_name='falcon_transmitter_msg.TransmitterInfoResponse.comms', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='falcon_transmitter_msg.TransmitterInfoResponse.ping', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid', full_name='falcon_transmitter_msg.TransmitterInfoResponse.raid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1057,
  serialized_end=1223,
)

_TRANSMITTERREQUEST.fields_by_name['action'].enum_type = _TRANSMITTERREQUEST_ACTION
_TRANSMITTERREQUEST.fields_by_name['property'].enum_type = _TRANSMITTERREQUEST_PROPERTY
_TRANSMITTERREQUEST_ACTION.containing_type = _TRANSMITTERREQUEST;
_TRANSMITTERREQUEST_PROPERTY.containing_type = _TRANSMITTERREQUEST;
_TRANSMITTERRESPONSE.fields_by_name['status'].enum_type = _TRANSMITTERRESPONSE_STATUS
_TRANSMITTERRESPONSE.fields_by_name['property'].enum_type = _TRANSMITTERREQUEST_PROPERTY
_TRANSMITTERRESPONSE_STATUS.containing_type = _TRANSMITTERRESPONSE;
_UNIQUETXIDREQUEST.fields_by_name['action'].enum_type = _UNIQUETXIDREQUEST_ACTION
_UNIQUETXIDREQUEST_ACTION.containing_type = _UNIQUETXIDREQUEST;
DESCRIPTOR.message_types_by_name['TransmitterRequest'] = _TRANSMITTERREQUEST
DESCRIPTOR.message_types_by_name['TransmitterResponse'] = _TRANSMITTERRESPONSE
DESCRIPTOR.message_types_by_name['UniqueTXIDRequest'] = _UNIQUETXIDREQUEST
DESCRIPTOR.message_types_by_name['UniqueTXIDResponse'] = _UNIQUETXIDRESPONSE
DESCRIPTOR.message_types_by_name['TransmitterInfoRequest'] = _TRANSMITTERINFOREQUEST
DESCRIPTOR.message_types_by_name['TransmitterInfoResponse'] = _TRANSMITTERINFORESPONSE

class TransmitterRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSMITTERREQUEST

  # @@protoc_insertion_point(class_scope:falcon_transmitter_msg.TransmitterRequest)

class TransmitterResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSMITTERRESPONSE

  # @@protoc_insertion_point(class_scope:falcon_transmitter_msg.TransmitterResponse)

class UniqueTXIDRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNIQUETXIDREQUEST

  # @@protoc_insertion_point(class_scope:falcon_transmitter_msg.UniqueTXIDRequest)

class UniqueTXIDResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNIQUETXIDRESPONSE

  # @@protoc_insertion_point(class_scope:falcon_transmitter_msg.UniqueTXIDResponse)

class TransmitterInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSMITTERINFOREQUEST

  # @@protoc_insertion_point(class_scope:falcon_transmitter_msg.TransmitterInfoRequest)

class TransmitterInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSMITTERINFORESPONSE

  # @@protoc_insertion_point(class_scope:falcon_transmitter_msg.TransmitterInfoResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\023fv.protos.kepsvisor')
# @@protoc_insertion_point(module_scope)
