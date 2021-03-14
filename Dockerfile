FROM python:3.8-slim

WORKDIR code-directory

# Install necessary packages
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get -y install vim
RUN apt-get -y install jq
RUN apt-get -y install curl
RUN apt-get -y install unzip
# RUN apt-get -y install gcc python3.7-dev

# Install necessary packages
RUN pip install cerberus
RUN pip install Pandas3
RUN pip install PyYAML
RUN pip install behave-py3
RUN pip install coverage
RUN pip install requests
RUN pip install opencv-python
RUN pip install flask
RUN pip install Pillow
RUN pip install numpy

EXPOSE 5000

COPY ./ ./
CMD [ "python", "./api.py" ]
