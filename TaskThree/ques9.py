# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

given_num =  int(input("Enter a number: "))
dict1 = dict()
for i in range(1,given_num+1 ):
    dict1[i] = i * i

print(dict1)


# 
# dict1 = {x:x * x for x in range(1, given_num+1)}
# print(dict1)