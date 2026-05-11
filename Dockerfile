FROM ubuntu:latest
LABEL authors="astyles"

ENTRYPOINT ["top", "-b"]