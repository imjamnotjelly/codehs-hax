# Usage
# Just run and enjoy!

# Settings
# ---------------
UNAME = ""
HOSTNAME = "codehs"
STARTING_DIR = ""
NAME_COL = ""
DIR_COL = ""
# ---------------


import os
import readline
from time import time
from math import floor
from subprocess import PIPE
from subprocess import run
from socket import gethostname
from getpass import getuser
from lib_hack import install_lib
qs = install_lib("quick_styles")

def set_default(var, default):
    return var or default

def space_to_dash(text):
    return text.strip(" ").replace(" ", "-")

def bold(text):
    return qs.style_string(text, styles="bold")

def elasped_mins():
    return floor((time() - startTime)/60)

def run_to_str(cmd):
    return run(cmd, shell=True, stdout=PIPE).stdout.decode("utf-8")
    
UNAME = space_to_dash(set_default(UNAME, getuser()))
HOSTNAME = space_to_dash(set_default(HOSTNAME, gethostname()))
STARTING_DIR = set_default(STARTING_DIR, ".")
NAME_COL = set_default(NAME_COL, "green")
DIR_COL = set_default(DIR_COL, "blue")
FULL_NAME = f'{UNAME}@{HOSTNAME}'

FILE_ERRS = (
    PermissionError,
    FileNotFoundError
)

run(f"cd {STARTING_DIR}", shell=True)
os.chdir(STARTING_DIR)
run("clear", shell=True)

startTime = time()
while True:
    cmd = input(
        qs.style_string(f"{FULL_NAME}:", color=NAME_COL) + 
        qs.style_string(os.getcwd() if os.getcwd() != '/' else '~', color=DIR_COL) + 
        " $ "
    )
    
    if (cmd:=cmd.strip(" ")) == "neofetch":
        mem = [i.strip(" ") for i in run_to_str("free -m").replace("\n", "  ").split("  ") if i]
        neofetch_str = f"""
.,,,,,,,,,,,,,,,,,,,,,,,  
$ $``,,,,,,,,,,,`,,,`)F]F   {bold(FULL_NAME)}
$ $ *MMMMMMMMMMP MMM ]F]F   {'-'*len(FULL_NAME)}
$ $ ]KKP:KKE KKKKKKK ]F]F   {bold("OS: ")}Ubuntu 18.04.6 LTS x86_64
$ $ jHHHHHH[ ppF ppm ]F]F   {bold("Kernel: ")}4.4.0-1101-aws
$ $ .ww  ,,,.,,, ,,, ]F]F   {bold("Uptime: ")}{elasped_mins()} mins
$ $,,,,,,,,,,,,,,,,,,]F]F   {bold("CPU: ")}Intel(R) Xeon(R) Platinum @ 2.50GHz
$,'''''''''''''''''''',]F   {bold("Mem: ")}{mem[8]} / {mem[7]}MiB
 ``````)$YYYYYY$```````
  pmmmmHbmmmmmmmHmmmmmp
  bppppppppppppppppppp$
  ^^^^^^^^^^^^^^^^^^^^^   
        """
        
        neofetch_str = "\n".join([qs.style_string(l, color="blue") for l in neofetch_str.split("\n")])
        print(neofetch_str)
        continue
    
    run(cmd, shell=True)
    
    try:
        if cmd.startswith("cd"):
            os.chdir(cmd[3:])
    except FILE_ERRS:
        pass
