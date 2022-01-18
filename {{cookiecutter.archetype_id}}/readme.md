# {{ cookiecutter.archetype_id }}

![](https://img.shields.io/badge/current_version-v0.0.0-blue)
![](https://github.com/{{ cookiecutter.archetype_org }}/{{ cookiecutter.archetype_id }}/workflows/build/badge.svg)
## Overview
{{ cookiecutter.archetype_description }}

## Configuration

- param1: this is the parameter description (default: "hello")
- param2: this is the parameter description (default: "world")
- ...
- paramN: this is the parameter description (default: "flow")

## Running the workflow

### Install or update the workflow

```bash
nextflow pull {{ cookiecutter.archetype_org }}/{{ cookiecutter.archetype_id }}
```

### Run the analysis

```bash
nextflow run {{ cookiecutter.archetype_org }}/{{ cookiecutter.archetype_id }}
```

## Results

- `results/analysis.txt`: file with the analysis results.
- `results/tuning.txt`: file with the parameter tuning.
- ...

## Authors

- {{ cookiecutter.archetype_author }}
