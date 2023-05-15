# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.

def find_upper(str):
    res = [char for char in str if char.isupper()]
    return res

if __name__ == "__main__":
    print(find_upper("TellMemOre"))
