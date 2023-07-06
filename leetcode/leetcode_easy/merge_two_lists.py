'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
list1.extend(list2)
    return sorted(list1)
'''
def merge_two_lists(list1, list2):
    new_list = []
    i,j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i +=1
        else:
            new_list.append(list2[j])
            j += 1
    new_list = new_list + list1[i:] + list2[j:]
    return new_list

if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    # print(list1)
    # print(list2)
    print(merge_two_lists(list1, list2))
    # print(list1)