# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.Make sure to use only higher order functions.

def find_values(lst):
    for i in lst:
        if i % 3 != 0 and i % 7 == 0:
            print(i)

if __name__ == "__main__":
    find_values([3,7,11,54,63])

