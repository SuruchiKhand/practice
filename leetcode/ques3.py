def solution(inputArray):
    max_num = max(inputArray)
    max_num_index = 0
    for i in range(0,len(inputArray)):
        if max_num == inputArray[i]:
            max_num_index = i

    if max_num_index == len(inputArray) - 1:
        return max_num * inputArray[max_num_index - 1]

    elif max_num_index == 0:
        return max_num * inputArray[max_num_index + 1]

    else:
        left_product = max_num * inputArray[max_num_index - 1]

        right_product = max_num * inputArray[max_num_index + 1]

        if left_product > right_product:
            return left_product
        else:
            return right_product

def solution_test(inputArray):
    sum_list = []

    for i in range (0, len(inputArray) - 1):
        sum_list.append(inputArray[i] * inputArray[i + 1])

    print(sum_list)

    return max(sum_list)

if __name__ == "__main__":
    print(solution_test([9, 5, 10, 2, 24, -1, -48]))
    print(solution_test([4, 1, 2, 3, 1, 5]))