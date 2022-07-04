import sys

from services import repos_service


def main(org="microsoft"):
    '''use microsoft as default argument for demo'''
    print(f"Retrieving github repos (page 1, sorted by updated) for {org}....\n")
    repos = repos_service.get_gh_repos(org)
    for repo in repos:
        print(repo)


# special variable to check if it's direct execution or module import
if __name__ == "__main__":
    # sys.argv contains args passed in. First one is the filename
    # for e.g. python3 app.py microsoft    
    if (len(sys.argv) > 1):
        print(f"Executing {sys.argv[0]} with argument: {sys.argv[1]}\n")
        main(sys.argv[1])
    else:
        print(f"Executing {sys.argv[0]}\n")
        main()
else:
    # runs when doing `import app` from python3 terminal or from another module
    # the client can then call, `app.main()` to invoke the main function above

    # Note: In above case, `sys.argv[0]` will be blank too

    print(f"{__name__} imported via {sys.argv[0]}")
    # any code that needs to be run by default upon module import
