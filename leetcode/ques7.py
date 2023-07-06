# nums = [3,2,2,3], val = 3
# output = 2 , [2,2]

# nums = [0,1,2,2,3,0,4,2], val = 2
# output = 5

def remove_element_2(nums, val):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count +=1
    return count

# def remove_element(nums, val):
#     list1 = []
#     for i in range(0, len(nums)):
#         if nums[i] != val:
#             list1.append(nums[i])
#         i += 1
#     return len(list1)
    
if __name__ == "__main__":
    print(remove_element_2([3,2,2,3], 3))
    print(remove_element([0,1,2,2,3,0,4,2], 2))
