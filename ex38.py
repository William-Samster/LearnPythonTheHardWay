#this is the 38th exercise of the book and getting starte with directories

ten_things = "Apples, Ornages, Crow, telephone, Light, Sugar"
print("Wait! There are not ten things in that list. Let's fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbie", "Corn", "Banana", "Girl", "Boy"]


#now running the while loop on stuff

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print("There we go:", stuff)

print("Let's do somethings with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
