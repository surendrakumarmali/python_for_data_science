################################################
# beginner's python code
# written by: Hari
################################################


# Hello world
print("Hello, World!")

# hello world with a variable
# variables are used to store values
msg = "Hello world!"
print(msg)

# concatenation (combinig strings)
first_name = 'hari'
middle_name = 'shanker'
last_name = 'gupta'
full_name = first_name + ' ' + middle_name + ' ' + last_name
print(full_name)

# lists
# a list stores a series of items in a particular order,
# you access items using an index, or within a loop
bikes = ['trek', 'redline', 'giant']
# first items
first_bike = bikes[1]
last_bike = bikes[-1]
print(bikes)
# looping thorough a list
for bike in bikes:
    print(bike)
# adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
print(bikes)

# making numerical lists
squares = []
for x in range(1,11):
    squares.append(x**2)
print(squares)

#slicing a list
# first four
print(squares[0:4])
# count from last, leaving the last index
print(squares[-4:-2])
# copying a list
copy_of_bikes = bikes[:]
# list comprehensions
squares = [x**2 for x in range(1,11)]
print(squares)

# tuples
# tuples are similar to list, but items in tuples can not be modified
# making a tuple
dimensions = (101, 80)
print(dimensions)

# dictioaries
# dictionaries store connections between pieces of information,
#  each item in a dictionary is a key-value pair
# a simple dictionary
alien = {'color': 'green', 'points': 5}
#accessing a value
print("The alien's color is " + alien['color'])
#adding a new key-value pair
alien['x_position'] = 0
print(alien)
# looping through all key-value pairs
fav_numbers = {'eric': 17, 'ever': 4}
print(fav_numbers)
fav_numbers.items()
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))
# looping through all keys
for name in fav_numbers.keys():
    print(name + ' loves a number')
# looping through all the values
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')
######################
# if statements
######################
#conditional tests

######################################
# sum of two numberss
######################################

num1 = 5
num2 = 7
sum = num1 + num2
print(sum)

