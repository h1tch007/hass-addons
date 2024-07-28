ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install requirements for add-on
RUN apk add --no-cache ffmpeg

COPY rootfs /
RUN chmod a+x /etc/TorrServer-linux-amd64

CMD [ "/etc/TorrServer-linux-amd64","--path","/config" ]
