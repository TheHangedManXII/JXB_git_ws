#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2019 Wuhan PS-Micro Technology Co., Itd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy, sys
import moveit_commander

import signal
from ast import literal_eval
from ntpath import join

from learning_tf.msg import Person

import tf2_ros
from geometry_msgs.msg import PoseStamped, Pose,TransformStamped
from tf2_geometry_msgs import PointStamped
import tf



def tf_subscriber():


	# 创建一个Subscriber，订阅名为/person_info的topic，注册回调函数personInfoCallback
    rospy.Subscriber('mytf_person', Person, tfCallback,queue_size=1,buff_size=524288)

	# 循环等待回调函数
    rospy.spin()

def tfCallback(msg):
    # tf transform
    point_source = PointStamped()
    point_source.header.frame_id = "seat"
    point_source.header.stamp = rospy.Time.now()
    point_source.point.x = msg.x
    point_source.point.y = msg.y
    point_source.point.z = msg.z

    point_target = buffer.transform(point_source,"link1",rospy.Duration(0.5))
    rospy.loginfo("point_target 所属的坐标系:%s",point_target.header.frame_id)
    rospy.loginfo("坐标点相对于 link1 的坐标:(%.5f,%.5f,%.5f)",
    point_target.point.x,
    point_target.point.y,
    point_target.point.z)

    # moveit plan
    target_pose = PoseStamped()
    target_pose.header.frame_id = 'link1'
    target_pose.header.stamp = rospy.Time.now()    
    target_pose.pose.position.x = point_target.point.x
    target_pose.pose.position.y = -point_target.point.y
    target_pose.pose.position.z = -point_target.point.z
    target_pose.pose.orientation.x = 0
    target_pose.pose.orientation.y = 0
    target_pose.pose.orientation.z = 0
    target_pose.pose.orientation.w = 0

    arm.set_start_state_to_current_state()
    arm.set_pose_target(target_pose, end_effector_link)
    traj = arm.plan()
    rospy.loginfo(target_pose)
    arm.go()



	
if __name__ == "__main__":
	 # ROS节点初始化
     rospy.init_node('person_subscriber', anonymous=True)
     # 初始化move_group的API
     moveit_commander.roscpp_initialize(sys.argv)
            
     # 初始化需要使用move group控制的机械臂中的arm group
     arm = moveit_commander.MoveGroupCommander('manipulator')
            
     # 获取终端link的名称
     end_effector_link = arm.get_end_effector_link()
                    
     # 设置目标位置所使用的参考坐标系

     arm.set_pose_reference_frame('link1')
             
     # 当运动规划失败后，允许重新规划
     arm.allow_replanning(True)

     # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
     arm.set_goal_position_tolerance(0.001)
     arm.set_goal_orientation_tolerance(0.01)

     # 设置允许的最大速度和加速度
     arm.set_max_acceleration_scaling_factor(0.8)
     arm.set_max_velocity_scaling_factor(0.8)
     buffer = tf2_ros.Buffer()
     listener = tf2_ros.TransformListener(buffer)
     br = tf.TransformBroadcaster()
     rate = rospy.Rate(0.1)
     while not rospy.is_shutdown():
        tf_subscriber()


    
    
