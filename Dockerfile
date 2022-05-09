FROM python:3.9.5-slim-buster AS base

ARG USER_ID=1000
ARG GROUP_ID=1000

ENV USERNAME servo
ENV WORKPATH /opt/workdir
RUN addgroup --gid ${GROUP_ID} $USERNAME
RUN adduser --uid ${USER_ID} --gid ${GROUP_ID} --disabled-password --gecos '' --system $USERNAME
WORKDIR $WORKPATH
RUN chown -R ${USER_ID}:${GROUP_ID} .

ENV PYTHONPATH "${PYTHONPATH}:${WORKPATH}"
ENV PATH "/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

COPY --chown=$USERNAME:$USERNAME requirements.txt $WORKPATH

CMD ["python", "src/main.py"]

FROM base AS dev
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r requirements.txt
COPY --chown=$USERNAME:$USERNAME . $WORKPATH
