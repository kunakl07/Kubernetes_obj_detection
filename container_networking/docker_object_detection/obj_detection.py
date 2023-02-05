from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
import matplotlib.pyplot as plt
import cv2
import requests
import numpy as np
import codecs
import pickle


app = Flask(__name__)
api = Api(app)
status = 'busy'
file_name = 'labels.txt'


config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model, config_file)
classLabels = []
nurl = 'http://frame-combination-deployment-service-2:8082/frame_combination'


with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
   
   
model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
font = cv2.FONT_HERSHEY_PLAIN
font_scale = 3

@app.route("/send_data", methods = ["POST"])
def post():
    global status
    pdata = request.data
    frame = pickle.loads(pdata)

    status = 'busy'
    ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.7)        
    if len(ClassIndex)!=0:
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            if ClassInd<=80:
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0]+10, boxes[1]+40), font, fontScale=font_scale, color = (0, 255, 0), thickness = 3)
    print(frame)

    status = 'ready'
    data_pickled_again = pickle.dumps(frame)
    try:
        response = requests.post(nurl, data = data_pickled_again)
        response.raise_for_status()
        print('Data sent to third API successfully')
    except requests.exceptions.RequestException as e:
        print('Error sending data to third API:', e)


    # response = requests.post(nurl, data = data_pickled_again)
    # print(response)x
    get()
    #cv2.imshow('Obj detection', frame)
    return jsonify({'status': 'success'})

def get():
    global status
    return jsonify({'status': status})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
