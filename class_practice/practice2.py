# functions
'''
def greet(name):
    print("Hello", name)

greet("Apple")

# positional argument
def add(num1, num2):
    result = num1 + num2
    return result
a = add(2,3)
print(a)


#Types of arguments
# Keyword Argument
def add(num1, num2):
    print("num1 = ", num1)
    print("num2= ", num2)
add(num1=99, num2= 1)


# default arguments
def add(num1, num2=8):
    print("num1 = ", num1)
    print("num2= ", num2)
add(7)
add(4,2)


# arbitrary argument - when you don't know how many arguments to pass, values in the form of tuple
def desc(*arg):
    print(arg)
desc(12,34,2,434)


# keyword arbitrary argument- in the form of dictionary
def desc(**kwargs):
    print(kwargs)
desc(k1=6, k2=8, k3=7)


# recursion function - if the function calls itself

def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return(num*fact(num-1))
print(fact(1))

# lambda functions - anonymous and inline function
# def func(arg1):
#     arg1 + 10

x = lambda arg1:arg1 +10
print(x(5.8))

x=lambda arg1,arg2:arg1 +arg2
print(x(23,22))

x = lambda num: "Even" if num % 2 == 0 else "Odd"
print(x(21))


# main function
# print("__name__")
def desc():
    print("Describe a function")
if __name__ == "__main__":
    print("Inside function")
    print("here")
    desc()

# high order functions, using multiple functions as an argument
def sum(num1, num2):
    return num1 + num2
def max(num1 = 0, num2 = 0):
    if num1 > num2:
        return num1
    else:
        return num2
print(max(20, sum(2,4)))


# filter, map and reduce
# filter = takes sequence, filter things out
nums = [3,2, 5,7,4]
evens = list(filter(lambda n:n%2 ==0, nums))
# print(evens)

# map = to perform operations on the elements
# doubles = list(map(lambda n:n*2,nums))

doubles = list(map(lambda n:n*2,evens))
print(doubles)

# reduce , reduce multiple values into one
nums = [3,2, 5,7,4]
doubles = list(map(lambda n:n*2,nums))
print(doubles)

from functools import reduce
sum=reduce(lambda a,b: a+b, doubles)
print(sum)




# Lambda functions can have any number of parameters but the function body can only contain one expression.

# lambda p1,p2: expression,p1,p2 are parameters

adder = lambda x,y: x + y
print(adder(1,2))

string='some kind of a useless lambda'
print(lambda string:print(string))

# instead write like this

x ="some kind of a useless lambda"
(lambda x:print(x)) (x)


def guru(funct, *args):
    funct(*args)
def printer_one(arg):
    return print(arg)
def printer_two(arg):
    print(arg)

guru(printer_one, 'printer 1 regular call')
guru(printer_two, 'printer 2 regular call')

guru(lambda:printer_one('printer 1 lambda call'))
guru(lambda:printer_two('printer 2 lambda call'))


# (lambda x:x+x)(2)

# filter and lambdas
sequences = [10,2,8,7,4,3,11,0,1]
filtered_result = filter(lambda x:x > 4, sequences)
print(list(filtered_result))

sequences = [2,4,6,8,9,12,14,19]
filtered_result = filter(lambda x:x%2==0, sequences)
print(list(filtered_result))


# map and lambda
sequences = [2,4,6,8,9,12,14,19]
filtered_result = map(lambda x:x*x, sequences)
print(list(filtered_result))



# reduce and lambda
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce(lambda x,y: x * y, sequences)
print(product)

sequences = [1,2,3,4,5]
sum = reduce(lambda x,y: x + y, sequences)
print(sum)



# map and lambda
sequences = [2,4,6,8,9,12,14,19]
filtered_result = map(lambda x: x+10, sequences)
print(list(filtered_result))

# syntax for writing lambda is :lambda parameter: expression
# Filter: filter (lambda parameter: expression, iterable-sequence)
# Map: map (lambda parameter: expression, iterable-sequences)
# Reduce: reduce (lambda parameter1, parameter2: expression, iterable-sequence)


String interpolation Python
day = "Friday"
activity = 'bowling'
print(f"Let's go {activity} on {day} afternoon.")


berries = ['grape', 'tomato', 'cucumber', 'egglant', 'banana', 'watermelon', 'pumpkin']
print(type(berries))
print(berries[1])
print(berries[-1])
print(berries[2:4])
print(berries[:3])
print(berries[2:])



jeff = {
    'name': 'jeff',
    'age': 44,
    'job': 'influencer'
}
print(jeff['age'])


people = [
    {
        'name': 'alice',
        'age': 44,
        'job': 'influencer',
    },
    {
        'name': 'bob',
        'age': 31,
        'job': 'dog walker'
    },
    {
        'name': 'carol',
        'age': 65,
        'job': 'life coach',
    },
]
print(people[1]['name'])
'''

def gimme_five():
    return 5
print(gimme_five() + 10)