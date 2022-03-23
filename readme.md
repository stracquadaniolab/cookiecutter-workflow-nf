# A cookiecutter for Nextflow workflows
![](https://img.shields.io/badge/current_version-v0.7.0-blue)
![](https://github.com/stracquadaniolab/cookiecutter-workflow-nf/workflows/build/badge.svg)

A standardized directory structure to build workflows using Nextflow.

## Directory structure

```bash
├── .github
│  └── workflows
│     └── ci.yml
├── bin
│  ├── fit.py
│  └── plots.py
├── conf
│  └── base.config
├── containers
│  ├── Dockerfile
│  └── environment.yml
├── testdata
│  └── mydata.txt
├── .bumpversion.cfg
├── .devcontainer.json
├── .gitignore
├── main.nf
├── nextflow.config
└── readme.md
```

## The workflow file

The `main.nf` file contains the entrypoint for the workflow, and it uses
Nextflow DSL2 by default. The workflow parameters are stored in the
`nextflow.config` file, which in turn include other files in the `conf`
directory; usually, you only have to define the parameters of your specific
pipeline, since the `conf/base.conf` file includes profiles to run your workflow
in different computing environment, e.g. Slurm, GitHub. 

Please, refer to the [Nextflow
documentation](https://www.nextflow.io/docs/latest/index.html) for an overview
of the framework.

## Custom scripts management

Custom code (aka your scripts and classes) needed by the pipeline should be
added to the `bin` directory; the code in this directory is automatically added
to `$PATH` when running the pipeline, which makes custom scripts easily portable
and accessible. If you are using Python, you should have a file for each class
of operations, e.g. a file `plots.py` for all the plots, and use
[`docopt`](https://github.com/docopt/docopt) to have standard Unix command line
interface. See the auto-generated pipeline for an example.

## Software management

Third-party software is managed by `micromamba` and specified in a
`environment.yml` file; keep the `yml` file updated and specify the version of
each software you are using in order to ensure reproducibility.

To ensure reproducibility and running experiments on local machines and HPC
clusters, it is strongly recommended to build a Docker image. The bundled
`Dockerfile` can be used to build an image with the software specified in your
`environment.yml` file. To do that, run:

```bash
docker build . -t ghcr.io/stracquadaniolab/<my-workflow>:<version> -f containers/Dockerfile
```

where `<my-workflow>` is the name of your workflow and `<version>`
is the current version of your workflow, starting from `0.0.0`.

The template comes with an auto-generated `.devcontainer.json` file, which
allows developing your scripts inside a container with all the software
specified in `environment.yml` using `vscode`.

Sometimes you would want to pull a docker image from GitHub container registry:
```bash
docker pull ghcr.io/stracquadaniolab/<workflow_name>:<version>
```
In order to successfully pull an image, first you need to authenticate yourself
with your personal access token, see here: [Authenticating with the container
registry](https://docs.github.com/en/packages/guides/migrating-to-github-container-registry-for-docker-images#authenticating-with-the-container-registryhttps://docs.github.com/en/packages/guides/migrating-to-github-container-registry-for-docker-images#authenticating-with-the-container-registry)

## Testing

It is important to build workflows that can be automatically tested; thus, you
will have to add small test data into the `testdata` directory, and modify the
`test` profile in `conf/base.config` configuration file to specify any parameter
needed for your workflow to run. See the auto-generated pipeline for an example.

## Versioning

All projects must follow a semantic version scheme. The format adopted is
`MAJOR.MINOR.PATCH`:

- MAJOR: drastic changes that make disruptive changes with a previous release. 
- MINOR: add functions to the workflow but keeps everything compatible within
  the MAJOR version.
- PATCH: bug fixes or settings update.

To update the version of your workflow, you should run the following command from 
the command line: 

```bash
bump2version major #for major release
bump2version minor #for minor release
bump2version patch #for patch release
```

## Push your code to GitHub

As the project is version controlled using Git, you can push your code to GitHub
as follows:

```bash
git add . 
git commit -am "new: added super cool feature"
git push -u origin master
```

Importantly, after a `bumpversion`, you also have to push the tag just created as follows:

```bash
git push --tags
```

## Continuous integration

Each pipeline comes with a pre-configured GitHub workflow to automatically test
the code and build a Docker image; the workflow is stored in
`.github/workflows/ci.yml`. Please note that a Docker image is only released
when you push a tag.
## Documentation

Each workflow must have an updated `readme.md` file, describing:

* what the workflow does
* how to configure the workflow
* how to run the workflow
* a description of the output generated

A `readme.md` file with the required sections is automatically generated by this
cookiecutter.
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
