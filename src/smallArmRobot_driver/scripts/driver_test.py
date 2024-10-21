#!/usr/bin/python3
# coding:utf-8

# 导入rospy库
import rospy

# joint_state的msg是属于sensor
from sensor_msgs.msg import JointState
from smallArmRobot_driver.msg import step_msg
# 调用StandardFirmata协议
from pyfirmata import ArduinoMega, util

# 导入时间函数
import time

# 导入IO配置函数，自定义
from IO_config import *

# 步进电机驱动引脚声明
Joint_STEP = [Joint1_STEP, Joint2_STEP, Joint3_STEP, Joint4_STEP, Joint5_STEP, Joint6_STEP]  # 脉冲引脚声明
Joint_DIR = [Joint1_DIR, Joint2_DIR, Joint3_DIR, Joint4_DIR, Joint5_DIR, Joint6_DIR]  # 方向引脚声明
Joint_EN = [Joint1_EN, Joint2_EN, Joint3_EN, Joint4_EN, Joint5_EN, Joint6_EN]  # 使能驱动引脚声明

# 减速比系数声明，这里有减速带，需要重新计算
joint_pro = [joint1_pro, joint2_pro, joint3_pro, joint4_pro, joint5_pro, joint6_pro]

# 标记量声明
joint_pul_flag = [joint1_pul_flag, joint2_pul_flag, joint3_pul_flag, joint4_pul_flag, joint5_pul_flag,
                  joint6_pul_flag]  # 脉冲标记
joint_dir_flag = [joint1_dir_flag, joint2_dir_flag, joint3_dir_flag, joint4_dir_flag, joint5_dir_flag,
                  joint6_dir_flag]  # 方向标记
joint_value = [joint1_value, joint2_value, joint3_value, joint4_value, joint5_value, joint6_value]  # 当前角度值
joint_angle = [joint1_angle, joint2_angle, joint3_angle, joint4_angle, joint5_angle, joint6_angle]
diff_value = [diff_value1, diff_value2, diff_value3, diff_value4, diff_value5, diff_value6]

total_step = 0
step_joint = [step_joint1, step_joint2, step_joint3, step_joint4, step_joint5, step_joint6]
# 脉冲限位
joint_min_pul = [joint1_min_pul, joint2_min_pul, joint3_min_pul, joint4_min_pul, joint5_min_pul,
                 joint6_min_pul]  # 最小脉冲值
joint_max_pul = [joint1_max_pul, joint2_max_pul, joint3_max_pul, joint4_max_pul, joint5_max_pul,
                 joint6_max_pul]  # 最大脉冲值

'''
函数名称：value_driver
函数功能：控制对应的关节旋转到指定的角度值
输入参数：joint为关节编号，angle为该关节目标角度值
'''


def value_calculate(goal_angle):
    # 如果当前的脉冲迭代超出可运行范围，步进电机不执行，输出提示信息。这里是为了避免过转导致机械臂卡住
    # 需要的部署变量声明
    i = 0

    for i in range(0, 6):

        # 如果目标角度angle小于当前角度值
        if goal_angle[i] < joint_value[i]:
            joint_dir_flag[i] = 0  # 对应关节方向标记为0
           # board.digital[Joint_DIR[i]].write(0)  # 方向引脚为低电平
            diff_value[i] = goal_angle[i] - 90  # 计算角度差值

        else:
            joint_dir_flag[i] = 1  # 对应关节方向标记为1
           # board.digital[Joint_DIR[i]].write(1)  # 方向引脚为高电平
            diff_value[i] = goal_angle[i] - 90  # 计算角度差值



        step_joint[i] = int((diff_value[i] / joint_pro[i])  )# 步数=角度值/减速比

    for m in range(0, 6):
        step_joint[m] = int((diff_value[m] / joint_pro[m]))
        if joint_dir_flag[m] == 0:
            joint_pul_flag[m] = joint_pul_flag[m] - step_joint[m]  # 更新当前脉冲标识
        else:
            joint_pul_flag[m] = joint_pul_flag[m] + step_joint[m]


        joint_value[m] = goal_angle[m]  # 角度值迭代







'''
函数名称：callback
函数功能：作为回调函数执行
'''


def callback(data):
    global step_msg
    joint_angle[5] = data.position[0] * 360 / 6.28 + 90  # 对应的关节弧度值转角度值值转
    # 判断当前角度值是否越界
    if joint_angle[5] < 0:
        # 如果当前角度值小于0，则角度值为0，避免出现负数
        joint_angle[5] = 0
    elif joint_angle[5] > 180:
        # 如果当前角度值大于180，则角度值为180，避免出现角度超出
        joint_angle[5] = 180
    rospy.loginfo(rospy.get_caller_id() + ']--->Joint6 Angle :%d', joint_angle[5])  # ros下输出提示信息
    # value_driver(5,joint_angle[5])   #角度值执行

    # 下同
    joint_angle[4] = data.position[1] * 360 / 6.28 + 90
    if joint_angle[4] < 0:
        joint_angle[4] = 0
    elif joint_angle[4] > 180:
        joint_angle[4] = 180
    rospy.loginfo(rospy.get_caller_id() + ']--->Joint5 Angle :%d', joint_angle[4])
    # value_driver(4,joint_angle[4])

    joint_angle[3] = data.position[2] * 360 / 6.28 + 90
    if joint_angle[3] < 0:
        joint_angle[3] = 0
    elif joint_angle[3] > 180:
        joint_angle[3] = 180
    rospy.loginfo(rospy.get_caller_id() + ']--->Joint4 Angle :%d', joint_angle[3])
    # value_driver(3,joint_angle[3])

    joint_angle[2] = data.position[3] * 360 / 6.28 + 90
    if joint_angle[2] < 0:
        joint_angle[2] = 0
    elif joint_angle[2] > 180:
        joint_angle[2] = 180
    rospy.loginfo(rospy.get_caller_id() + ']--->Joint3 Angle :%d', joint_angle[2])
    # value_driver(2,joint_angle[2])

    joint_angle[1] = data.position[4] * 360 / 6.28 + 90
    if joint_angle[1] < 0:
        joint_angle[1] = 0
    elif joint_angle[1] > 180:
        joint_angle[1] = 180
    rospy.loginfo(rospy.get_caller_id() + ']--->Joint2 Angle :%d', joint_angle[1])
    # value_driver(1,joint_angle[1])

    joint_angle[0] = data.position[5] * 360 / 6.28 + 90
    if joint_angle[0] < 0:
        joint_angle[0] = 0
    elif joint_angle[0] > 180:
        joint_angle[0] = 180
    rospy.loginfo(rospy.get_caller_id() + ']--->Joint1 Angle :%d', joint_angle[0])

    value_calculate(joint_angle)

    step_pub = rospy.Publisher('Step_msgs', step_msg, queue_size=1)
    step_msgs = step_msg()
    step_msgs.Steps  = (step_joint[0]*4,step_joint[1]*4,step_joint[2]*4,step_joint[3]*4,step_joint[4]*3,step_joint[5]*4)
    # step_msgs.step2  = step_joint[1]
    # step_msgs.step3  = step_joint[2]
    # step_msgs.step4  = step_joint[3]
    # step_msgs.step5  = step_joint[4]
    # step_msgs.step6  = step_joint[5]
    step_pub.publish(step_msgs)
    rate = rospy.Rate(1)
    rate.sleep()


def driver():
    rospy.init_node('SmallArmRobot_Driver', anonymous=True)  # 初始化节点，命名为SmallArmRobot_Driver
    
    rospy.Subscriber('joint_states', JointState, callback,queue_size=1,buff_size=524288)  # 订阅joint_states话题，类型为JointState，当订阅到该话题执行callback函数

    rospy.spin()



if __name__ == '__main__':
    driver()

