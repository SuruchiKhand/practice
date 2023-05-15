# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”

def reverse_string(str):
    length = len(str)
    for i in range(length-1, -1, -1):
        yield str[i]

for char in reverse_string("Consultadd Training"):
    print(char)
                           