# import necessary library
import requests
import pprint
import json

# parameters for calling ai service
HOST_IP = "xxxxxxx"
PORT = "xxxxx"
image01Path = "xxxxx.jpg"
image02Path = "xxxxx.jpg"
endpoint = "/CompareFace"

request_form = {
  "ImageA": open(image01Path, "rb"),
  "ImageB": open(image02Path, "rb")
}

# calling ai service function
response = requests.post(f'http://{HOST_IP}:{PORT}{endpoint}', files=request_form)

# response and results in json format
print(response.status_code)
pprint.pprint(response.json())