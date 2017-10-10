#this is the 15th exercise of the book and about reading files

from sys import argv

script, file_name = argv

txt = open(file_name)
print("Here is your file", file_name)
print(txt.read())

print("Type the file name again")

file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())

#this is the 16th exercise of the book about reading and writing files

print("We are going to erase the file", file_name)
print("If you don't want that then press CLTR C")
print("If you want to erase the file then press RETURN")

input('?')

target = open(file_name, 'w')
print("Truncating the file. Good Bye!")
target.truncate()

print("Now I am going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these three lines to the file", file_name)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it")
target.close()
