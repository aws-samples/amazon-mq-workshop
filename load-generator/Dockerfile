FROM amazonlinux:2

# Install dependencies
RUN yum install -y java-1.8.0 \
    && yum clean all

ENV JAVA_OPTS=""
ENTRYPOINT ["java", "-jar", "app.jar"]

# Provision the Proxy
VOLUME /tmp

ADD target/load-generator.jar app.jar