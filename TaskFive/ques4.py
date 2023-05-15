# 4. Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

username = input("Enter a username: ")
password = input("Please enter a password: ")
count=0
while count < 3:
    re_password = input("Please enter the password again: ")

    if re_password == password:
        print("Access granted")
        break


    else:
        print("ACCESS dENIED")
        count +=1
