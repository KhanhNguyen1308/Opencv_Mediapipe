import cv2
import time
import numpy as np
import mediapipe as mp
from threading import Thread
from mode import sleep_mode, color_text
from head_pose_ratio import head_pose_ratio
from function import play_sound, draw_point, eye_avg_ratio, put_text
from head_pose import gat_dau, head_pose_status, eye_stat

wav_path = '/home/pi/Documents/Drowsy_detect/alarm.wav'
m, t, dem , ear, count, blink, pTime, gat_num, blink_perM, time_active, prev_status = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
status = ''
eye_status = ''
x_status = ''
y_status = ''
z_status = ''
head_status = ''
Drowsy_mode = ''
z = ''
draw = False
f = open('Text/n.txt', 'w+')
a = open('Text/c1.txt', 'w+')
b = open('Text/c2.txt', 'w+')
start_time = time.time()
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)
# cap = cv2.VideoCapture("Video/Thang_Cui.mp4")
cap = cv2.VideoCapture("Video/Video_test.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# wav_path = "/home/pi/Documents/Drowsy_detect/alarm.wav"
alarm = False
i = 0
while True:
    ret, img = cap.read()
    key = cv2.waitKey(1)
    ih, iw = img.shape[0], img.shape[1]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        Mount = []
        Left_eye = []
        Right_eye = []
        try:
            for face_lms in results.multi_face_landmarks:
                for lm in face_lms.landmark:
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])

            nose = face[5]
            Left_eye.append([face[249], face[374], face[380], face[382], face[385], face[386]])
            Right_eye.append([face[7], face[145], face[153], face[155], face[158], face[159]])
            Mount.append([face[308], face[317], face[14], face[87], face[61], face[82], face[13], face[312]])
            img = draw_point(img, nose, Left_eye, Right_eye, Mount)
            ear = eye_avg_ratio(Left_eye, Right_eye)
            n_ratio_1, n_ratio_2, c_ratio_1, c_ratio_2, x5, x6 = head_pose_ratio(nose, Left_eye, Right_eye)
            head_status, mode = head_pose_status(round(n_ratio_1,3), round(n_ratio_2,3),round(c_ratio_1,3),round(c_ratio_2,3))
            z = str(round(n_ratio_1,3)) + "   " + str(round(n_ratio_2,3)) + "   " + str(round(c_ratio_1,3)) + "   " + str(round(c_ratio_2,3))
            if key == ord('a'):
                print(z)
            # eye_status, blink, count, alarm = eye_stat(ear, count, blink, mode, alarm)
            # gat_num, dem, prev_status = gat_dau(prev_status, mode, dem, gat_num)
            f.write(str(round(n_ratio_1,3))+"\n")
            a.write(str(round(c_ratio_1,3))+"\n")
            b.write(str(round(c_ratio_2,3))+"\n")
            # if alarm == True:
            #     t = Thread(target=play_sound, args=(wav_path,))
            #     t.deamon = True
            #     t.start()
            m+=1
            # if m >4000:
            #     f.write(str(round(ear,3))+"\n")
            color = (0, 255, 0)
        except Exception:
            print("loi: " + z)
            color = (255, 0, 0)
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    cv2.putText(img, str(fps), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    cv2.putText(img, "Tu the: " + head_status, (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    pTime = cTime
    cv2.imshow('results', img)
    if m == 4000:
        f.close()
        break
    if key == ord('a'):
        print(z)
    if key == ord('q'):
        f.close()
        break

f.close()
cap.release()
cv2.destroyAllWindows()
