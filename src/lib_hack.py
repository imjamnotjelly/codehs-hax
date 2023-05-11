from subprocess import run
from importlib import import_module
from types import ModuleType

def install_lib(libname: str) -> ModuleType:
    while True:
        try:
            return import_module(libname)
        except ModuleNotFoundError:
            run(f"python3 -m pip install {libname}", shell=True)