import dlib

face_detector = dlib.get_frontal_face_detector()
face_detection = face_detector(test_img)

for f in face_detection:
	cv2.rectangle(test_img, (f.left(), f.top()), (f.right(), f.bottom()), (0, 0, 255), 4)