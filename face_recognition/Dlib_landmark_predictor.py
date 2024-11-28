import dlib
import cv2

image_path = "face_image/face_img1.JPG"
image = cv2.imread(image_path)

predictor_file = "shape_predictor_68_face_landmarks.dat" #https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 에서 다운로드 가능
face_detector = dlib.get_frontal_face_detector() #얼굴 검출기
shape_predictor = dlib.shape_predictor(predictor_file) #얼굴 좌표표시

face_detection = face_detector(image) #얼굴 검출
for f in face_detection:
	shape = shape_predictor(image, f) #68개의 좌표(68*2 사이즈)의 데이터가 저장