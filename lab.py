
#  TASK 0

#!/usr/bin/env python

# Lista komponentow
required_packages = [
    "sys",
    "json",
    "os",
    "subprocess",
    
]

if __name__ == '__main__':
    import subprocess

    for package in required_packages:
        try:
            subprocess.check_call(['pip', 'install', package])
        except subprocess.CalledProcessError:
            print(f'Błąd podczas instalacji pakietu {package}.')
    print('Wszystkie wymagane pakiety zostały zainstalowane.')


#  TASK 1
import sys

arguments = sys.argv[1:]
print("Passed arguments:", arguments)

#Task 2
import json
import os

filename = "json_file.json"

try:
    with open(filename, "r") as file:
        data = json.load(file)
        data = json.dumps(data, indent=4)
        print(f"[{filename}]: \n {data}")
except Exception as Error:
    print("Error: ", Error)
    os.system('pause')


    