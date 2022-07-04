# py-scaffold

The `modules_packages_and_deps_mgmt` directory contains source code, demos that cover following areas of python:

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

---
#### Coding Guidelines 
* [PEP 8 - Style guide](https://peps.python.org/pep-0008/)

#### VS Code Setup
* [Getting started](https://code.visualstudio.com/docs/python/python-tutorial)
* [VS Code Docs](https://code.visualstudio.com/docs/python/debugging)
