# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/EquippedBadge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import BadgeType_pb2 as Enums_dot_BadgeType__pb2

from Enums.BadgeType_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Player/EquippedBadge.proto',
  package='POGOProtos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x1aPlayer/EquippedBadge.proto\x12\x11POGOProtos.Player\x1a\x15\x45nums/BadgeType.proto\"\x7f\n\rEquippedBadge\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.BadgeType\x12\r\n\x05level\x18\x02 \x01(\x05\x12.\n&next_equip_change_allowed_timestamp_ms\x18\x03 \x01(\x03P\x00\x62\x06proto3')
  ,
  dependencies=[Enums_dot_BadgeType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EQUIPPEDBADGE = _descriptor.Descriptor(
  name='EquippedBadge',
  full_name='POGOProtos.Player.EquippedBadge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='POGOProtos.Player.EquippedBadge.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='POGOProtos.Player.EquippedBadge.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_equip_change_allowed_timestamp_ms', full_name='POGOProtos.Player.EquippedBadge.next_equip_change_allowed_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=199,
)

_EQUIPPEDBADGE.fields_by_name['badge_type'].enum_type = Enums_dot_BadgeType__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['EquippedBadge'] = _EQUIPPEDBADGE

EquippedBadge = _reflection.GeneratedProtocolMessageType('EquippedBadge', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPPEDBADGE,
  __module__ = 'Player.EquippedBadge_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Player.EquippedBadge)
  ))
_sym_db.RegisterMessage(EquippedBadge)


# @@protoc_insertion_point(module_scope)