import os
from pathlib import Path

package_name = "mongodb_automation"

list_of_files = [
   ".github/workflows/ci.yaml",
   ".github/workflows/python-publish.yaml",
   
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/integration.py",
   
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   
   "notebooks/experiments.ipynb",
   "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file