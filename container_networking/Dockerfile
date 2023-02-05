FROM python:3.7-slim
EXPOSE 8081
COPY ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt /app
COPY frozen_inference_graph.pb /app
COPY labels.txt /app
COPY your_script_name.py /app
WORKDIR /app
RUN pip install opencv-python-headless
RUN pip install Flask
RUN pip install flask_restful
RUN pip install json
RUN pip install matplotlib
RUN pip install numpy
RUN pip install requests
RUN pip install codecs
CMD ["python", "obj_detection.py"]
