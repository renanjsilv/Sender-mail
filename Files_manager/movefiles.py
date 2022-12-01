from logging import root
import os
import shutil

source = "" # Pasta raíz Síntaxe C:\\Pasta\\Pasta\\Pasta\\
destination = "" # Pasta de destino

for (root, dir, files) in os.walk(source,topdown=True):
    for arquivos in files:
        dest = shutil.move(f"{root}\\{arquivos}", f"{destination}\\{arquivos}")
        print(f"{root} || {dir} || {arquivos}")
