def solution(inputString):
    reversed_string = inputString[::-1]
    if inputString == reversed_string:
        return True
    else:
        return False
    

if __name__ == "__main__":
    #print(solution("aabab"))

    testStr = "HelloWorld"
    test1 = testStr[::-1]
    print(test1)