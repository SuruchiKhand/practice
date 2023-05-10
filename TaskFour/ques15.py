# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.

def multiply(x):
    return(x*x)

func = [multiply]
for i in range(5):
    values = list(map(lambda x: x(i), func))
    print(values)


