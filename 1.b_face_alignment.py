import math
import cv2
import numpy as np
from deepface.commons import distance
from deepface.detectors import FaceDetector
from PIL import Image
import imutils

def build_model():
	from mtcnn import MTCNN
	face_detector = MTCNN()
	return face_detector

def getLeftEyeRightEye(face_detector, img):
	resp = []

	detected_face = None
	img_region = [0, 0, img.shape[1], img.shape[0]]

	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #mtcnn expects RGB but OpenCV read BGR
	detections = face_detector.detect_faces(img_rgb)

	if len(detections) > 0:

		for detection in detections:
			x, y, w, h = detection["box"]
			detected_face = img[int(y):int(y+h), int(x):int(x+w)]
			img_region = [x, y, w, h]
			confidence = detection["confidence"]
			keypoints = detection["keypoints"]
			left_eye = keypoints["left_eye"]
			right_eye = keypoints["right_eye"]

			# if align:
			# 	keypoints = detection["keypoints"]
			# 	left_eye = keypoints["left_eye"]
			# 	right_eye = keypoints["right_eye"]
			# 	detected_face = FaceDetector.alignment_procedure(detected_face, left_eye, right_eye)

			# resp.append((detected_face, img_region, confidence))

	return left_eye, right_eye


def alignment_procedure(img, left_eye, right_eye):

	#this function aligns given face in img based on left and right eye coordinates

	left_eye_x, left_eye_y = left_eye
	right_eye_x, right_eye_y = right_eye

	#-----------------------
	#find rotation direction

	if left_eye_y > right_eye_y:
		point_3rd = (right_eye_x, left_eye_y)
		direction = -1 #rotate same direction to clock
	else:
		point_3rd = (left_eye_x, right_eye_y)
		direction = 1 #rotate inverse direction of clock

	#-----------------------
	#find length of triangle edges

	a = distance.findEuclideanDistance(np.array(left_eye), np.array(point_3rd))
	b = distance.findEuclideanDistance(np.array(right_eye), np.array(point_3rd))
	c = distance.findEuclideanDistance(np.array(right_eye), np.array(left_eye))

	#-----------------------

	#apply cosine rule

	if b != 0 and c != 0: #this multiplication causes division by zero in cos_a calculation

		cos_a = (b*b + c*c - a*a)/(2*b*c)
		angle = np.arccos(cos_a) #angle in radian
		angle = (angle * 180) / math.pi #radian to degree

		#-----------------------
		#rotate base image

		if direction == -1:
			angle = 90 - angle

		img = Image.fromarray(img)
		img = np.array(img.rotate(direction * angle))

	#-----------------------

	return img #return img anyway


face_detector = build_model()
img = cv2.imread("output/detected_face.jpg")
leftEye, rightEye = getLeftEyeRightEye(face_detector= face_detector, img=img)

alignedFace = alignment_procedure(img=img, left_eye=leftEye, right_eye=rightEye)
alignedFace = imutils.resize(alignedFace, width=224)
cv2.imwrite("output/aligned_face.jpg", alignedFace)