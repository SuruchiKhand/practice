# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

while True:
    user_input = int(input(("Enter a number: ")))
    if user_input >= 0:
        print("Good Going")
        continue
    if user_input < 0 :
        print("It's over")
        break
    
   





    

  