#this is the 10th exercise of the book about prompting users for input

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh", end=' ')
weight = input()

print(f"So, you are {age} years old, {height} tall and weight {weight} kilos.")


#this is the 11th exercise of the book and about prompting users with hint

age1 = input("How old are you? >")
height1 = input("How tall are you? >")
weight1 = input("How much do you weigh? >")

print(f"So, you are {age1} years old, {height1} tall and weight {weight1} kilos.")
