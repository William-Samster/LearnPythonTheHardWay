#this is the 32nd exercise of the book about loops and lists

# this is where we declare the lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots',]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# the first kind if for-loop goes through the lists

for number in the_count:
    print(f"The number is {number}")

for fruit in fruits:
    print(f"The fruit is {fruit}")

for i in change:
    print(f"The change is {i}")


element = []

for i in range(0,6):
    x = input(">")
    print("Adding this to the list")
    element.append(x)

#Now print them too

for i in element:
    print(f"The element is {i}")

# this is the 33rd exercise of the book about while loops

i = 0
number = []

while i < 6:
    print(f"At the top i is {i}")
    number.append(i)
    i = i+1
    print(f"The number now is {number}")
    print(f"At the bottom i is {i}")
    print("------")

print("The numbers are:", number)

for num in number:
    print(num)

# Just testing out how to reach items in the lists

print(f"The fifth element is {element[4]}")
