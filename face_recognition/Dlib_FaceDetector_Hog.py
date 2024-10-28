import dlib
import cv2

image_path = "face_recognition/face_image/face_img1.JPG"
image = cv2.imread(image_path)

face_detector = dlib.get_frontal_face_detector()
face_detection = face_detector(image)

for f in face_detection:
	cv2.rectangle("face_recognition/face_image/face_img1.JPG", (f.left(), f.top()), (f.right(), f.bottom()), (0, 0, 255), 4)