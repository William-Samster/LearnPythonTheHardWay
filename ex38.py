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


# this is the 39th exercise of the book and more stuff with dictionaries

things = ['a','b', 'c', 'd','e']
print(things[1])
#replacing an item in the dictionaries
things[1] = 'z'
print(things[1])
print(things)

#there are other ways of storing in a dictionary using indexes

stuff = {'name':'Som', 'age':'32', 'height':'5.10'}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

#creating a mapping of state to abbreavation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California':'CA',
    'Newyork':'NY',
    'Michigan':'MI'
}


#create a basic set of states and some cities in them

cities = {
    'CA':'Sanfransisco',
    'MI':'Detroit',
    'FL':'JacksonVille'
}

#add some more cities

cities['NY'] = 'Newyork'
cities['OR'] = 'Portland'

#print some cities
print('--'*10)
print("NY state has", cities['NY'])

# print some states
print('--'*10)
print("Michigan abbreviation is", states['Michigan'])

# do it now by using the cities and states dictionaries

print('--'*10)
print("Michigan has", cities[states['Michigan']])
print("Florida has", cities[states['Florida']])

#print every state abbreviation
print('--'*10)
for state, abbrev in list(states.items()):
    print(f"The abbreve of {state} is {abbrev}")
    print(f"and has city {cities[abbrev]}")
    print('--'*10)

#safely get a abbreviation by state that might not be there

state = states.get('Texas')

if not state:
    print("Sorry no Texas")

# get city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for state 'TX' is : {city}")
