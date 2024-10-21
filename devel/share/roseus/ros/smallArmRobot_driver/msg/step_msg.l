;; Auto-generated. Do not edit!


(when (boundp 'smallArmRobot_driver::step_msg)
  (if (not (find-package "SMALLARMROBOT_DRIVER"))
    (make-package "SMALLARMROBOT_DRIVER"))
  (shadow 'step_msg (find-package "SMALLARMROBOT_DRIVER")))
(unless (find-package "SMALLARMROBOT_DRIVER::STEP_MSG")
  (make-package "SMALLARMROBOT_DRIVER::STEP_MSG"))

(in-package "ROS")
;;//! \htmlinclude step_msg.msg.html


(defclass smallArmRobot_driver::step_msg
  :super ros::object
  :slots (_Steps ))

(defmethod smallArmRobot_driver::step_msg
  (:init
   (&key
    ((:Steps __Steps) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _Steps __Steps)
   self)
  (:Steps
   (&optional __Steps)
   (if __Steps (setq _Steps __Steps)) _Steps)
  (:serialization-length
   ()
   (+
    ;; int16[] _Steps
    (* 2    (length _Steps)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16[] _Steps
     (write-long (length _Steps) s)
     (dotimes (i (length _Steps))
       (write-word (elt _Steps i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16[] _Steps
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Steps (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _Steps i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;;
   self)
  )

(setf (get smallArmRobot_driver::step_msg :md5sum-) "f848ce10d6e93faa8d4adf474668aef3")
(setf (get smallArmRobot_driver::step_msg :datatype-) "smallArmRobot_driver/step_msg")
(setf (get smallArmRobot_driver::step_msg :definition-)
      "int16[] Steps


")



(provide :smallArmRobot_driver/step_msg "f848ce10d6e93faa8d4adf474668aef3")


