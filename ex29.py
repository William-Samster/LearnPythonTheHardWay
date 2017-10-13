#this is the 29th exercise of the book and about if loops

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats")

if people > cats:
    print("Not too many cats, the world is saved")

if people < dogs:
    print("The world is drooled on")

if people > dogs:
    print("The world is dry")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs")

#this is the 30th exercise of the book about else and elseif

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")

elif cars < people:
    print("We shoud not take the cars")

else:
    print("We can't decide")


if trucks > cars:
    print("There are too many trucks")

elif trucks < cars:
    print("There are too many cars")

else:
    print("There is enough")

if people > trucks:
    print("Alright! Let's just take the trucks")

else:
    print("Fine! Let's stay home")
