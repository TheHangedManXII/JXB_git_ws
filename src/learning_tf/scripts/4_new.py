#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 导入各种包
import cv2
import mediapipe as mp
import time
import numpy as np
import math
import csv

import tf
import rospy
from geometry_msgs.msg import Twist
from learning_tf.msg import Person
# 类型转换函数

Distance_H, angle_d, angle_rad = 0,0,0


# 帧处理函数
def Cacurlater(results, image_RGB):
    global Distance_H, angle_d, angle_rad,count_flag1
      # 计数变量1,存储数据计数
    h, w, c = image_RGB.shape
    centre_x, centre_y, centre_z = 0, 0, 0
    centre_X, centre_Y, centre_Z = 0, 0, 0
    angle_rad = 0
    scale = 1
    NL_Color = (255, 255, 255)
    if results.face_landmarks:
        detect_flag = 1
        # 使用面网获取嘴部中心坐标，用于绘图展示，下同
        NL = results.face_landmarks.landmark[13]
        ML = results.face_landmarks.landmark[14]
        NL_X, NL_Y = int(NL.x * w), int(NL.y * h)
        ML_X, ML_Y = int(ML.x * w), int(ML.y * h)
        Distance_H = abs(NL.y - ML.y)
        centre_X, centre_Y, centre_Z = int((NL_X + ML_X) / 2), int((NL_Y + ML_Y) / 2), float((NL.z + ML.z) / 2)
        centre_x, centre_y, centre_z = float((NL.x + ML.x) / 2), float((NL.y + ML.y) / 2), float((NL.z + ML.z) / 2)
        try:
        # pose_right_eye
            Ey = results.pose_landmarks.landmark[5].y
            Ez = results.pose_landmarks.landmark[5].z
            # pose_nose
            Ny = results.pose_landmarks.landmark[0].y
            Nz = results.pose_landmarks.landmark[0].z
            Long_E2N = ((Ey - Ny) * (Ey - Ny) + (Nz - Ez) * (Ey - Ny)) ** 0.5
            Z_E2N = abs(Ez - Nz)
            Y_E2N = abs(Ey - Ny)
            cos_E2N = float(Y_E2N / Long_E2N)
        except Exception:
            cos_E2N = 0
        # 注意：角度正确性判断，当角度检测错误时，为避免程序退出，会输出0
        if (cos_E2N >= -1) & (cos_E2N <= 1):
            angle_rad = math.acos(cos_E2N)
        else:
            pass
        angle_d = math.degrees(angle_rad)
        # yi = time.strftime("%S", time.localtime())
        count_flag1 += 1

        image_RGB = cv2.circle(image_RGB, (centre_X, centre_Y), 3, NL_Color, -1)

        cv2.putText(image_RGB, "center", (centre_X + 2, centre_Y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)

        # right nose
        '''
        NR = results.multi_face_landmarks[0].landmark[358];
        NR_X, NR_Y = int(NR.x * w), int(NR.y * h);
        NR_Color = (255, 255, 255)
        img = cv2.circle(img, (NR_X - 17, NR_Y), 3, NR_Color, -1)
        cv2.putText(image, "center", (NR_X - 25, NR_Y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)
        '''

        scale = 1

    # 未检测到人脸输出NO FACE DETECTED
    else:
        detect_flag = 0
        image_RGB = cv2.putText(image_RGB, 'NO FACE DETECTED', (25 * scale, 50 * scale), cv2.FONT_HERSHEY_SIMPLEX, 1.25,
                                (0, 128, 255), 1, 30)
        end_time = time.time()  # 获取处理完毕时间
        fps = 1 / (end_time - start_time)  # 得到帧数
        scale = 1
        image_RGB = cv2.putText(image_RGB, 'FPS:' + str(int(fps)), (25 * scale, 80 * scale), cv2.FONT_HERSHEY_SIMPLEX,
                                0.7,
                                (0, 0, 255), 1, 30)

    image_BGR = cv2.cvtColor(image_RGB, cv2.COLOR_RGB2BGR)
    return image_BGR, centre_x, centre_y, centre_z





if __name__ == '__main__':
    try:
        # 初始化ros节点

        rospy.init_node('tf_test_node', anonymous=True)
        br = tf.TransformBroadcaster()
        tf_pub = rospy.Publisher('mytf_person', Person, queue_size=1)

        cap = cv2.VideoCapture(1)
        mp_pose = mp.solutions.pose  # 位置函数
        mp_face_mesh = mp.solutions.face_mesh  # 面网函数，获取面网用于绘图
        mp_drawing = mp.solutions.drawing_utils  # 绘图函数

        mp_holistic = mp.solutions.holistic  # 框架
        draw_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1, color=[66, 77, 229])  # 画笔之类的定义
        landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=2, color=[66, 77, 229])
        connection_drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1, color=[233, 155, 6])
        # 提前定义模型参数

        model = mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        detect_flag = 0  # 自己设定的判断标志，防止程序退出
        count_flag1 = 0
        # empty_static = np.empty(shape=[0,4],dtype=int)  # 创建空4维数组，用于清空数据
        temp_static = np.empty(shape=[0, 4], dtype=int)  # 创建空4维数组，用于存放数据
        xl_ = yn_ = zn_ = angle_d_ = 0  # 数据平均值

        cap = cv2.VideoCapture(0)
        with mp_holistic.Holistic(
                min_detection_confidence=0.6,
                min_tracking_confidence=0.6

        ) as holistic:
            while cap.isOpened():
                detect_flag, scale = 1, 1
                centre_X, centre_Y, centre_Z, Distance_H = 0, 0, 0, 0

                success, image = cap.read()
                # 镜像
                image = cv2.flip(image, 1)
                start_time = time.time()  # 获取开始处理时间
                if not success:
                    print("Ignoring empty camera frame.")
                    break

                image.flags.writeable = False
                # cv2.normalize(image, image, 0, 1, cv2.NORM_MINMAX)
                image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = holistic.process(image_RGB)
                image.flags.writeable = True

                image_BGR, centre_x, centre_y, centre_z = Cacurlater(results=results, image_RGB=image_RGB)

                if (cv2.waitKey(5) & 0xFF == 27):  # ESC退出
                    print("退出")
                    break
                    # 有时会存在'NoneType' object has no attribute 'landmark'情况，改为此
                try:
                    end_time = time.time()  # 获取处理完毕时间
                    fps = 1 / (end_time - start_time)
                    image_BGR = cv2.putText(image_BGR, 'FPS:' + str(int(fps)), (25, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                        (0, 0, 255), 1, 30)
                    cv2.imshow('my_window', image_BGR)

                    # tf ——set
                    br.sendTransform(((centre_z * 15), (centre_x - 0.5), -(centre_y - 0.9)),
                                        tf.transformations.quaternion_from_euler(0, 0, 0),
                                        rospy.Time.now(), "centre", "seat")
                    if (detect_flag & (count_flag1 % 5== 0)):
                        person_msg = Person()
                        person_msg.name = "tf"
                        person_msg.x = centre_z * 15
                        person_msg.y = (centre_x - 0.5)
                        person_msg.z = -(centre_y - 0.9)
                        person_msg.r = 0
                        person_msg.p = 0
                        person_msg.w = 0
                        tf_pub.publish(person_msg)
                        print('centre house world landmark--', "x:",  (centre_x - 0.5), "y:",-(centre_y - 0.9), "z:", centre_z * 15)
                        print("角度：", float(angle_d))
                        # rospy.loginfo("弧度：%lf", math.radians(float(angle_d)))

                    else:
                        pass
                except Exception as e:
                    rospy.loginfo('Some error happened:', e)
                    image_BGR = cv2.putText(image_BGR, 'Angle calculation failure', (25, 50),
                                            cv2.FONT_HERSHEY_SIMPLEX, 1.25,
                                            (0, 128, 255), 1, 30)
                    angle_rad = 0
                    angle_d = math.degrees(angle_rad)
                    # yi = time.strftime("%S", time.localtime())

        cap.release()
    except KeyboardInterrupt:
        rospy.loginfo("Shutting down face detector node.")
        cv2.destroyAllWindows()
        cap.release()

