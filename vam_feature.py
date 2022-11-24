# import necessary library
import requests
import pprint
import json

# parameters for calling ai service
HOST_IP = "xxxxx"
PORT = "xxxx"
IMAGE_PATH = "img1.jpg"
endpoint = "/FaceFeature"

# imagepath
request_form = {"Image": open(IMAGE_PATH, "rb")}

# calling ai service function
response = requests.post(f'http://{HOST_IP}:{PORT}{endpoint}', files=request_form)

# response and results in json format
# print(response.status_code)
# pprint.pprint(response.json())

data = response.json()
print(data["face_feature"])