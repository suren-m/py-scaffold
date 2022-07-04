# This file is also an example of a basic module (not a package!)
# Notice the config directory also doesn't contain __init__.py

import sys

api_base = "https://api.github.com"
api_orgs = f"{api_base}/orgs"

if __name__ == "__main__":
    print(f"script execution for {sys.argv[0]}")
else:
    print(f"{__name__} imported via {sys.argv[0]}")
