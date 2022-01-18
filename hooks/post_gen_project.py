import sys
import subprocess as sh


# import subprocess

# try:
#     # initialise git
#     sh.run(["git", "init"], check=True)

#     # create repository
#     sh.run(["gh", "repo", "create","{{ cookiecutter.archetype_org}}/{{ cookiecutter.archetype_id }}", "-d", "{{ cookiecutter.archetype_description }}", "--private", "--confirm"], check=True)

# except subprocess.CalledProcessError as err:
#     print('Error:', err)

sys.exit(0)