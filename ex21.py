#This is the 21st exercise of the book about more functions and stuff they RETURN

def add(a,b):
    print(f"We are adding {a} and {b}")
    return a + b

def substract(a,b):
    print(f"We are substracting {a} and {b}")
    return a - b

def multiplying(a,b):
    print(f"We are multiplying {a} and {b}")
    return a * b

def divide(a,b):
    print(f"We are dividing {a} and {b}")
    return a / b

print("Let's do some math just with functions")

age = add(30, 20)
height = substract(80, 70)
weight = multiplying(20, 4)
iq = divide(200, 3)

print(f"Age : {age}, Height : {height} , weight: {weight} and IQ: {iq}")

print("Here is a puzzel")

#what = add(age, substract(height, multiplying(weight. divide(iq, 2))))
