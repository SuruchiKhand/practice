# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(list1):
    num = []
    for i in list1:
        if i not in num:
            num.append(i)
    return num

print("The unique elements are")
print(unique([1,2,4,5,4,5,6,9,10]))



