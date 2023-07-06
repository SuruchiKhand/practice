# def valid_palindrome(string):
#     new_string = "".join(string.split())
#     print(new_string)

#     lower_newstring = new_string.lower()
#     print(lower_newstring)

#     alpha_string = "".join( i for i in lower_newstring if i.isalpha() or i.isnumeric())
#     print(alpha_string)

#     reversed_alphastring = alpha_string[::-1]
#     print(reversed_alphastring)

#     if alpha_string == reversed_alphastring:
#         print("true")
#     else:
#         print("false")


# if __name__ == "__main__":
#     # valid_palindrome("Was it a car or a cat I saw!!")
#     # valid_palindrome("A man, a plan, a canal: Panama")
#     # valid_palindrome("race a car")
#     # valid_palindrome(" ")
#     valid_palindrome("0P")


def valid_palindrome(str):
    l = 0
    r = len(str) - 1

    while l < r:
        while l < r and not alpha_numeric(str[l]):
            l += 1
        while l < r and not alpha_numeric(str[r]):
            r -= 1
        if str[l].lower() != str[r].lower():
            return False
        l += 1
        r -= 1
    return True

def alpha_numeric(c):
    return (ord('a')<= ord(c)<= ord('z') or ord('A')<= ord(c)<= ord('Z') or ord('0')<= ord(c)<= ord('9'))

if __name__ == "__main__":
    # print(valid_palindrome("Was it a car or a cat I saw!!"))
    # print(valid_palindrome("A man, a plan, a canal: Panama"))
    print(valid_palindrome("race a car"))
    



