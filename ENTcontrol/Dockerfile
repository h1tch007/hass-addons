ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install python/pip
#ENV PYTHONUNBUFFERED=1
#RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python
RUN pip3 install paho-mqtt

COPY rootfs /
RUN chmod a+x /etc/ent/__main__.py

CMD [ "python3","/etc/ent/__main__.py" ]
