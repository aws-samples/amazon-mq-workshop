FROM sapk/cloud9
RUN echo 'deb http://http.debian.net/debian jessie-backports main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install -t jessie-backports -y openjdk-8-jdk
COPY ./bash_env bash_env
RUN cat bash_env >> ~/.bashrc
RUN update-java-alternatives --set java-1.8.0-openjdk-amd64

