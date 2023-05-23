
#  TASK 0

#!/usr/bin/env python

# Lista komponentow
required_packages = [
    "sys",
    "json",
    "os",
    "subprocess",
    "importlib",
    "pyyaml",
    "xml",
]

if __name__ == '__main__':
    import importlib
    import subprocess

    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            try:
                subprocess.check_call(['pip', 'install', package])
            except subprocess.CalledProcessError:
                print(f'\nError while instaling package: {package}.')
                exit()
    print('\nAll packages are installed.')


#  TASK 1
import sys

arguments = sys.argv[1:]
if arguments:
    print("\nPassed arguments:", arguments)
else:
    print("\nNo arguments were passed.\n")


#Task 2
import json
import os

filename = "json_file.json"
data = {}

try:
    with open(filename, "r") as file:
        data = json.load(file)
        data = json.dumps(data, indent=4)
        print(f"[{filename}]: \n {data}")
except Exception:
    print(f"[!!!] Error while importing  {filename}.\nProbably file does not exist or is not in json syntax [!!!]")
    exit()