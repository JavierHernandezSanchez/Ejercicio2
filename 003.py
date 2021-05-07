#!/usr/bin/python

#imprimir las 3 primeras líneas de text_example.txt con el número de línea delante

initial_path = "/home/dsc/data/shell/Text_example.txt"
n_lines = 3

with open(initial_path) as in_file:
    for i in range(n_lines):
        line = in_file.readline()        
        if not line:
            break
        print(f"{i+1}: {line}", end="")
