FROM fedora:25

ARG USER_ID=1000
ARG USERNAME="app"
ARG GIT_REPOSITORY="ssh://${USERNAME}@git.example.com/app.git"

RUN set -x && adduser -m -u ${USER_ID} ${USERNAME}
USER ${USERNAME}

COPY fresh_ssh_key* /home/${USERNAME}/.ssh/
USER root
RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/.ssh/
USER ${USERNAME}
RUN set -x ; cd /home/${USERNAME} && \
    git clone ${GIT_REPOSITORY} || \
    rm ~/.ssh/*

CMD ["start_application"]
