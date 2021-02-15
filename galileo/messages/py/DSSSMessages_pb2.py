# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DSSSMessages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DSSSMessages.proto',
  package='',
  serialized_pb='\n\x12\x44SSSMessages.proto\"\xae\x01\n\x0b\x44SSSProduct\x12\x1d\n\x07msgName\x18\x01 \x01(\t:\x0c\x44SSS_PRODUCT\x12\r\n\x05rf_hz\x18\x02 \x01(\x01\x12\x10\n\x08\x63hiprate\x18\x03 \x01(\x01\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\x12\n\ncodelength\x18\x05 \x01(\x05\x12\x14\n\x0cwholeSeconds\x18\x06 \x01(\x01\x12\x13\n\x0b\x66racSeconds\x18\x07 \x01(\x01\x12\x12\n\nconfidence\x18\x08 \x01(\x02\x42\x15\n\x13\x66v.protos.kepsvisor')




_DSSSPRODUCT = _descriptor.Descriptor(
  name='DSSSProduct',
  full_name='DSSSProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgName', full_name='DSSSProduct.msgName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("DSSS_PRODUCT", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rf_hz', full_name='DSSSProduct.rf_hz', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chiprate', full_name='DSSSProduct.chiprate', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='DSSSProduct.code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='codelength', full_name='DSSSProduct.codelength', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wholeSeconds', full_name='DSSSProduct.wholeSeconds', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fracSeconds', full_name='DSSSProduct.fracSeconds', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='DSSSProduct.confidence', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=23,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['DSSSProduct'] = _DSSSPRODUCT

class DSSSProduct(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DSSSPRODUCT

  # @@protoc_insertion_point(class_scope:DSSSProduct)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\023fv.protos.kepsvisor')
# @@protoc_insertion_point(module_scope)
