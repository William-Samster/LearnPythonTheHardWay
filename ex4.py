# this is the 4th exercis in the book about variables

cars = 100
space_in_the_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_the_car
avg_passenger_per_car = passengers/cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars")
print("We can transport", carpool_capacity, "people")
print("We have", passengers, "to carpool today.")
print("We need to put", avg_passenger_per_car, "in each car")

# this is the 5th exercis in the book about more variables and printing

my_name = 'Som'
my_age = 32
my_height = 70 #inches
my_weight = 94 #kilos
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} kilos heavy")
print("Actually that's not to heavy")
print(f"He's got {my_eyes} coloe eyes and {my_hair} color hairs")
print(f"His teeth is usually {my_teeth} depending on the coffee")

total = my_age + my_weight + my_height
print(f"If I add {my_age}, {my_weight}, and {my_height}, I will get {total}")
