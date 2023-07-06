# def reverse_string(string):
#     reversed_string = string[::-1]

#     return reversed_string

# def print_letters(string):
#     for i, element in enumerate(string):
#         print("Index ", i, "=", element)
    

def reverse_string(string):
    reverse_string = ""
    for i in range(len(string)-1, -1, -1):
        reverse_string = reverse_string + string[i]
        # print(string[i])
    return reverse_string
        
def is_palindrome(string):
    reverse_string = ""
    for i in range(len(string)-1, -1, -1):
        reverse_string = reverse_string + string[i]

    if reverse_string == string:
        return True
    else:
        return False
    


if __name__ == "__main__":
    # print(reverse_string("nisha"))
    # print(reverse_string('nisha'))
    print(is_palindrome("nisha"))




