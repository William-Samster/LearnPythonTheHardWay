#this is the 20th exercise of the book more about functions and reading files

from sys import argv

sript, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("Let's print the whole file first \n")

print_all(current_file)

print("Now let's rewind the file")

rewind(current_file)

print("Now let's print three lines of the file")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line =current_line + 1
print_a_line(current_line, current_file)
