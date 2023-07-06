import math

def solution(year):
    # return math.ceil(year/100)
    return math.floor(year/100)

if __name__ == "__main__":
    print(solution(1905))
    print(solution(99))