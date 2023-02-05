import cv2
import requests
import json 
import numpy as np
import pickle, json 
import time

cap = cv2.VideoCapture('ff.mp4')
li = []
url = 'http://obj-detection-deployment-5-service:8001/send_data'

while True:
    ret, frame = cap.read()
    if ret == True:
        data_pickled = pickle.dumps(frame)
        print(frame)
        response = requests.post(url, data = data_pickled)
        print(response)
    else: 
        break

