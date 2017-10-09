# this is the 6th exercise of the book about stings and text

types_of_people = 10
x = f"there are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said :{x}")
print(f"I also said :{y}")

# this part shows how to print a variable in a sentence in a different way
hilarious = False
joke_evaluation = "Isn't that joke so funny? {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with the right side"

print(w + e)
