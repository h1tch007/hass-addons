ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache py3-paho-mqtt py3-yaml && ln -sf python3 /usr/bin/python

COPY rootfs /
RUN chmod a+x /etc/ent/__main__.py

CMD [ "python3","/etc/ent/__main__.py" ]
