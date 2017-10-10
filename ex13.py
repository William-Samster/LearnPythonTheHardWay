#this is the 13th exercise of the book about parameters and unpacking variables

from sys import argv

script, one, two, three = argv

print("Your script is", script)
print("Your first parameter is", one)
print("Your second parameter is", two)
print("Your thirs parameter is", three)


#this is the 14th exercise of the book about prompting and passing

from sys import argv

script, user_name = argv
prompt = ">"

print(f"Hi {user_name}, I am {script} script")
print("I would like to ask you a few questions")
print(f"Do you like me {user_name}?")

likes = input(prompt)
