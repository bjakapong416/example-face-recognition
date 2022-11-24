from faceVerification_deepface import DeepFace

f1 = "img1.jpg"
f2 = "img1.jpg"

# backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
# result = DeepFace.verify(img1_path=f1, img2_path=f2, detector_backend=backends[1])

result = DeepFace.verify(img1_path = f1, img2_path = f2)

print(result)