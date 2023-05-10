# 16. What is the output of the following codes:
def foo():
    try:
        return 1
    finally:
        return 2

k = foo()
print(k)

# OUTPUT: 2

# def a():
#     try:
#         f(x, 4)
#     finally:    
#         print('after f')
#         print('after f?')
# a()

# Output: NameError: name 'f' is not defined