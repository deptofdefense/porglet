# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_rx_scheduler.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_rx_scheduler.proto',
  package='service_rx_scheduler',
  serialized_pb='\n\x1aservice_rx_scheduler.proto\x12\x14service_rx_scheduler\"\x9c\x04\n\x11RxSchedulerConfig\x12\x37\n\x07msgName\x18\x01 \x01(\t:&service_rx_scheduler.RxSchedulerConfig\x12W\n\x13scheduleImportInfos\x18\x02 \x03(\x0b\x32:.service_rx_scheduler.RxSchedulerConfig.ScheduleImportInfo\x12W\n\x13timelineImportInfos\x18\x03 \x03(\x0b\x32:.service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo\x12W\n\x13\x62lackoutImportInfos\x18\x04 \x03(\x0b\x32:.service_rx_scheduler.RxSchedulerConfig.BlackoutImportInfo\x1a;\n\x12ScheduleImportInfo\x12\x11\n\tchannelId\x18\x01 \x02(\t\x12\x12\n\nimportPath\x18\x02 \x02(\t\x1a^\n\x12TimelineImportInfo\x12\x11\n\tchannelId\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\t\x12\x10\n\x08stopTime\x18\x03 \x01(\t\x12\x10\n\x08\x66ilePath\x18\x04 \x01(\t\x1a&\n\x12\x42lackoutImportInfo\x12\x10\n\x08\x66ilePath\x18\x01 \x01(\tB\x15\n\x13\x66v.protos.kepsvisor')




_RXSCHEDULERCONFIG_SCHEDULEIMPORTINFO = _descriptor.Descriptor(
  name='ScheduleImportInfo',
  full_name='service_rx_scheduler.RxSchedulerConfig.ScheduleImportInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelId', full_name='service_rx_scheduler.RxSchedulerConfig.ScheduleImportInfo.channelId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='importPath', full_name='service_rx_scheduler.RxSchedulerConfig.ScheduleImportInfo.importPath', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=398,
  serialized_end=457,
)

_RXSCHEDULERCONFIG_TIMELINEIMPORTINFO = _descriptor.Descriptor(
  name='TimelineImportInfo',
  full_name='service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelId', full_name='service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo.channelId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo.startTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stopTime', full_name='service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo.stopTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filePath', full_name='service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo.filePath', index=3,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=459,
  serialized_end=553,
)

_RXSCHEDULERCONFIG_BLACKOUTIMPORTINFO = _descriptor.Descriptor(
  name='BlackoutImportInfo',
  full_name='service_rx_scheduler.RxSchedulerConfig.BlackoutImportInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filePath', full_name='service_rx_scheduler.RxSchedulerConfig.BlackoutImportInfo.filePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=555,
  serialized_end=593,
)

_RXSCHEDULERCONFIG = _descriptor.Descriptor(
  name='RxSchedulerConfig',
  full_name='service_rx_scheduler.RxSchedulerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='service_rx_scheduler.RxSchedulerConfig.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("service_rx_scheduler.RxSchedulerConfig", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scheduleImportInfos', full_name='service_rx_scheduler.RxSchedulerConfig.scheduleImportInfos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timelineImportInfos', full_name='service_rx_scheduler.RxSchedulerConfig.timelineImportInfos', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blackoutImportInfos', full_name='service_rx_scheduler.RxSchedulerConfig.blackoutImportInfos', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RXSCHEDULERCONFIG_SCHEDULEIMPORTINFO, _RXSCHEDULERCONFIG_TIMELINEIMPORTINFO, _RXSCHEDULERCONFIG_BLACKOUTIMPORTINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=53,
  serialized_end=593,
)

_RXSCHEDULERCONFIG_SCHEDULEIMPORTINFO.containing_type = _RXSCHEDULERCONFIG;
_RXSCHEDULERCONFIG_TIMELINEIMPORTINFO.containing_type = _RXSCHEDULERCONFIG;
_RXSCHEDULERCONFIG_BLACKOUTIMPORTINFO.containing_type = _RXSCHEDULERCONFIG;
_RXSCHEDULERCONFIG.fields_by_name['scheduleImportInfos'].message_type = _RXSCHEDULERCONFIG_SCHEDULEIMPORTINFO
_RXSCHEDULERCONFIG.fields_by_name['timelineImportInfos'].message_type = _RXSCHEDULERCONFIG_TIMELINEIMPORTINFO
_RXSCHEDULERCONFIG.fields_by_name['blackoutImportInfos'].message_type = _RXSCHEDULERCONFIG_BLACKOUTIMPORTINFO
DESCRIPTOR.message_types_by_name['RxSchedulerConfig'] = _RXSCHEDULERCONFIG

class RxSchedulerConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class ScheduleImportInfo(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RXSCHEDULERCONFIG_SCHEDULEIMPORTINFO

    # @@protoc_insertion_point(class_scope:service_rx_scheduler.RxSchedulerConfig.ScheduleImportInfo)

  class TimelineImportInfo(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RXSCHEDULERCONFIG_TIMELINEIMPORTINFO

    # @@protoc_insertion_point(class_scope:service_rx_scheduler.RxSchedulerConfig.TimelineImportInfo)

  class BlackoutImportInfo(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RXSCHEDULERCONFIG_BLACKOUTIMPORTINFO

    # @@protoc_insertion_point(class_scope:service_rx_scheduler.RxSchedulerConfig.BlackoutImportInfo)
  DESCRIPTOR = _RXSCHEDULERCONFIG

  # @@protoc_insertion_point(class_scope:service_rx_scheduler.RxSchedulerConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\023fv.protos.kepsvisor')
# @@protoc_insertion_point(module_scope)
