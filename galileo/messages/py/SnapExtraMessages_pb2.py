# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SnapExtraMessages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SnapExtraMessages.proto',
  package='',
  serialized_pb='\n\x17SnapExtraMessages.proto\"I\n\x10SnapExtraRequest\x12#\n\x07msgName\x18\x01 \x01(\t:\x12SNAP_EXTRA_REQUEST\x12\x10\n\x08snapName\x18\x02 \x01(\tB\x15\n\x13\x66v.protos.kepsvisor')




_SNAPEXTRAREQUEST = _descriptor.Descriptor(
  name='SnapExtraRequest',
  full_name='SnapExtraRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='SnapExtraRequest.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("SNAP_EXTRA_REQUEST", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapName', full_name='SnapExtraRequest.snapName', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=27,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['SnapExtraRequest'] = _SNAPEXTRAREQUEST

class SnapExtraRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SNAPEXTRAREQUEST

  # @@protoc_insertion_point(class_scope:SnapExtraRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\023fv.protos.kepsvisor')
# @@protoc_insertion_point(module_scope)
