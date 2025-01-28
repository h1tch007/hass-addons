ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cachepaho-mqtt --root-user-action

COPY rootfs /
RUN chmod a+x /etc/ent/__main__.py

CMD [ "python3","/etc/ent/__main__.py" ]
