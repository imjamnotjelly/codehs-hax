import os
import readline
from subprocess import run
from socket import gethostname
from getpass import getuser


# Settings
# ---------------
UNAME = "imjamnotjelly"
STARTING_DIR = ""
HOSTNAME = "codehs"
# ---------------

def set_default(var, default):
    return var or default

def dash_to_space(text):
    return text.strip(" ").replace(" ", "-")

UNAME = dash_to_space(set_default(UNAME, getuser()))
STARTING_DIR = set_default(STARTING_DIR, ".")
HOSTNAME = dash_to_space(set_default(HOSTNAME, gethostname()))

FILE_ERRS = (
    PermissionError,
    FileNotFoundError
)

run(f"cd {STARTING_DIR}", shell=True)
os.chdir(STARTING_DIR)
run("clear", shell=True)
while True:
    cmd = input(f"{UNAME}@{HOSTNAME}:{os.getcwd() if os.getcwd() != '/' else '~'} $ ")
    
    run(cmd, shell=True)
    
    try:
        if (cmd:=cmd.strip(" ")).startswith("cd"):
            os.chdir(cmd[3:])
    except FILE_ERRS:
        pass