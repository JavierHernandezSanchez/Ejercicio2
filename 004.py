#!/usr/bin/python

#use text_exampl.txt to generate a new file with the same content but the line
#number at the beginning of each line

original_file = "/home/dsc/data/shell/Text_example.txt"
copy_file = "./Text_example_lines.txt"

orig = open(original_file, "r")
copy = open(copy_file, "w")
line_number = 1
for line in orig:
    copy.write(f"{line_number}: {line}")
    line_number += 1
orig.close()
copy.close()
