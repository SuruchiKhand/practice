# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
    # If User Enter 1 - Addition
    # If User Enter 2 - Subtraction
    # If User Enter 3 - Division
    # If User Enter 4 - Multiplication
    # If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.

choose_option = input("Choose the following option first: 1) Addition | 2) Subtraction | 3) Division | 4) Multiplication 5) Average [1/2/3/4/5]")

num1= int(input("Choose a number: "))
num2= int(input("Choose another number: "))
    
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

list1 = [num1, num2, first_number, second_number]
n = len(list1)

if choose_option == '1':
    result = num1 + num2
    print('You picked addition. The sum is', result)
    
elif choose_option == '2':
    result = num1 - num2
    print("You picked Subtraction. The result is ", result)

elif choose_option == '3':
    result = num1 / num2
    print("You picked Division. The result is ", result)

elif choose_option == '4':
    result = num1 * num2
    print("You picked Multiplication. The result is ", result)

elif choose_option == '5':
    sum1 = sum(list1)
    result = sum1/n
    print("You picked Average. The result is ", result)

else:
    pass

if result > 0:
    print("The result is a Positive number")
else:
    print("The result is a Negative number")





    





