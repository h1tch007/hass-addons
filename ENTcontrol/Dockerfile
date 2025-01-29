ARG BUILD_FROM=homeassistant/amd64-base-ubuntu:latest
FROM $BUILD_FROM

#ENV GODEBUG=madvdontneed=1

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python3-pip && \
  pip3 install paho-mqtt &&
  pip3 install pyyaml

COPY rootfs /
WORKDIR /etc/ent/

CMD [ "python3","ent.py" ]
