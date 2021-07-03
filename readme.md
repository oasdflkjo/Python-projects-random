# Python venv in win10 wsl2
Versions

- Ubuntu 20.04.2 LTS
- Python 3.8.5
***
commands for venv
``` bash
# create venv
python3 -m venv venv

# activate venv
source venv/bin/activate 

# shows python version
which python

# installs dependen
pip install -r requirements.txt

# deactivate venv
deactive 
```

requirements.txt is generated with

```bash
pip freeze > requirements.txt
```
***
<br>
Going to push random py projects here for fun. 😀
<br>

<br>

1. First project is about on how u can speed up python code by converting python function into c with Cython library.

2. Second is a word counting program that uses dictionary data structure.