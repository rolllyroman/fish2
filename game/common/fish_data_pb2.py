# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pickfish/fish_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pickfish/fish_data.proto',
  package='fishdata',
  serialized_pb='\n\x18pickfish/fish_data.proto\x12\x08\x66ishdata\">\n\tRouteNode\x12\x10\n\x08rotSpeed\x18\x01 \x02(\x0f\x12\r\n\x05speed\x18\x02 \x02(\x07\x12\x10\n\x08\x64uration\x18\x03 \x02(\x02\"\x93\x01\n\x0b\x46ishingData\x12\r\n\x05level\x18\x01 \x02(\x07\x12\x0b\n\x03rot\x18\x02 \x02(\x02\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\x0c\n\x04\x64ice\x18\x05 \x02(\x07\x12\x10\n\x08\x64uration\x18\x06 \x02(\x02\x12\x0e\n\x06offset\x18\x07 \x02(\x07\x12\"\n\x05route\x18\x08 \x03(\x0b\x32\x13.fishdata.RouteNode\"3\n\nFishesData\x12%\n\x06\x66ishes\x18\x01 \x03(\x0b\x32\x15.fishdata.FishingData\"8\n\x0b\x46ishBatches\x12)\n\x0b\x66ishesBatch\x18\x01 \x03(\x0b\x32\x14.fishdata.FishesData\"D\n\tFishArray\x12\x10\n\x08\x64uration\x18\x01 \x02(\x07\x12%\n\x06\x66ishes\x18\x02 \x03(\x0b\x32\x15.fishdata.FishingData\"5\n\nFishArrays\x12\'\n\nfishArrays\x18\x02 \x03(\x0b\x32\x13.fishdata.FishArray')




_ROUTENODE = _descriptor.Descriptor(
  name='RouteNode',
  full_name='fishdata.RouteNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotSpeed', full_name='fishdata.RouteNode.rotSpeed', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='fishdata.RouteNode.speed', index=1,
      number=2, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='fishdata.RouteNode.duration', index=2,
      number=3, type=2, cpp_type=6, label=2,
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
  serialized_start=38,
  serialized_end=100,
)


_FISHINGDATA = _descriptor.Descriptor(
  name='FishingData',
  full_name='fishdata.FishingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='fishdata.FishingData.level', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rot', full_name='fishdata.FishingData.rot', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='fishdata.FishingData.x', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='fishdata.FishingData.y', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dice', full_name='fishdata.FishingData.dice', index=4,
      number=5, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='fishdata.FishingData.duration', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='fishdata.FishingData.offset', index=6,
      number=7, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route', full_name='fishdata.FishingData.route', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=103,
  serialized_end=250,
)


_FISHESDATA = _descriptor.Descriptor(
  name='FishesData',
  full_name='fishdata.FishesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fishes', full_name='fishdata.FishesData.fishes', index=0,
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
  serialized_start=252,
  serialized_end=303,
)


_FISHBATCHES = _descriptor.Descriptor(
  name='FishBatches',
  full_name='fishdata.FishBatches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fishesBatch', full_name='fishdata.FishBatches.fishesBatch', index=0,
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
  serialized_start=305,
  serialized_end=361,
)


_FISHARRAY = _descriptor.Descriptor(
  name='FishArray',
  full_name='fishdata.FishArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration', full_name='fishdata.FishArray.duration', index=0,
      number=1, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fishes', full_name='fishdata.FishArray.fishes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=363,
  serialized_end=431,
)


_FISHARRAYS = _descriptor.Descriptor(
  name='FishArrays',
  full_name='fishdata.FishArrays',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fishArrays', full_name='fishdata.FishArrays.fishArrays', index=0,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=433,
  serialized_end=486,
)

_FISHINGDATA.fields_by_name['route'].message_type = _ROUTENODE
_FISHESDATA.fields_by_name['fishes'].message_type = _FISHINGDATA
_FISHBATCHES.fields_by_name['fishesBatch'].message_type = _FISHESDATA
_FISHARRAY.fields_by_name['fishes'].message_type = _FISHINGDATA
_FISHARRAYS.fields_by_name['fishArrays'].message_type = _FISHARRAY
DESCRIPTOR.message_types_by_name['RouteNode'] = _ROUTENODE
DESCRIPTOR.message_types_by_name['FishingData'] = _FISHINGDATA
DESCRIPTOR.message_types_by_name['FishesData'] = _FISHESDATA
DESCRIPTOR.message_types_by_name['FishBatches'] = _FISHBATCHES
DESCRIPTOR.message_types_by_name['FishArray'] = _FISHARRAY
DESCRIPTOR.message_types_by_name['FishArrays'] = _FISHARRAYS

class RouteNode(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROUTENODE

  # @@protoc_insertion_point(class_scope:fishdata.RouteNode)

class FishingData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FISHINGDATA

  # @@protoc_insertion_point(class_scope:fishdata.FishingData)

class FishesData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FISHESDATA

  # @@protoc_insertion_point(class_scope:fishdata.FishesData)

class FishBatches(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FISHBATCHES

  # @@protoc_insertion_point(class_scope:fishdata.FishBatches)

class FishArray(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FISHARRAY

  # @@protoc_insertion_point(class_scope:fishdata.FishArray)

class FishArrays(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FISHARRAYS

  # @@protoc_insertion_point(class_scope:fishdata.FishArrays)


# @@protoc_insertion_point(module_scope)