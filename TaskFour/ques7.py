# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.

def max_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len(str1) == len(str2):
        print(str1,"\n",str2)

    elif len1 > len2:
        print(str1)
    else:
        print(str2)
    
if __name__ == "__main__":
    max_length("hello", "Jainika")

