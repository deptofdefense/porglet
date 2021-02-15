# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DTAMFELMessages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import ThunderbirdMessages_pb2
import ServiceInfrastructureCommon_pb2
import ServiceInfrastructureExclusive_pb2
import BitMessages_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DTAMFELMessages.proto',
  package='',
  serialized_pb='\n\x15\x44TAMFELMessages.proto\x1a\x19ThunderbirdMessages.proto\x1a!ServiceInfrastructureCommon.proto\x1a$ServiceInfrastructureExclusive.proto\x1a\x11\x42itMessages.proto\"\t\n\x07RunMode\"\r\n\x0bStandbyMode\"\x10\n\x0eShutdownSystem\"\x11\n\x0fGetSystemStatus\"\x0e\n\x0cGetTrackList\"\x10\n\x0eGetTrackReport\"\x0e\n\x0cGetTrackPDWs\"\x05\n\x03\x41\x43K\"\x0e\n\x0cSystemStatus\"\x0c\n\nSystemInfo\"\xee\x01\n\x10\x44taResponseTopic\x12.\n\x06header\x18\x64 \x01(\x0b\x32\x1e.service_infrastructure.Header\x12)\n\x10\x64ta_bit_response\x18\x01 \x01(\x0b\x32\x0f.DtaBitResponse\x12)\n\x10\x64ta_track_report\x18\x02 \x01(\x0b\x32\x0f.DtaTrackReport\x12\'\n\x0f\x64ta_system_info\x18\x03 \x01(\x0b\x32\x0e.DtaSystemInfo\x12+\n\x11\x64ta_system_status\x18\x04 \x01(\x0b\x32\x10.DtaSystemStatus\"\xdd\x01\n\x0c\x44taBitReport\x12\x11\n\ttest_name\x18\x01 \x01(\t\x12(\n\x06result\x18\x02 \x01(\x0e\x32\x18.DtaBitReport.ResultEnum\x12&\n\x05state\x18\x03 \x01(\x0e\x32\x17.DtaBitReport.StateEnum\x12\x13\n\x05notes\x18\x04 \x01(\t:\x04None\"&\n\nResultEnum\x12\x0b\n\x07NOERROR\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\"+\n\tStateEnum\x12\x0b\n\x07STANDBY\x10\x00\x12\x07\n\x03RUN\x10\x01\x12\x08\n\x04GOOD\x10\x02\"8\n\x0e\x44taBitResponse\x12&\n\x0f\x64ta_bit_reports\x18\x01 \x03(\x0b\x32\r.DtaBitReport\"\"\n\x0e\x44taTrackReport\x12\x10\n\x05\x65mpty\x18\x01 \x01(\x05:\x01\x30\"#\n\x0f\x44taSystemStatus\x12\x10\n\x05\x65mpty\x18\x01 \x01(\x05:\x01\x30\"!\n\rDtaSystemInfo\x12\x10\n\x05\x65mpty\x18\x01 \x01(\x05:\x01\x30')



_DTABITREPORT_RESULTENUM = _descriptor.EnumDescriptor(
  name='ResultEnum',
  full_name='DtaBitReport.ResultEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=674,
  serialized_end=712,
)

_DTABITREPORT_STATEENUM = _descriptor.EnumDescriptor(
  name='StateEnum',
  full_name='DtaBitReport.StateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STANDBY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=714,
  serialized_end=757,
)


_RUNMODE = _descriptor.Descriptor(
  name='RunMode',
  full_name='RunMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=144,
  serialized_end=153,
)


_STANDBYMODE = _descriptor.Descriptor(
  name='StandbyMode',
  full_name='StandbyMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=155,
  serialized_end=168,
)


_SHUTDOWNSYSTEM = _descriptor.Descriptor(
  name='ShutdownSystem',
  full_name='ShutdownSystem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=170,
  serialized_end=186,
)


_GETSYSTEMSTATUS = _descriptor.Descriptor(
  name='GetSystemStatus',
  full_name='GetSystemStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=188,
  serialized_end=205,
)


_GETTRACKLIST = _descriptor.Descriptor(
  name='GetTrackList',
  full_name='GetTrackList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=207,
  serialized_end=221,
)


_GETTRACKREPORT = _descriptor.Descriptor(
  name='GetTrackReport',
  full_name='GetTrackReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=223,
  serialized_end=239,
)


_GETTRACKPDWS = _descriptor.Descriptor(
  name='GetTrackPDWs',
  full_name='GetTrackPDWs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=241,
  serialized_end=255,
)


_ACK = _descriptor.Descriptor(
  name='ACK',
  full_name='ACK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=257,
  serialized_end=262,
)


_SYSTEMSTATUS = _descriptor.Descriptor(
  name='SystemStatus',
  full_name='SystemStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=264,
  serialized_end=278,
)


_SYSTEMINFO = _descriptor.Descriptor(
  name='SystemInfo',
  full_name='SystemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=280,
  serialized_end=292,
)


_DTARESPONSETOPIC = _descriptor.Descriptor(
  name='DtaResponseTopic',
  full_name='DtaResponseTopic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='DtaResponseTopic.header', index=0,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dta_bit_response', full_name='DtaResponseTopic.dta_bit_response', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dta_track_report', full_name='DtaResponseTopic.dta_track_report', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dta_system_info', full_name='DtaResponseTopic.dta_system_info', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dta_system_status', full_name='DtaResponseTopic.dta_system_status', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=295,
  serialized_end=533,
)


_DTABITREPORT = _descriptor.Descriptor(
  name='DtaBitReport',
  full_name='DtaBitReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_name', full_name='DtaBitReport.test_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='DtaBitReport.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='DtaBitReport.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notes', full_name='DtaBitReport.notes', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("None", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DTABITREPORT_RESULTENUM,
    _DTABITREPORT_STATEENUM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=536,
  serialized_end=757,
)


_DTABITRESPONSE = _descriptor.Descriptor(
  name='DtaBitResponse',
  full_name='DtaBitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dta_bit_reports', full_name='DtaBitResponse.dta_bit_reports', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=759,
  serialized_end=815,
)


_DTATRACKREPORT = _descriptor.Descriptor(
  name='DtaTrackReport',
  full_name='DtaTrackReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='DtaTrackReport.empty', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=817,
  serialized_end=851,
)


_DTASYSTEMSTATUS = _descriptor.Descriptor(
  name='DtaSystemStatus',
  full_name='DtaSystemStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='DtaSystemStatus.empty', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=853,
  serialized_end=888,
)


_DTASYSTEMINFO = _descriptor.Descriptor(
  name='DtaSystemInfo',
  full_name='DtaSystemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty', full_name='DtaSystemInfo.empty', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=890,
  serialized_end=923,
)

_DTARESPONSETOPIC.fields_by_name['header'].message_type = ServiceInfrastructureCommon_pb2._HEADER
_DTARESPONSETOPIC.fields_by_name['dta_bit_response'].message_type = _DTABITRESPONSE
_DTARESPONSETOPIC.fields_by_name['dta_track_report'].message_type = _DTATRACKREPORT
_DTARESPONSETOPIC.fields_by_name['dta_system_info'].message_type = _DTASYSTEMINFO
_DTARESPONSETOPIC.fields_by_name['dta_system_status'].message_type = _DTASYSTEMSTATUS
_DTABITREPORT.fields_by_name['result'].enum_type = _DTABITREPORT_RESULTENUM
_DTABITREPORT.fields_by_name['state'].enum_type = _DTABITREPORT_STATEENUM
_DTABITREPORT_RESULTENUM.containing_type = _DTABITREPORT;
_DTABITREPORT_STATEENUM.containing_type = _DTABITREPORT;
_DTABITRESPONSE.fields_by_name['dta_bit_reports'].message_type = _DTABITREPORT
DESCRIPTOR.message_types_by_name['RunMode'] = _RUNMODE
DESCRIPTOR.message_types_by_name['StandbyMode'] = _STANDBYMODE
DESCRIPTOR.message_types_by_name['ShutdownSystem'] = _SHUTDOWNSYSTEM
DESCRIPTOR.message_types_by_name['GetSystemStatus'] = _GETSYSTEMSTATUS
DESCRIPTOR.message_types_by_name['GetTrackList'] = _GETTRACKLIST
DESCRIPTOR.message_types_by_name['GetTrackReport'] = _GETTRACKREPORT
DESCRIPTOR.message_types_by_name['GetTrackPDWs'] = _GETTRACKPDWS
DESCRIPTOR.message_types_by_name['ACK'] = _ACK
DESCRIPTOR.message_types_by_name['SystemStatus'] = _SYSTEMSTATUS
DESCRIPTOR.message_types_by_name['SystemInfo'] = _SYSTEMINFO
DESCRIPTOR.message_types_by_name['DtaResponseTopic'] = _DTARESPONSETOPIC
DESCRIPTOR.message_types_by_name['DtaBitReport'] = _DTABITREPORT
DESCRIPTOR.message_types_by_name['DtaBitResponse'] = _DTABITRESPONSE
DESCRIPTOR.message_types_by_name['DtaTrackReport'] = _DTATRACKREPORT
DESCRIPTOR.message_types_by_name['DtaSystemStatus'] = _DTASYSTEMSTATUS
DESCRIPTOR.message_types_by_name['DtaSystemInfo'] = _DTASYSTEMINFO

class RunMode(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNMODE

  # @@protoc_insertion_point(class_scope:RunMode)

class StandbyMode(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STANDBYMODE

  # @@protoc_insertion_point(class_scope:StandbyMode)

class ShutdownSystem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHUTDOWNSYSTEM

  # @@protoc_insertion_point(class_scope:ShutdownSystem)

class GetSystemStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSYSTEMSTATUS

  # @@protoc_insertion_point(class_scope:GetSystemStatus)

class GetTrackList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETTRACKLIST

  # @@protoc_insertion_point(class_scope:GetTrackList)

class GetTrackReport(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETTRACKREPORT

  # @@protoc_insertion_point(class_scope:GetTrackReport)

class GetTrackPDWs(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETTRACKPDWS

  # @@protoc_insertion_point(class_scope:GetTrackPDWs)

class ACK(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACK

  # @@protoc_insertion_point(class_scope:ACK)

class SystemStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMSTATUS

  # @@protoc_insertion_point(class_scope:SystemStatus)

class SystemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMINFO

  # @@protoc_insertion_point(class_scope:SystemInfo)

class DtaResponseTopic(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DTARESPONSETOPIC

  # @@protoc_insertion_point(class_scope:DtaResponseTopic)

class DtaBitReport(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DTABITREPORT

  # @@protoc_insertion_point(class_scope:DtaBitReport)

class DtaBitResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DTABITRESPONSE

  # @@protoc_insertion_point(class_scope:DtaBitResponse)

class DtaTrackReport(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DTATRACKREPORT

  # @@protoc_insertion_point(class_scope:DtaTrackReport)

class DtaSystemStatus(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DTASYSTEMSTATUS

  # @@protoc_insertion_point(class_scope:DtaSystemStatus)

class DtaSystemInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DTASYSTEMINFO

  # @@protoc_insertion_point(class_scope:DtaSystemInfo)


# @@protoc_insertion_point(module_scope)
