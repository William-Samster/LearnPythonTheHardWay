#this is the 31st exercise of the book about making decisions

#this is the welcome message to the game

print("""You enter a dark room with two doors
which door will you select # Door 1 or # Door 2""")

#this is where we collect the input from the user

door = input(">")

#based on the  door input we apply the following logic

if door == "1":
    print("There is a giant bear here eating cheese cake")
    print("What would you do?")
    print("""    1. Take the cheese cake
    2. Scream at the bear""")
    choice = input(">")

    #now based on the user choice we will proceed in one of the two directions
    #mentioned below

    if choice == "1":
        print("The bear eats your face off. Great Job!")
    elif choice == "2":
        print("The bear eats your leg off. Great Job")
    else:
        print(f"Well doing {choice} is probably better!")

elif door == "2":
    print("You stare into the endless abbys of the Chitula's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolver yelling melodies")

    choice = input(">")

    #Now based on the users choice we will take them in one of the two options

    if choice == "1" or choice == "2":
        print("Your body survives powered by the mind of jello")
        print("Good Job!!")
    else:
        print("You stuble around and fall on a knife and die. Good Job!")
