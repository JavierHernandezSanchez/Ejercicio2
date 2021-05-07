#!/usr/bin/python

#obtener cuántas palabras contienen las 5 primeras líneas del archivo finn.txt

initial_path = "/home/dsc/data/shell/Finn.txt"
n_lines = 5
total_words = 0
with open(initial_path) as in_file:
    for i in range(n_lines):
        line = in_file.readline()        
        if not line:
            break
        line_words = len(line.split())
        total_words += line_words
    print(f"{total_words}")
