# Usage
# Just run and enjoy!

# Settings
# ---------------
UNAME = ""
STARTING_DIR = ""
HOSTNAME = "codehs"
NAME_COL = ""
DIR_COL = ""
# ---------------


import os
import readline
from subprocess import run
from socket import gethostname
from getpass import getuser
from lib_hack import install_lib
qs = install_lib("quick_styles")

def set_default(var, default):
    return var or default

def dash_to_space(text):
    return text.strip(" ").replace(" ", "-")

UNAME = dash_to_space(set_default(UNAME, getuser()))
STARTING_DIR = set_default(STARTING_DIR, ".")
HOSTNAME = dash_to_space(set_default(HOSTNAME, gethostname()))
NAME_COL = set_default(NAME_COL, "green")
DIR_COL = set_default(DIR_COL, "blue")

FILE_ERRS = (
    PermissionError,
    FileNotFoundError
)

run(f"cd {STARTING_DIR}", shell=True)
os.chdir(STARTING_DIR)
run("clear", shell=True)
while True:
    cmd = input(
        qs.style_string(f"{UNAME}@{HOSTNAME}:", color=NAME_COL) + 
        qs.style_string(os.getcwd() if os.getcwd() != '/' else '~', color=DIR_COL) + 
        " $ "
    )
    
    run(cmd, shell=True)
    
    try:
        if (cmd:=cmd.strip(" ")).startswith("cd"):
            os.chdir(cmd[3:])
    except FILE_ERRS:
        pass
