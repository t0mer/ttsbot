FROM ubuntu:18.04

LABEL maintainer="tomer.klein@gmail.com"
RUN apt update
RUN apt install python3-pip --yes
RUN pip3 install telepot requests pyttsreverso --no-cache-dir

ENV PYTHONIOENCODING=utf-8
ENV TTS_LANG = "Sharon-US-English"
ENV TTS_PITCH = "100"
ENV TTS_BITRATE = "128k"
ENV BOT_API_KEY = ""



RUN mkdir /opt/ttsbot

COPY ttsbot.py /opt/ttsbot



ENTRYPOINT ["/usr/bin/python3", "/opt/ttsbot/ttsbot.py"]
