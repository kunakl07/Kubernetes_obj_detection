FROM python:3.8.8
EXPOSE 8081

COPY  . /app

COPY ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt /app
COPY frozen_inference_graph.pb /app
COPY labels.txt /app
COPY obj_detection.py /app
WORKDIR /app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install opencv-python
RUN pip install Flask
RUN pip install flask_restful
RUN pip install matplotlib
RUN pip install numpy
RUN pip install requests
CMD ["python", "obj_detection.py"]
