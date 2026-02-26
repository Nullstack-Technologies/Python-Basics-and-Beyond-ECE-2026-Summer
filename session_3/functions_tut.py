import math

def greet():
    print("Hello EIEM")

# greet()


def add(a, b):
    return a + b

result = add(2,3)
# print(result)


def area_of_circle(radius):
    return math.pi * radius ** 2

# print(round(area_of_circle(7), 2))


def greet_me(first_name="Nauman", last_name="Arif"):
    count_of_characters = len(first_name) + len(last_name)
    return first_name + " " + last_name, count_of_characters

# print(greet_me())


def fact(a):
    result = 1
    while a > 1:
        result = result * a
        a = a - 1
    return result
#6! = 6 * 5 * 4 * 3 * 2 *1

# print(fact(3)) 

def is_prime(n):
    # check whether the number is greater than 0
    # else return false
    if n < 1:
        return False
    
    for i in range(2, n // 2):
        if n % i == 0: 
            return False
    
    return True

# print(is_prime(5))
# print(is_prime(6))



def fact_2(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * fact_2(n-1)

# result = fact_2(6)
# print(result)   

a = ["apple", "cherry", "tomato", "orange"]
# list_length = len(a)
# a_reverse = a
# i = 0
# while i < list_length:
#     a_reverse[i] = a[list_length -i - 1]
#     i = i + 1
# print(a_reverse)

def print_reverse(value):
    if not value:
        return
    else:
        size = len(value)
        print(value[size-1], end=" ")
        print_reverse(value[:size -1])
        
# print_reverse(a)

# * args, *kwargs


def add(*args):
    sum = 0
    for _ in args:
        sum = sum + _
    return sum

result = add(1,2,3,4,5,100, 200)
# print(result)

def person_details(**kwargs):
    print(kwargs)

# person_details(name= 'Nauman', college= 'EIEM')

def test_1(*args, **kwargs):
    print(args, kwargs)

# test_1(1,2,3,4,5,5, name="Nauman", gender="M")



def avg(*args):
    # sum of all args

    # average = sum / number of args

    # return average
    pass

a =int(input())
for i in range(1, 50) :
    if i%2 != 0 or i%3 != 0 :
        print(i, end=" ")



