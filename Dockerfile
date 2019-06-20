# This Dockerfile is used in:
# https://github.com/mnieber/dodo_commands/blob/master/README.md.
#
# to demonstrate the use of Docker in a Dodo Commands environment.

FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y cmake
