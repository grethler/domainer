![license](https://img.shields.io/badge/License-GNU_GPLv3-blue)
![python_ci](https://github.com/delsyst0m/domainer/actions/workflows/python.yml/badge.svg)
![docker_cd](https://github.com/delsyst0m/domainer/actions/workflows/docker.yml/badge.svg)

<img src="./domainer.png" width="20%">

# Welcome to domainer!

Domainer is a custom script designed to search for subdomains of a given domain. 
The script uses different techniques to scan a target domain and discover all of its subdomains. 

The syntax of the target should be: SLD + TLD \
For example instead of `https://www.github.com` use `github.com`

## Install dependencies:
```
pip install -r .\requirements.txt
```

## Run the script with Python:
```
python .\domainer.py [-h] [-w] [-d DICT] [-n] [-A] target
```