FROM  continuumio/miniconda3

LABEL org.stracquadaniolab.name="{{ cookiecutter.artefact_id }}"
LABEL org.stracquadaniolab.description="{{ cookiecutter.artefact_description }}"

RUN apt-get update \
    && apt-get install --yes rename tini procps curl \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY environment.yml /
RUN conda env update -n base --file environment.yml && conda clean --all --yes 

ENTRYPOINT ["tini", "--"]
CMD ["/bin/bash"]