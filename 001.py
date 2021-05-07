#!/usr/bin/python

from os import listdir
from os.path import isfile
from os.path import join
from os.path import getsize
from os import stat
from stat import filemode
from datetime import datetime, timezone

#obtener la informacion (permisos, tamaño, fecha de modificación, etc.) 
#Sobre el archivo más grande de la carpeta opentraveldata

initial_path = "/home/dsc/data/opentraveldata/"
max_size = 0
biggest_file = ""

for f in listdir(initial_path):
    curr_file = join(initial_path, f)
    if not isfile(curr_file):
        print(f"{f} is not a file")
        continue
    
    curr_size = getsize(curr_file)
    if curr_size >= max_size:
        max_size = curr_size
        biggest_file = curr_file

s = stat(biggest_file)

print("fichero más grande")
print("__________________")
print(f"nombre: {biggest_file}")
print(f"tamaño: {s.st_size} bytes")
permissions = filemode(s.st_mode)
print(f"permisos: {permissions}")
modified = datetime.fromtimestamp(s.st_mtime, tz=timezone.utc)
print(f'fecha de modificacion: {modified} UTC')
