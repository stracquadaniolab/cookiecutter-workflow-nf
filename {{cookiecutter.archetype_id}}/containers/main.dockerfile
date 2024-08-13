FROM mambaorg/micromamba:1.5.8-lunar

COPY --chown=$MAMBA_USER:$MAMBA_USER containers/container_id /container_id
COPY --chown=$MAMBA_USER:$MAMBA_USER containers/main.env.yml /tmp/conda.yml

RUN micromamba install -y -n base -f /tmp/conda.yml \
    && micromamba install -y -n base conda-forge::procps-ng \
    && micromamba clean -a -y
USER root
ENV PATH="$MAMBA_ROOT_PREFIX/bin:$PATH"