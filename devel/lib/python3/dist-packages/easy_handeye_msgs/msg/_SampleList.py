# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from easy_handeye_msgs/SampleList.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class SampleList(genpy.Message):
  _md5sum = "19e891d084c5a799fdfe97bd1dbbf9c5"
  _type = "easy_handeye_msgs/SampleList"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Transform[] hand_world_samples
geometry_msgs/Transform[] camera_marker_samples
================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['hand_world_samples','camera_marker_samples']
  _slot_types = ['geometry_msgs/Transform[]','geometry_msgs/Transform[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       hand_world_samples,camera_marker_samples

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SampleList, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.hand_world_samples is None:
        self.hand_world_samples = []
      if self.camera_marker_samples is None:
        self.camera_marker_samples = []
    else:
      self.hand_world_samples = []
      self.camera_marker_samples = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.hand_world_samples)
      buff.write(_struct_I.pack(length))
      for val1 in self.hand_world_samples:
        _v1 = val1.translation
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.rotation
        _x = _v2
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.camera_marker_samples)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_marker_samples:
        _v3 = val1.translation
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.rotation
        _x = _v4
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.hand_world_samples is None:
        self.hand_world_samples = None
      if self.camera_marker_samples is None:
        self.camera_marker_samples = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.hand_world_samples = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v5 = val1.translation
        _x = _v5
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v6 = val1.rotation
        _x = _v6
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.hand_world_samples.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_marker_samples = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v7 = val1.translation
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v8 = val1.rotation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.camera_marker_samples.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.hand_world_samples)
      buff.write(_struct_I.pack(length))
      for val1 in self.hand_world_samples:
        _v9 = val1.translation
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v10 = val1.rotation
        _x = _v10
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.camera_marker_samples)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_marker_samples:
        _v11 = val1.translation
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = val1.rotation
        _x = _v12
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.hand_world_samples is None:
        self.hand_world_samples = None
      if self.camera_marker_samples is None:
        self.camera_marker_samples = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.hand_world_samples = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v13 = val1.translation
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = val1.rotation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.hand_world_samples.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_marker_samples = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v15 = val1.translation
        _x = _v15
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v16 = val1.rotation
        _x = _v16
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.camera_marker_samples.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d