# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

from functools import reduce
def convert(lst):
    concat_lst = [str(i) for i in lst]
    res = reduce(lambda x,y: x + y, concat_lst)
    return int(res)

if __name__ == "__main__":
    print(convert([1,2,3,4,5,6,7]))
