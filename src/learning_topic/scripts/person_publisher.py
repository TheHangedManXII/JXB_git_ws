#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 该例程将发布/person_info话题，自定义消息类型learning_topic::Person

import rospy
from learning_topic.msg import Person

def velocity_publisher():
	# ROS节点初始化
    rospy.init_node('person_publisher', anonymous=True)

	# 创建一个Publisher，发布名为/person_info的topic，消息类型为learning_topic::Person，队列长度10
    person_info_pub = rospy.Publisher('/person_tf', Person, queue_size=10)

	#设置循环的频率
    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
		# 初始化learning_topic::Person类型的消息
    	person_msg = Person()
    	person_msg.name = "Tom";
    	person_msg.x  = 0.2413204145431519;
    	person_msg.y  = 0.23344324;

		# 发布消息
        person_info_pub.publish(person_msg)
    	rospy.loginfo("Publsh person message[%s, %0.8lf, %lf]", 
				person_msg.name, person_msg.x, person_msg.y)

		# 按照循环频率延时
        rate.sleep()

if __name__ == '__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass
