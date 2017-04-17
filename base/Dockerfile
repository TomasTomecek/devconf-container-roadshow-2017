FROM fedora:25
ENV USERNAME=dan
ARG USERNAME=$USERNAME
RUN dnf install -y iproute && \
    adduser -m $USERNAME
