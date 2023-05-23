
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



#Task 3
data = json.loads(data)

filename = "json_output.json"

try:
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print(f"\n[{filename}] created.")
except Exception:
    print(f"[!!!] Error while creating {filename} [!!!]")
    exit()


#Task 4

import yaml


filename = "yaml_file.yml"
data = {}

try:
    with open(filename, "r") as file:
        try:
            data = yaml.safe_load(file)
            print(f"[{filename}]:")
            print(yaml.dump(data, indent=4))
        except yaml.YAMLError:
            print(f"[!!!] Error while importing {filename}.")
            print("Probably file does not exist or is not in YAML syntax [!!!]")
            exit()
except FileNotFoundError:
    print(f"[!!!] Error: {filename} does not exist [!!!]")
    exit()

# Task 5

filename = "yaml_output.yml"

try:
    with open(filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False, indent=4)
        print(f"\n[{filename}] created.")
except Exception:
    print(f"[!!!] Error while creating {filename} [!!!]")
    exit()



# Task 6
import xml.etree.ElementTree as ET

filename = "xml_file.xml"
data = {}

try:
    tree = ET.parse(filename)
    root = tree.getroot()

    for person in root.findall("person"):
        person_data = {}
        for element in person:
            person_data[element.tag] = element.text
        data[f"person{len(data)+1}"] = person_data

    print(f"[{filename}]:")
    for key, person_data in data.items():
        print(key)
        for element, value in person_data.items():
            print(f"    {element}: {value}")
except FileNotFoundError:
    print(f"[!!!] Error: {filename} does not exist [!!!]")
    exit()
except ET.ParseError:
    print(f"[!!!] Error while importing {filename}.")
    print("Probably file does not exist or is not in valid XML syntax [!!!]")
    exit()



