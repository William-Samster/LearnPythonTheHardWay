#this is the 13th exercise of the book about parameters and unpacking variables
import sys
print(sys.version)
print(sys.executable)
from sys import argv

script, one, two, three = argv

print("Your script is", script)
print("Your first parameter is", one)
print("Your second parameter is", two)
print("Your thirs parameter is", three)
