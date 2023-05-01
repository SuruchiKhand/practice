# 3. Swap two numbers using a third variable and do the same task without using any third variable.

a = 1
b = 2

c = a
a = b
b = c

print("a: ", a)
print("b: ", b)

#  without using third variable

a,b = b,a

print("a: ", b)
print("b: ", a)
