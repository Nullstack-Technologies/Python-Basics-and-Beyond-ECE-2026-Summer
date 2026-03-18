# LIST COMPREHENSIONS
a = [1, 2, 3, 4 ,5 , 6, 7, 8, 9, 10]

# numbers = [ x * x for x in a]
# print(numbers)
# even = [x for x in a if x %2 == 0 ]
# print(even)

cube_even = [x**3 for x in a if x %2 == 0 ]
# print(cube_even)


# LAMBDA FUNCTIONS
square = lambda x: x * x
concat = lambda x,y: x + y

# print(square(5))
# print(concat("Nauman ", "Arif"))


# MAP FILTER REDUCE

b = list(map(lambda x: x * x, a))
# print(b)

c = list(filter(lambda x: x % 2 ==0, a))
# print(c)

from functools import reduce
d = reduce(lambda x, y: x + y, a)
# print(d)


# TRY EXCEPT
c = 5
d = 0
try:
    c / d
except:
    print("You tried to play me , but execution goes on")
d = 4
# print(c /d) 

# NAMING

# class PaymentDefinition:

# a = 5 
# A = 5

# def area_of_circle

