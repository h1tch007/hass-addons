ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install requirements for add-on
RUN apk add --no-cache ffmpeg

COPY rootfs /
RUN chmod a+x /etc/ent/__main__.py

CMD [ "python3","/etc/ent/__main__.py" ]
