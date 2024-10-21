#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import cv2
import mediapipe as mp
import time
import numpy as np
from collections import OrderedDict
from sensor_msgs.msg import Image, RegionOfInterest
from cv_bridge import CvBridge, CvBridgeError

class faceDetector:
    def __init__(self):
        # rospy.on_shutdown(self.cleanup);

        # 创建cv_bridge
        self.bridge = CvBridge()
        # rospy.Publisher(“/topic_name”, message_type, queue_size=size)
        # /topic_name表示发布者向这个topic发布消息。message_type表示发布到话题中消息的类型。
        self.image_pub = rospy.Publisher("cv_bridge_image", Image, queue_size=1)
	#self.image_pub = rospy.Publisher("cv_bridge_image", Image, queue_size=1)
        self.color = (50, 255, 50)
        cap = cv2.VideoCapture(1)
        # 初始化订阅rgb格式图像数据的订阅者，此处图像topic的话题名可以在launch文件中重映射
        self.image_sub = rospy.Subscriber("input_rgb_image", Image, self.image_callback, queue_size=1)

    Cap = cv2.VideoCapture(0)
    def image_callback(self, data, cap=Cap):
        # 使用cv_bridge将ROS的图像数据转换成OpenCV的图像格式
        try:
            image = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
            #image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            frame = np.array(image, dtype=np.uint8)
        except CvBridgeError as e:
            print  (e)


        with mp_holistic.Holistic(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
        ) as holistic:
            while cap.isOpened():
                #success, image = cap.read()
                #f not success:
                 #   print("Ignoring empty camera frame.")
                 #   continue

                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = holistic.process(image)
                h, w, c = image.shape

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # there img

                frame = self.process_frame(image)
                # 在窗口输出图片
                self.image_pub.publish(self.bridge.cv2_to_imgmsg(image, "bgr8"))
                cv2.imshow('my_window', frame)
                cv2.imshow('my_window2', image)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
                xl = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x + 0.005
                xr = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x - 0.005
                yn = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y - 0.005
                zn = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z - 0.005


# use？
    def shape_to_np(shape, dtype="int"):
        coords = np.zeros((shape.num_parts, 2), dtype=dtype)

        for i in range(0, shape.num_parts):
            coords[i] = (shape.part(i).x, shape.part(i).y)
        return coords

    def process_frame(img):
        start_time = time.time()
        scaler = 1
        scaler = 1
        radius = 12
        lw = 2
        scaler = 1
        h, w = img.shape[0], img.shape[1]
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = model.process(img_RGB)
        if results.multi_face_landmarks:
            NL = results.multi_face_landmarks[0].landmark[129];
            NL_X, NL_Y = int(NL.x * w), int(NL.y * h);
            NL_Color = (255, 255, 255)
            img = cv2.circle(img, (NL_X+17, NL_Y), 3, NL_Color, -1)
            cv2.putText(img, "center", (NL_X+2, NL_Y-10),
                         cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)

            NR = results.multi_face_landmarks[0].landmark[358];
            NR_X, NR_Y = int(NR.x * w), int(NR.y * h);
            NR_Color = (255, 255, 255)
            # 画圆圈，-1处为圆圈大小
            img = cv2.circle(img, (NR_X-17, NR_Y), 3, NR_Color, -1)
            cv2.putText(img, "center", (NR_X-25, NR_Y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)
        else:
            img = cv2.putText(img, 'NO FACE DELECTED', (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.25,
                             (218, 112, 214), 1, 8)
        end_time = time.time()
        FPS = 1/(end_time - start_time)
        scaler = 1
        img = cv2.putText(img, 'FPS' + str(int(FPS)), (25 * scaler, 700 * scaler), cv2.FONT_HERSHEY_SIMPLEX,
                             1.25 * scaler, (0, 0, 255), 1, 8)
        return img



    def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):

        overlay = image.copy()
        output = image.copy()

        if colors is None:
            colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
                      (168, 100, 168), (158, 163, 32),
                      (163, 38, 32), (180, 42, 220)]

        for (i, name) in enumerate(FACIAL_LANDMARKS_68_IDXS.keys()):

            (j, k) = FACIAL_LANDMARKS_68_IDXS[name]
            pts = shape[j:k]

            if name == "jaw":
                for l in range(1, len(pts)):
                    ptA = tuple(pts[l - 1])
                    ptB = tuple(pts[l])
                    cv2.line(overlay, ptA, ptB, colors[i], 2)
            else:
                hull = cv2.convexHull(pts)
                cv2.drawContours(overlay, [hull], -1, colors[i], -1)

        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
        return output


        def count_exception(sumSamples, mobidity, x):
            f = (sumSamples // x) * (1 * (1 - mobidity) ** x + (x + 1) * (1 - (1 - mobidity) ** x))
            return f


        def max_numGroup(sumSamples, mobidity, rate):
            factors = [factor for factor in range(2, 100)]
            max_numEachGroup = 0
            for i in factors:
                test_rate = count_exception(sumSamples, mobidity, i) // sumSamples

                if test_rate > rate:
                    max_numEachGroup = i
                    break
                else:
                    max_numEachGroup = i
            return max_numEachGroup
        with mp_pose.Pose(
                static_image_mode=False, min_detection_confidence=0.5, model_complexity=1) as pose:
                print('Left NOSE world landmark--',"x:",xl,"y:",yn,"z:",zn)
                print('Right NOSE world landmark--', "x:", xr, "y:", yn, "z:", zn)
                print(" ")

        def cleanup(self):
            print
            "Shutting down vision node."
            cv2.destroyAllWindows()

    Cap.release()
if __name__ == '__main__':
    try:
        mp_pose = mp.solutions.pose
        mp_face_mesh = mp.solutions.face_mesh
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_holistic = mp.solutions.holistic
        draw_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1, color=[66, 77, 229])
        landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=2, color=[66, 77, 229])

        connection_drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1, color=[233, 155, 6])

        FACIAL_LANDMARKS_68_IDXS = OrderedDict([
            ("mouth", (48, 68)),
            ("right_eyebrow", (17, 22)),
            ("left_eyebrow", (22, 27)),
            ("right_eye", (36, 42)),
            ("left_eye", (42, 48)),
            ("nose", (27, 36)),
            ("jaw", (0, 17))
        ])

        model = mp_face_mesh.FaceMesh(
            static_image_mode=False,
            refine_landmarks=True,
            max_num_faces=5,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

        # 初始化ros节点
        rospy.init_node("face_detector")
        faceDetector()
        rospy.loginfo("Face detector is started..")
        rospy.loginfo("Please subscribe the ROS image.")
        rospy.spin()
    except KeyboardInterrupt:
        print
        "Shutting down face detector node."
        cv2.destroyAllWindows()
