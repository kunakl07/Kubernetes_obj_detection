
FROM python:3.8-slim
# Install system packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#       bzip2 \
#       g++ \
#       git \
#       graphviz \
#       libgl1-mesa-glx \
#       libhdf5-dev \
#       openmpi-bin \
#       wget \
#       python3-tk && \
#     rm -rf /var/lib/apt/lists/*

# COPY . /app
# COPY frame_combination.py /app

# WORKDIR /app
# RUN pip install --upgrade pip

# RUN pip install matplotlib
# RUN pip install numpy
# RUN pip install requests

# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# RUN pip install opencv-python==4.0.0.21
# RUN pip install Flask
# RUN pip install flask_restful
# RUN pip install numpy
# RUN pip install requests



# # Minimize image size 
# RUN (apt-get autoremove -y; \
#      apt-get autoclean -y)
# ENV QT_X11_NO_MITSHM=1
# CMD ["bash"]








EXPOSE 8082


COPY . /app
COPY frame_combination.py /app

WORKDIR /app
RUN pip install matplotlib
RUN pip install numpy
RUN pip install requests

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install opencv-python --upgrade
RUN pip install Flask
RUN pip install flask_restful
RUN pip install numpy
RUN pip install requests

EXPOSE 8082

CMD ["python", "frame_combination.py"]
