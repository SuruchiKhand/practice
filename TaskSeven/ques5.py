# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a parameter. The constructor must assign the integer value to the age variable after confirming the argument passed is not negative; if a negative argument is passed then the constructor should set age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance methods:

# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
    # f age is between 0 and <13, print “You are young”.
    # If age is >=13 and <=19 , print “You are a teenager”.
    # Otherwise, print “You are old”.


class Person:
    def __init__(self, initialAge):
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            self.age = 0

        else:
            self.age = initialAge

    def amIOld(self):
        if(self.age < 13):
            print("You are young.")
        elif(self.age >= 13 and self.age < 18):
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):
        self.age += 1




