; Auto-generated. Do not edit!


(cl:in-package smallArmRobot_driver-msg)


;//! \htmlinclude step_msg.msg.html

(cl:defclass <step_msg> (roslisp-msg-protocol:ros-message)
  ((Steps
    :reader Steps
    :initarg :Steps
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass step_msg (<step_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <step_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'step_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smallArmRobot_driver-msg:<step_msg> is deprecated: use smallArmRobot_driver-msg:step_msg instead.")))

(cl:ensure-generic-function 'Steps-val :lambda-list '(m))
(cl:defmethod Steps-val ((m <step_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smallArmRobot_driver-msg:Steps-val is deprecated.  Use smallArmRobot_driver-msg:Steps instead.")
  (Steps m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <step_msg>) ostream)
  "Serializes a message object of type '<step_msg>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'Steps))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'Steps))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <step_msg>) istream)
  "Deserializes a message object of type '<step_msg>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'Steps) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'Steps)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<step_msg>)))
  "Returns string type for a message object of type '<step_msg>"
  "smallArmRobot_driver/step_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'step_msg)))
  "Returns string type for a message object of type 'step_msg"
  "smallArmRobot_driver/step_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<step_msg>)))
  "Returns md5sum for a message object of type '<step_msg>"
  "f848ce10d6e93faa8d4adf474668aef3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'step_msg)))
  "Returns md5sum for a message object of type 'step_msg"
  "f848ce10d6e93faa8d4adf474668aef3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<step_msg>)))
  "Returns full string definition for message of type '<step_msg>"
  (cl:format cl:nil "int16[] Steps~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'step_msg)))
  "Returns full string definition for message of type 'step_msg"
  (cl:format cl:nil "int16[] Steps~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <step_msg>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'Steps) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <step_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'step_msg
    (cl:cons ':Steps (Steps msg))
))
