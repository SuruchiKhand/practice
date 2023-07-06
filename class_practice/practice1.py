'''
list1 = [44,66,22,33,1,22]
# print(list1)
'''
# completely changes the list
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
'''
print(sorted(list1))
print(list1)
print(sorted(list1, reverse=True))
print(list1)

list1.reverse()
print(list1)
print(min(list1))
print(sum(list1))
print(list1.count(33))
print(list1.index(22))
print(list1[-3])

list1 = ['a', 'A', 'abc']
print(min(list1))
print(max(list1))
# print(sum(list1))

#Slicing
# [start:end:step]
list1 = [22,33,77,11,6]
print(list1)
print(list1[2:5:2])
print(list1[1:])


# input
n = int(input())
print(n)
print(n+9)
print(type(n))

'''
'''
#tuples , can do typecasting change to list and again change to tuple
tup=(34,20,99,13,65)
tup1 = (1,2,3,4)
print(tup+tup1)
print(type(tup))
print(tup[2])
# tup[2] = 555
# print(tup)
print(len(tup))
print(tup.count(24))
'''
'''
x = (1,2,3,4)
# y = []
y = list(x)
print(y)
# y[3] = 9
print(y)
x = tuple(y)
print(x)

#sets can only contain unique values, unordered elements, cannot be indexed
set1 = {44,55,11,2,9,6}
print(set1)
set1.add(10)
print(set1)
set1.remove(10) # will give error if element is not present
print(set1)
# set1.discard(55)  will not give error
print(set1)

set2 = {1,2,3,4}
set3 = {2,6,4,8}
set2.update(set3)
print(set2)


#dictionary, ordered elements, key and value pairs, have unique keys but values can be same

dict1 = {'k1': 'v1',
         'k2': 'v2',
         'k3': 'v3',
         'k4': 'v4'}
print(dict1)
print(dict1['k2'])
dict1['k3']= ['value3']
print(dict1)
dict1['k5']= 'v5'
print(dict1)
# clear deletes values but prints empty dict
dict1.clear() 
print(dict1)
del dict1
print(dict1)


# looping statements

lst = [1,2,3,4,5,6,7]
for m in lst:
    print(m)

for m in range(1,8):
    print(m)



# lst=[1,2,3,4,5,6,7]
# a = 0
# while a<len(lst):
#     print(lst[a])
#     a+=1

a = 5
while a >= 1:
    print(a)
    a-=1

dict1 = {'k1': 'v1',
         'k2': 'v2',
         'k3': 'v3',
         'k4': 'v4'}
print(dict1)

for m in dict1.keys():
    print(m)
for m in dict1.values():
    print(m)
for m in dict1.items():
    print(m)


# break, continue

# breaks comes out of loop
a=0
while a<=5:
    print(a)
    if a == 3:
        break
    a+=1

# continues with the condition
a=0
while a<=5:
    print(a)
    if a==3: 
        continue
    a+=1



# List Comprehension and Dictionary Comprehension

list1 = []
for m in range(1,11):
    list1.append(m**2)
print(list1)


list1 = [m**2 for m in range(1,11)]
print(list1)

dict1 = {}
for m in range(1,11):
    dict1[m] = m **2
print(dict1)

dict1={m:m**2 for m in range(1,11)}
print(dict1)
'''

