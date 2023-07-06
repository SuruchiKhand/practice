def remove_duplicates(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l

if __name__ == "__main__":
   
    nums = [0,0,1,1,1,2,2,3,3,4]
    expectedNums = [0,1,2,3,4]

    k = remove_duplicates(nums)
    print(k)
    assert k == len(expectedNums);
    for i in range(0, k):
        assert nums[i] == expectedNums[i];
    

        





