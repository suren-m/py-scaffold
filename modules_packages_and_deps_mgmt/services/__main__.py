# called when doing somethign like `python3 -m services`
print(f"{__name__} loaded")

# Printing sys path to demonstrate why doing a 
# pyhton3 repos_service.py 
# will result in models module not found error
# but it should be fine with `python3 -m services` 
# due to sys path containing root dir with the latter

import sys
print(sys.path)
