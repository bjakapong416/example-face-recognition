# import necessary library
import requests
import pprint
import json

# parameters for calling ai service
HOST_IP = "http://58.137.58.164/"
PORT = "8500"
imagePath = "xxxxx.jpg"


endpoint = "/SearchFace"
top_k = 5
request_form = {
  "Image": open(imagePath, "rb")
}

# url = f"http://58.137.58.164:8500/SearchFace?top_k=5" 
url = f'http://{HOST_IP}:{PORT}{endpoint}?top_k={top_k}'

# calling ai service function
response = requests.post(url, files=request_form)

# response and results in json format
print(response.status_code)
pprint.pprint(response.json())