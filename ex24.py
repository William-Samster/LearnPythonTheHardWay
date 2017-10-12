#this is the 24th exercise of the book and basically practising all the things
#I have learnt till now

print("Let's practise everything")
print('You\' d need to know \' about escapes with \\ that do:')

print('\n newlines \t tabs.')

poem = """
\t The lovely world with logic so firmly planted
that cannot discern \n the need for love or the passion
from intitution \n and requires an explanation \n\t\t where
there is none."""

print("-----")
print(poem)
print("-----")

five = 10 - 2 + 6 - 6
print(f"This should be {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jar = jelly_beans /1000
    crates = jar / 100

    return jelly_beans, crates, jar

start_point = 10000
beans, crates, jars = secret_formula(start_point)
#this is another way of formating a substracting
print("With a starting point of {}".format(start_point))
print(f"We have {beans} beans, {crates} crates and {jars}")

start_point = start_point / 10
print("We can also do it this way")
formula = secret_formula(start_point)
print(formula)
print("We have {} beans, {} crates and {} jars".format(*formula))
