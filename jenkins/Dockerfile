FROM jenkins/jenkins:2.263.4-lts-jdk11
USER root
RUN apt-get update && apt-get install -y apt-transport-https \
       ca-certificates curl gnupg2 \
       software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce-cli
RUN apt-get install python3 -y && apt-get install python3-pip -y && apt-get install python3-venv -y
RUN echo "jenkins:jenkins" | chpasswd && adduser jenkins sudo

COPY . .

USER jenkins
RUN jenkins-plugin-cli --plugins blueocean:1.24.4

#docker run --name jenkins-test1 --rm --detach \
#  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
#  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
#  --publish 8083:8080 --publish 50000:50000 \
#  --volume jenkins-data:/var/jenkins_home \
#  --volume jenkins-docker-certs:/certs/client:ro \
#  jenkins-test1:latest