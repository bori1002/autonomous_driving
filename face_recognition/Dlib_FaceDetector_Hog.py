import dlib
import cv2

face_detector = dlib.get_frontal_face_detector()
face_detection = face_detector("face_image/face_img1.JPG")

for f in face_detection:
	cv2.rectangle("face_image/face_img1.JPG", (f.left(), f.top()), (f.right(), f.bottom()), (0, 0, 255), 4)