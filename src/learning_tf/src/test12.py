#! /usr/bin/env python3
# -*-coding:utf-8-*
"""  
    静态坐标变换发布方:
        发布关于 laser 坐标系的位置信息 
    实现流程:
        1.导包
        2.初始化 ROS 节点
        3.创建 静态坐标广播器
        4.创建并组织被广播的消息
        5.广播器发送消息
        6.spin
"""
# 1.导包
import rospy
import tf2_ros
import tf
from geometry_msgs.msg import TransformStamped

if __name__ == "__main__":
    # 2.初始化 ROS 节点
    rospy.init_node("static_tf_pub_p")
    # 3.创建 静态坐标广播器
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    # 4.创建并组织被广播的消息
    tfs = TransformStamped()
    # --- 头信息
    tfs.header.frame_id = "world"
    tfs.header.stamp = rospy.Time.now()
    tfs.header.seq = 101
    # --- 子坐标系
    tfs.child_frame_id = "radar"
    # --- 坐标系相对信息
    # ------ 偏移量
    tfs.transform.translation.x = 0.2
    tfs.transform.translation.y = 0.0
    tfs.transform.translation.z = 0.5
    # ------ 四元数
    qtn = tf.transformations.quaternion_from_euler(0,0,0)
    tfs.transform.rotation.x = qtn[0]
    tfs.transform.rotation.y = qtn[1]
    tfs.transform.rotation.z = qtn[2]
    tfs.transform.rotation.w = qtn[3]


    # 5.广播器发送消息
    broadcaster.sendTransform(tfs)
    # 6.spin
    rospy.spin()
