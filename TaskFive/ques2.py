# 2. Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.

try:

    ask_user = input("Enter the file name: ")

    f = open(ask_user)
    c = f.read()
    print(c)

except: 
    print("Something went wrong. Please enter the correct file name.")
