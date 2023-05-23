#  TASK 0

#!/usr/bin/env python

# Lista komponentow
required_packages = [
    'package1',
    'package2',
    'package3',
    # Dodaj więcej pakietów, jeśli są potrzebne
]

if __name__ == '__main__':
    import subprocess

    for package in required_packages:
        try:
            subprocess.check_call(['pip', 'install', package])
        except subprocess.CalledProcessError:
            print(f'Błąd podczas instalacji pakietu {package}.')
    print('Wszystkie wymagane pakiety zostały zainstalowane.')
