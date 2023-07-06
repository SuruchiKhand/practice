# def shape_area(n):
#     # if n >= 10 ** 4 or n < 1:
#     if n < 1:
#         return False
    
#     return (n**2+(n-1)**2)

# if __name__ == "__main__":
#     print(shape_area(0))


array_1 = [6,2,3,8]

sorted_arr = sorted(array_1)
print(sorted_arr)

additional_statues = 0
for i in range(0,len(sorted_arr)-1):
    if sorted_arr[i + 1] - sorted_arr[i] > 1:
        additional_statues = additional_statues + sorted_arr[i + 1] - sorted_arr[i] - 1
print(additional_statues)
