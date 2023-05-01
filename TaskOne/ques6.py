# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc


user_input= input("Enter the value: ")
try:
    value=int(user_input)
    print("The data type of the input value is : ", type(value))
except ValueError:
    try:
        value = float(user_input)
        print("The data type of the input value is : ", type(value))
    except ValueError:
        print("The data type of the input value is String.")