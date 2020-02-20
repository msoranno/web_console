FROM ubuntu:18.04
ARG KUBE_URL=https://storage.googleapis.com/kubernetes-release/release
# ARG CFG_FILE=/.kube/.config
COPY kubectl-x /usr/local/bin
RUN apt-get update -y && apt-get install curl vim -y && \
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
chmod +x kubectl && mv kubectl /usr/local/bin/xyz && \
xyz version --client && \
useradd -ms /bin/bash iac && chmod +x /usr/local/bin/kubectl-x && \
mv /usr/bin/which /usr/bin/xwhich && \
mv /bin/which /bin/xwhich && \
mv /usr/bin/find /usr/bin/xfind && \
mv /usr/bin/whereis /usr/bin/xwhereis 
USER iac
WORKDIR /home/iac
# ENV KUBECONFIG=${CFG_FILE}
ENTRYPOINT ["/bin/rbash"]

