# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the numbers in the filtered list. Use lambda() to define anonymous functions.


def even(num):
    return num % 2 == 0
        
def square(num):     
    return num ** 2

list1 = [i for i in range(1,11)]
list1 = map(square,filter(even,list1))
print(list(list1))