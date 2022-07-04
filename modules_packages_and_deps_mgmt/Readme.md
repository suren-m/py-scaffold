## This directory contains source code, demos that cover following areas of python:

* Python application structure (generic and not specific to any framework)
* Understanding [modules](https://docs.python.org/3/tutorial/modules.html#) and its usage (for e.g, how [`__name__`](https://docs.python.org/3/library/__main__.html) works)
* [Packages](https://docs.python.org/3/tutorial/modules.html#packages) to enable better code organisation and more sophisticated code reuse such as `sibling imports` with just `local packages` (and understand how `__init__.py` works)
    * Packages act as a namespace for a collection of modules
    * They also enable code-distribution and publishing in python ecosystem. But this webinar only focuses on `local packages` for code reuse within same repo / project.
* Intro to Dependency management with:
    * `pip` (most common, uses `requirements.txt` to specify deps)
    * `pipenv` (evolution of `pip` and abstracts some internal `virtual env` details. uses `Pipfile` to specify deps)
    * `conda` / `miniconda` (most popular in data science space)
* Intro to [python data model](https://docs.python.org/3/reference/datamodel.html) with classes.
* Intro to unit testing setup 

The above are demonstrated using a simple application that retrieves `page 1` `public repos` for a given `org` from [github api](https://docs.github.com/en/rest/reference/repos#list-organization-repositories) (sorted by `updated`)

`Docker` is used to showcase three popular dependency / package management tools in Python ecosystem. (`pip`, `pipenv`, `conda`)

## To Run locally 

1. Beginner friendly approach with pip

```bash
# Just make sure to have python and pip installed as a minimum
# Usually pip gets installed along with Python

# Install requests http library globally for now (or use requirements.txt and virtualenv if already familiar)
pip3 install requests

# pass org name as an argument
python3 app.py microsoft

# To run unit tests
python3 -m unittest
# Or for a specific test class in a module
# in this case, `TestReposService` class from `test_repos_service` module inside `tests` package
python3 -m unittest tests.test_repos_service.TestReposService

# or from VS code, place a breakpoint in `main` function in `app.py` and press `f5` 
# requires `python` extension for vs code
```

2. Use `Virtual env` with `pipenv`

```bash
pipenv install
pipenv shell
# this activates virtual env according to specifications in Pipfile
# Run and pass org name as an argument 
# note it's just python and not python3 when inside pipenv shell)
python app.py microsoft

# Exit pipenv shell when done
exit
```

3. Docker

```bash
# feel free to change the image name/tag as needed

# this example uses py:{dir_name}-{package-manager-name} format

# tip: ${PWD##*/} is used to print only the current dir_name in bash (notice the use of uppercase when parsing)
# In this case, it will be `modules_and_deps_management`

# below will result in image name `py:modules_and_deps_management-pip
docker build . -f Dockerfile.pip -t py:${PWD##*/}-pip
docker run py:${PWD##*/}-pip

# likewise for pipenv and conda demonstration

docker build . -f Dockerfile.pipenv -t py:${PWD##*/}-pipenv
docker run py:${PWD##*/}-pipenv

docker build . -f Dockerfile.conda -t py:${PWD##*/}-conda
docker run py:${PWD##*/}-conda
```

---

### Sample output
```bash
❯ python3 app.py microsoft
services.config.github imported via app.py
models.repo imported via app.py
services.repos_service imported via app.py
Executing app.py with argument: microsoft

Retrieving github repos (page 1, sorted by updated) for microsoft....

microsoft/vscode ⭐ 129622
microsoft/Data-Science-For-Beginners ⭐ 9616
microsoft/PowerToys ⭐ 70870
microsoft/DirectStorage ⭐ 191
microsoft/Web-Dev-For-Beginners ⭐ 45050
microsoft/msccl ⭐ 38
microsoft/IoT-For-Beginners ⭐ 9383
microsoft/Windows-classic-samples ⭐ 3359
microsoft/griffel ⭐ 715
microsoft/TypeScript ⭐ 79319
microsoft/recommenders ⭐ 12724
microsoft/terminal ⭐ 82056
microsoft/vscode-arduino ⭐ 938
microsoft/azuredatastudio ⭐ 6728
microsoft/vstest-docs ⭐ 196
microsoft/azure-healthcare-apis-workshop ⭐ 12
microsoft/LightGBM ⭐ 13610
microsoft/jupyter-core ⭐ 96
microsoft/Azure-Invoice-Process-Automation-Solution-Accelerator ⭐ 2
microsoft/kiota-serialization-text-go ⭐ 1
microsoft/playwright ⭐ 36128
microsoft/vcpkg ⭐ 15304
microsoft/TypeScript-React-Starter ⭐ 10889
microsoft/FLAML ⭐ 1794
microsoft/Microsoft-Win32-Content-Prep-Tool ⭐ 406
microsoft/TeamMate ⭐ 11
microsoft/TailwindTraders ⭐ 607
microsoft/reverse-proxy ⭐ 5162
microsoft/JigsawDataset ⭐ 3
microsoft/msagljs ⭐ 0

----
❯ python3 -m unittest      
services.config.github imported via python3 -m unittest
models.repo imported via python3 -m unittest
services.repos_service imported via python3 -m unittest
.
----------------------------------------------------------------------
Ran 1 test in 0.665s

OK
```

### Related docs and resources

https://peps.python.org/pep-0008/

https://docs.python.org/3/tutorial/modules.html

https://docs.python.org/3/tutorial/modules.html#packages

https://docs.python.org/3/tutorial/modules.html#packages-in-multiple-directories

https://pipenv.pypa.io/en/latest/

https://pypi.org/project/pip/

https://realpython.com/python-modules-packages/ 

