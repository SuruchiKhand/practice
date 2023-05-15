# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

import math

C = 50
H = 30
D = input("Enter the values of D: ")
D = D.split(',')

result_list = []
for i in D:
    final_result = round(math.sqrt(2*50*int(i) / 30))
    result_list.append(final_result)
print(result_list)