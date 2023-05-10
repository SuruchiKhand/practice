# 10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

given_num = input("Enter the numbers separated by commas: ")
list1 = given_num.split(',')
tuple1 = tuple(list1)

print(list1)
print(tuple1)
