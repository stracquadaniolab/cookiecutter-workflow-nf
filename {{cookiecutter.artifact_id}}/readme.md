# {{ cookiecutter.artifact_id }}

![](https://github.com/{{ cookiecutter.artifact_org }}/{{ cookiecutter.artifact_id }}/workflows/build/badge.svg)

{{ cookiecutter.artifact_description }}

## Configuration

- param1: this is the parameter description (default: "hello")
- param2: this is the parameter description (default: "world")
- ...
- paramN: this is the parameter description (default: "flow")

## Running the workflow

### Install or update the workflow

```bash
nextflow pull {{ cookiecutter.artifact_org }}/{{ cookiecutter.artifact_id }}
```

### Run the analysis

```bash
nextflow run {{ cookiecutter.artifact_org }}/{{ cookiecutter.artifact_id }}
```

## Results

- `results/analysis.txt`: file with the analysis results.
- `results/tuning.txt`: file with the parameter tuning.
- ...

## Authors

- {{ cookiecutter.artifact_author }}
