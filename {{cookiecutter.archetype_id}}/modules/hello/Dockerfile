FROM mambaorg/micromamba:1.4.4
RUN micromamba install -y -n base -c conda-forge \
     procps-ng \
     python>3.8 \
     docopt && \
    micromamba clean --all --yes
