# Base layer (one time build/always cache)
FROM python:3.8.13 as base
WORKDIR /usr/src/app

RUN apt-get update

RUN apt install -y libgl1-mesa-glx

COPY . /usr/src/app/
# COPY requirements.txt /usr/src/app/requirements.txt
# RUN python3 -m venv venv
# RUN source ./venv/bin/activate


RUN python3 -m pip install -r requirements.txt

# App layer (Update app/always rebuild)
FROM base as app
# Single file can copy in batch
# COPY Classification ./Classification
# COPY Detection ./Detection
# COPY LineNotification.py /usr/src/app/LineNotification.py

#Source code encryption
#RUN python3 -c "from vam import encrypt; encrypt()"

# runtime later (Deflate app layer/always rebuild)
FROM base as runtime
LABEL maintainer="p.sovatha@vamstack.com"
# COPY --from=app /usr/src/app /usr/src/app