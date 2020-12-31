################################################################################
# Import modules
################################################################################

import os
from os.path import splitext, dirname

################################################################################
# Define package composition
################################################################################

__all__ = []

for root, dirs, files in os.walk(dirname(__file__)):
    for filepath in files:
        root, ext = os.path.splitext(filepath)
        if ext == ".py" and root != "__init__":
            __all__.append(root)
    break

# Obsolete code
#__all__ = ["app_helpers", "jinja2_helpers", "page_helpers"]
#__all__ = ["home","sta"]
