FROM node:26-alpine

ARG UID=431805173
ARG GID=431805173
ARG USERNAME=lfv

RUN apk add --no-cache sudo \
    && addgroup -g ${GID} ${USERNAME} \
    && adduser -D -u ${UID} -G ${USERNAME} ${USERNAME} \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
