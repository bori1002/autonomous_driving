import dlib

predictor_file = "shape_predictor_68_face_landmarks.dat" #https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 에서 다운로드 가능
face_detector = dlib.get_frontal_face_detector() #얼굴 검출기
shape_predictor = dlib.shape_predictor(predictor_file) #얼굴 좌표표시

face_detection = face_detector("face_image/face_img1.JPG") #얼굴 검출
for f in face_detection:
	shape = shape_predictor("face_image/face_img1.JPG", f) #68개의 좌표(68*2 사이즈)의 데이터가 저장