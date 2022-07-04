# packages from standard library
from pprint import pprint
import sys
import json
# For decoding JSON (python 3x)
from types import SimpleNamespace as Namespace

# from local module (not a package)
from .config import github

# sibling package
from models.repo import Repo


# external dependency
import requests


def get_gh_repos(org_name):
    """see: https://docs.github.com/en/rest/reference/repos#list-organization-repositories"""

    url = f'{github.api_orgs}/{org_name}/repos?sort=updated&page=1'
    r = requests.get(url)

    if r.status_code != 200:
        print(r.status_code)
        exit(-1)
    results = r.json()  # list of repos
    repos = [parse_dict_to_obj(item) for item in results]
    # for item in data:
    #     print(item)
    #     parse_dict_to_obj(item)

    return repos


def parse_dict_to_obj(repo):
    return Repo.from_dict(repo)


if __name__ == "__main__":
    # for e.g: python3 repos_service.py "microsoft"
    print(f"script execution for {sys.argv[0]} using arg {sys.argv[1]}")
    # todo: args validation
    if (len(sys.argv) > 1):
        get_gh_repos(sys.argv[1])
    else:
        get_gh_repos("microsoft")
else:
    # for e.g: during `python3 app.py`, the output here will be
    # this will be `services.repos_service` imported via `app.py`
    print(f"{__name__} imported via {sys.argv[0]}")

    # any code that needs to be run by default upon module import
