#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import mediapipe as mp
import time
import numpy as np
from collections import OrderedDict
import tf
import rospy

mp_pose = mp.solutions.pose
mp_face_mesh=mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
draw_spec=mp_drawing.DrawingSpec(thickness=2,circle_radius=1,color=[66,77,229])
landmark_drawing_spec=mp_drawing.DrawingSpec(thickness=1,circle_radius=2,color=[66,77,229])

connection_drawing_spec=mp_drawing.DrawingSpec(thickness=2,circle_radius=1,color=[233,155,6])

rospy.init_node('tf_test_node')
br = tf.TransformBroadcaster()


FACIAL_LANDMARKS_68_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17))
])

model=mp_face_mesh.FaceMesh(
    static_image_mode=False,
    refine_landmarks=True,
    max_num_faces=5,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

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
        cv2.putText(image, "center", (NL_X+2, NL_Y-10),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)

        NR = results.multi_face_landmarks[0].landmark[358];
        NR_X, NR_Y = int(NR.x * w), int(NR.y * h);
        NR_Color = (255, 255, 255)
        img = cv2.circle(img, (NR_X-17, NR_Y), 3, NR_Color, -1)
        cv2.putText(image, "center", (NR_X-25, NR_Y-10),
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


cap = cv2.VideoCapture(1)
with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
            ) as holistic:
    while not rospy.is_shutdown():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        h, w, c = image.shape

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        frame = process_frame(image)
        cv2.imshow('my_window', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break
        xl = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x + 0.005
        xr = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x - 0.005
        yn = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y - 0.005
        zn = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z - 0.005

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
                br.sendTransform((xl,yn,zn),
				tf.transformations.quaternion_from_euler(0,0,0),
				rospy.Time.now(),"world","test") 


cap.release()
