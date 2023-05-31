# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.

# using traditional function and loop
# def multiply_elements(list1):
#     new_list = []
#     for i in list1:
#         new_list.append(i * i)
#     print(new_list)

#  using map and traditional function   
# def multiply_elements(n):
#     return n * n

# def multiply_list(list1):
#     result = map(multiply_elements, list1)
#     return list(result)

# using lambda
def multiply_list(list1):
    result = map(lambda x: x * x, list1)
    return list(result)

if __name__ == "__main__":
    print(multiply_list([0,1,2,3,4]))
