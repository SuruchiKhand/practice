# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}
def Merge(a,b):
    for i in b.keys():
        a[i] = b[i]
    return a
c = Merge(a,b)
print(c)

# def Merge(a, b):
#     res = {**a, **b}
#     return res
     
# c = Merge(a, b)
# print(c)