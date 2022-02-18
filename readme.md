# A cookiecutter for Nextflow workflows
![](https://img.shields.io/badge/current_version-v0.7.0-blue)
![](https://github.com/stracquadaniolab/cookiecutter-workflow-nf/workflows/build/badge.svg)

A standardized directory structure to build workflows using Nextflow.

## Directory structure

```
|-- bin
|   `-- main.py
|-- conf 
|   `-- base.config
|-- containers
|-- |-- environment.yml
|   `-- Dockerfile
|-- main.nf
|-- nextflow.config
`-- testdata
```

## Overview

The `main.nf` file contains the entrypoint for the workflow, and it uses DSL2 by
default. The workflow configuration is stored in the `nextflow.config` file and
under the `conf` directory; usually, you only have to define the parameters of
your specific pipeline, since the other configurations are profiles to run the
pipeline in different computing environment, e.g. SGE, GitHub. Please, refer to
the [Nextflow documentation](https://www.nextflow.io/docs/latest/index.html) for
an overview of the framework.

### Custom scripts management

Custom code need by the pipeline should be added to the `bin` directory; the
code in this directory is automatically added to `$PATH` when running the
pipeline, which makes custom scripts easily portable and accessible. If you are
using Python, you should have a file for each class of operations, e.g. a file
`plots.py` for all the plots, and use `docopt` to have standard Unix command
line interface. See the auto-generated pipeline for an example. 

The template comes with an auto-generated `.devcontainer.json` file, which
allows developing your scripts inside a container with all the software
specified in `environment.yml` using `vscode`.

### Software management

Third-party software is managed by `conda` and specified in a `environment.yml`
file; keep the `yml` file updated and specify the version of each software you
are using.

To ensure reproducibility and running experiments on local machines and HPC
clusters, it is strongly recommended to build a Docker image. The bundled
`Dockerfile` can be used to build an image with the software specified in your
`environment.yml` file. To do that, run:

```bash
docker build . -t ghcr.io/stracquadaniolab/<my-workflow>:v0.0.0 -f containers/Dockerfile
```

where `<my-workflow>` is the name of your workflow, and the version should match
the one in the config files.

### Testing

It is important to build workflows that can be automatically tested; thus, you
will have to add small test data into the `testdata` directory, and modify the
`test` profile in the `conf/base.config` file to specify any parameter needed
for your workflow to run. See the auto-generated pipeline for an example.

**IMPORTANT: if you are using an Apple M1, you should also specify the profile
apple, to make sure you can run your Docker image.**

### Versioning

All projects must follow a semantic version scheme. The format adopted is
`MAJOR.MINOR.PATCH`:

- MAJOR: drastic changes that make disruptive changes with a previous release. 
- MINOR: add functions to the workflow but keeps everything compatible within
  the MAJOR version.
- PATCH: bug fixes or settings update.

To update the version of your workflow, you should run the following command from 
the command line:

```
bump2version <major|minor|patch>
```

### Documentation

Each workflow must have an updated `readme.md` file, describing:

* what the workflow does
* how to configure the workflow
* how to run the workflow
* a description of the output generated

A `readme.md` file with the required sections is automatically generated by this
cookiecutter.

### Continuous integration

Each pipeline comes with a pre-configured GitHub workflow to automatically test
the code and build a Docker image; the workflow is stored in
`.github/workflows/ci.yml`.

## Getting started

### Step 1: Create a new workflow

```
cookiecutter https://github.com/stracquadaniolab/cookiecutter-workflow-nf.git
```

You will be asked a number of questions to setup your workflow.

### Step 2: Push the pipeline to GitHub

```bash
git push -u origin master
```

### Step 3: Run a pipeline with test data

```bash
nextflow run stracquadaniolab/my-pipeline -profile test
```

When you run a pipeline for the first time, it will download the latest release
from GitHub and run it on the test data.

### Step 4: Run a pipeline with test data and Docker

```bash
nextflow run stracquadaniolab/my-pipeline -profile test,docker
```
### Step 5: Run a pipeline with test data and Singularity

```bash
nextflow run stracquadaniolab/my-pipeline -profile test,singularity
```

### Step 6 (optional): Run a pipeline on a cluster with SLURM

```bash
nextflow run stracquadaniolab/my-pipeline -profile test,singularity,slurm
```

It is recommended to run this command using `tmux`, such that you can monitor
the progress of your job even if you logout from the cluster.

## Authors

* Giovanni Stracquadanio, giovanni.stracquadanio@ed.ac.uk
