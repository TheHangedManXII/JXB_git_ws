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

from ast import literal_eval
from ntpath import join
import rospy
import sys
import moveit_commander
import time

import signal

# 自定义信号处理函数
def my_handler(signum, frame):
    global stop
    stop = True
    print("终止")

def do_moveit():
    # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
    joint_positions = readLastSec("/home/bearpi/python3_ws/datalkmads.txt")
    print(joint_positions)
    arm.set_joint_value_target(joint_positions)

    # 控制机械臂完成运动
    arm.go()
    rospy.sleep(5)

def readLastSec(file):
    with open(file, 'r') as f:
        data = f.readlines()
        data_2 = literal_eval(data[-1])
        return data_2

def close_moveit():
        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
if __name__ == "__main__":
    try:
        stop = False
        signal.signal(signal.SIGINT, my_handler)
                # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)

        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('manipulator')

        # 设置机械臂运动的允许误差值
        arm.set_goal_joint_tolerance(0.001)

        # 设置允许的最大速度和加速度
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)

        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)
        while not stop:
            do_moveit()

    except rospy.ROSInterruptException:
        pass
