import cv2
import face_recognition

# 加载已知人脸图像
known_image = face_recognition.load_image_file("known_person.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# 初始化视频捕捉
video_capture = cv2.VideoCapture(0)

while True:
    # 捕捉视频中的每一帧
    ret, frame = video_capture.read()

    # 将捕获的图像从BGR转换为RGB
    rgb_frame = frame[:, :, ::-1]

    # 查找视频帧中的所有人脸和人脸编码
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 与已知人脸进行比对
        matches = face_recognition.compare_faces([known_encoding], face_encoding)

        name = "Unknown"

        # 如果找到匹配，使用已知人脸的名称
        if True in matches:
            name = "Known Person"

        # 在图像上标记人脸
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # 显示视频帧
    cv2.imshow('Video', frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头和窗口
video_capture.release()
cv2.destroyAllWindows()
cv2.waitKey()123
44444444