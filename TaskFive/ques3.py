# 3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”


try:
    x = int(input("Enter only four digits: "))
                
except:
        print("The length is too short/ long !!! Please provide only four digits")
        
if len(str(x)) == 4:
      print(x)

else:
      print("The length is too short/ long !!! Please provide only four digits") 
