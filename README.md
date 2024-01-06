![license](https://img.shields.io/badge/License-GNU_GPLv3-blue)
![python_ci](https://github.com/grethler/domainer/actions/workflows/python.yml/badge.svg)
![docker_cd](https://github.com/grethler/domainer/actions/workflows/docker.yml/badge.svg)

<img src="./domainer.png" width="50%">

# Welcome to domainer!

Domainer is a custom script designed to search for subdomains of a given domain. \
The script uses different techniques to scan a target domain and discover all of its subdomains. 

The syntax of the target should be: SLD + TLD \
For example instead of `https://www.github.com` use `github.com`

## Clone repository and start virtual environment:
```bash
git clone https://github.com/grethler/domainer
cd ./domainer
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies:
```bash
pip install -r .\requirements.txt
```

## Running the script:
The script can be run with Python or Docker. \
The following arguments that can be used with the script: \
`-w` - webcrawl \
`-d` - dictionary &\
`-t` - threads \
`-b` - database \
The last argument of the script is the target domain.   

The fastest and easiest way is to use the database argument.
```bash
python .\domainer.py -b target
```
The webcrawling argument is the slower but hast mostly the same results, \
but can have some extra ones.
```bash
python .\domainer.py -w target
```
The slowest way is to use the dictionary attack argument. \
Depending on the hardware (threads used) and the size of the dictionary, \
this can take a long time.
```bash
python .\domainer.py -d {strength} -t {threads} target
```
The strength of the dictionary means the length of the dictionary. \
1 - 1000 \
2 - 10000 \
3 - 100000 \
4 - 1000000 \
The threads argument is the amount of threads used to read the dictionary.

### Run the script with Python:
```bash
python .\domainer.py [-h] [-w] [-d DICT] [-t THREADS] [-b] target
```

### Run the script with Docker:
>(not tested yet)
```bash
docker build -t domainer .
docker run -it domainer [-h] [-w] [-d DICT] [-t THREADS] [-b] target
```
Dont forget to remove the container after usage.