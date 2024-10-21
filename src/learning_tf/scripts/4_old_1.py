#!/usr/bin/env python3
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


# 初始化ros节点
rospy.init_node('tf_ss_node')
br = tf.TransformBroadcaster()


# 定义要使用的函数
mp_pose = mp.solutions.pose  # 位置函数
mp_face_mesh = mp.solutions.face_mesh  # 面网函数，获取面网用于绘图
mp_drawing = mp.solutions.drawing_utils  # 绘图函数
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic  # 框架
draw_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1, color=[66, 77, 229])  # 画笔之类的定义
landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=2, color=[66, 77, 229])
connection_drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1, color=[233, 155, 6])
# 提前定义模型参数
model = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    refine_landmarks=True,
    max_num_faces=5,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)
detect_flag = 0  # 自己设定的判断标志，防止程序退出
count_flag1 = 0  # 计数变量1,存储数据计数
count_flag2 = 0  # 计数变量2，转换数据计数
Write_Freq = 20  # csv文件转换频率，每20个数据转换一次
avg_freq = 5  # 平均计算频率
# empty_static = np.empty(shape=[0,4],dtype=int)  # 创建空4维数组，用于清空数据
temp_static = np.empty(shape=[0, 4], dtype=int)  # 创建空4维数组，用于存放数据
xl_ = yn_ = zn_ = angle_d_ = 0  # 数据平均值


# 类型转换函数
def shape_to_np(shape, dtype="int"):
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)

    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


# 帧处理函数
def process_frame(img):
    global detect_flag
    start_time = time.time()  # 获取开始处理时间
    radius = 12
    lw = 2
    scale = 1
    h, w = img.shape[0], img.shape[1]
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model.process(img_RGB)
    if results.multi_face_landmarks:

        detect_flag = 1
        # 使用面网获取左鼻孔中心坐标，用于绘图展示，下同
        NL = results.multi_face_landmarks[0].landmark[129];
        NL_X, NL_Y = int(NL.x * w), int(NL.y * h);
        NL_Color = (255, 255, 255)
        img = cv2.circle(img, (NL_X + 17, NL_Y), 3, NL_Color, -1)
        cv2.putText(image, "center", (NL_X + 2, NL_Y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)
        '''
        NR = results.multi_face_landmarks[0].landmark[358];
        NR_X, NR_Y = int(NR.x * w), int(NR.y * h);
        NR_Color = (255, 255, 255)
        img = cv2.circle(img, (NR_X - 17, NR_Y), 3, NR_Color, -1)
        cv2.putText(image, "center", (NR_X - 25, NR_Y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)
        '''
    # 未检测到人脸输出NO FACE DETECTED
    else:
        detect_flag = 0
        img = cv2.putText(img, 'NO FACE DETECTED', (25 * scale, 50 * scale), cv2.FONT_HERSHEY_SIMPLEX, 1.25,
                          (0, 128, 255), 1, 30)
    end_time = time.time()  # 获取处理完毕时间
    fps = 1 / (end_time - start_time)  # 得到帧数
    scale = 1
    img = cv2.putText(img, 'FPS:' + str(int(fps)), (25 * scale, 80 * scale), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                      (0, 0, 255), 1, 30)
    return img


# 输出文件函数，仅输出4个量，左鼻孔xyz和角度
def Output_Csv(xl, yn, zn, angle_d):
    global count_flag2
    filename = 'pose.txt'  # 设定文件名字符串
    # ’a‘打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
    # 新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    test = open(filename, 'a')
    # print('坐标', ",", xl, ",", yn, ",", zn, ",", xr, ",", yn, ",", zn, ",", angle_d, file=test)
    print('坐标', ",", xl, ",", yn, ",", zn, ",", angle_d, file=test)
    count_flag2 += 1
    test.close()

    if count_flag2 % Write_Freq == 0:  # 控制写入频率
        count_flag = 1
        out = open('pose.csv', 'w', newline='')
        csv_writer = csv.writer(out, dialect='excel')

        f = open("pose.txt", "r")
        for line in f.readlines():
            line = line.replace(',', '\t')  # 将每行的逗号替换成空格
            stc_list = line.split()  # 将字符串转为列表，从而可以按单元格写入csv
            csv_writer.writerow(stc_list)


cap = cv2.VideoCapture(1)
with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False
        # cv2.normalize(image, image, 0, 1, cv2.NORM_MINMAX)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        h, w, c = image.shape

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        frame = process_frame(image)
        cv2.imshow('my_window', frame)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC退出
            break
        if detect_flag:
            xl = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x + 0.005
            # xr = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x - 0.005
            yn = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y - 0.005
            zn = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z - 0.005
            with mp_pose.Pose(
                    static_image_mode=False, min_detection_confidence=0.5, model_complexity=1) as pose:
                Ey = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].y
                Ez = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].z
                Ny = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
                Nz = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z
                Long_E2N = ((Ey - Ny) * (Ey - Ny) + (Nz - Ez) * (Ey - Ny)) ** 0.5
                Z_E2N = abs(Ez - Nz)
                Y_E2N = abs(Ey - Ny)
                cos_E2N = float(Y_E2N / Long_E2N)
                # 注意：角度正确性判断，当角度检测错误时，为避免程序退出，会输出0
                if (cos_E2N >= -1) & (cos_E2N <= 1):
                    angle_rad = math.acos(cos_E2N)
                else:
                    angle_rad = 0
                angle_d = math.degrees(angle_rad)
                yi = time.strftime("%S", time.localtime())
            count_flag1 += 1
            if count_flag1 % avg_freq == 0:
                print('Left NOSE world landmark--', "x:", xl, "y:", yn, "z:", zn)
                # print('Right NOSE world landmark--', "x:", xr, "y:", yn, "z:", zn)
                print("角度：", float(angle_d))
                print(" ")
                for i in temp_static[:, 0]:  # 求和
                    xl_ = xl_ + i
                for i in temp_static[:, 1]:
                    yn_ = yn_ + i
                for i in temp_static[:, 2]:
                    zn_ = zn_ + i
                for i in temp_static[:, 3]:
                    angle_d_ = angle_d_ + i
                xl_ = xl_ / count_flag1     # 取平均
                yn_ = yn_ / count_flag1
                zn_ = zn_ / count_flag1
                angle_d_ = angle_d_ / count_flag1
                Output_Csv(xl_, yn_, zn_, angle_d_)  # 数据写入
                count_flag1 = 0  # 数据归零
                xl_ = yn_ = zn_ = angle_d_ = 0
                temp_static = np.empty(shape=[0, 4], dtype=int)
            else:
                temp_static = np.append(temp_static, [[xl, yn, zn, angle_d]], axis=0)

cap.release()

