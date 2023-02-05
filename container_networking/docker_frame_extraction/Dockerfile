FROM python:3.8-slim
WORKDIR /app

COPY . /app
COPY ff.mp4 /app
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install opencv-python-headless requests numpy
CMD ["python", "frame_extraction.py"]