## base container
FROM mambaorg/micromamba:0.15.3 as base_container
USER root
RUN apt-get update \
    && apt-get install --yes rename tini procps curl \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER micromamba
ENTRYPOINT ["tini", "--"]
CMD ["/bin/bash"]

## main container
ARG CONDA_FILE=containers/env.base.yml
FROM base_container
# adding opencontainer labels to link registry to github repository
LABEL org.opencontainers.image.title="{{ cookiecutter.archetype_id }}"
LABEL org.opencontainers.image.description="{{ cookiecutter.archetype_description }}"
LABEL org.opencontainers.image.url="https://github.com/{{ cookiecutter.archetype_org }}/{{ cookiecutter.archetype_id }}"
LABEL org.opencontainers.image.documentation="https://github.com/{{ cookiecutter.archetype_org }}/{{ cookiecutter.archetype_id }}"
LABEL org.opencontainers.image.source="https://github.com/{{ cookiecutter.archetype_org }}/{{ cookiecutter.archetype_id }}"
LABEL org.opencontainers.image.vendor="{{ cookiecutter.archetype_org }}"
LABEL org.opencontainers.image.authors="{{ cookiecutter.archetype_author }}"
LABEL org.opencontainers.image.revision="v0.0.0"

COPY --chown=micromamba:micromamba ${CONDA_FILE} /tmp
RUN micromamba install -y -n base -f /tmp/`basename ${CONDA_FILE}` && \
    micromamba clean --all --yes
