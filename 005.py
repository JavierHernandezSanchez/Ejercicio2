#!/usr/bin/python
from getpass import getuser
from datetime import date

# generar un archivo que contenga:
# linea1: #!/bin/bash
# linea2: nombre del usuario y fecha de la creación

out_file = "005.out"
user = getuser()
today = date.today()

with open(out_file, "w") as out:
    out.write("#!/bin/bash\n")
    out.write(f"user: {user}, date: {today}\n")
	
