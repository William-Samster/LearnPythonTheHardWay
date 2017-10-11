#this is the 18th exercise of the book about functions

def print_two(*args):
    arg1, arg2 = args
    print(f"arg 1 = {arg1} and arg2 = {arg2}")

#we can do the above in a different way of giving two arguments

def print_two_again(arg1, arg2):
    print(f"arg1 = {arg1} and arg2 = {arg2}")

#this does not take any arguments

def no_arg():
    print("I got nothing")

print_two("Zed","Som")
print_two_again("Som", "Zed")
no_arg()


#this is the 19th exercise of the book more about functions

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for the party")
    print("Get a blanket \n")

print("We ca just give the fucntions number directly")

cheese_and_crackers(20, 10)

print("Or we can use variable from our script")
amount_of_cheese = 20
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do the math inside too")

cheese_and_crackers(10+5, 20+5)
