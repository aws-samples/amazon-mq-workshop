FROM 416075262792.dkr.ecr.eu-west-1.amazonaws.com/cloud9:latest
#RUN echo 'deb http://http.debian.net/debian jessie-backports main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install openjdk-8-jdk -y
COPY bash_env_src bash_env
RUN cat bash_env >> ~/.bashrc
RUN update-java-alternatives --set java-1.8.0-openjdk-amd64

