
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
