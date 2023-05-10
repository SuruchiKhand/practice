# 3. Write a program to get the sum and multiply of all the items in a given list.

list1 = [1,2,3,4,5]
def multiplyList(list1):
    result = 1
    for i in range(0,len(list1)):
        result = result * list1[i]
    return result

print(sum(list1))
print(multiplyList(list1))


from functools import reduce
result1 = reduce((lambda x,y: x * y), list1)
print(result1)
