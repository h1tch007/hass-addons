ARG BUILD_FROM
FROM $BUILD_FROM

ENV GODEBUG=madvdontneed=1

# Install requirements for add-on
RUN \
  apk add --no-cache \
    ffmpeg

COPY TorrServer-linux-amd64 / 
RUN chmod a+x /TorrServer-linux-amd64

CMD [ "/TorrServer-linux-amd64" ]
