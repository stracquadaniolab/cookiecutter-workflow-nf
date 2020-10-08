import sys
import subprocess as sh

# initialise git
sh.run(["git", "init"], check=True)

# create repository
sh.run(["gh", "repo", "create","{{ cookiecutter.artifact_org}}/{{ cookiecutter.artifact_id }}", "-d", "{{ cookiecutter.artifact_description }}", "--private", "--confirm"], check=True)

sys.exit(0)