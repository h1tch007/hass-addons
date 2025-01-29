ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-paho-mqtt py3-yaml && ln -sf python3 /usr/bin/python

COPY rootfs /
WORKDIR /etc/ent/

CMD [ "python3","ent.py" ]
