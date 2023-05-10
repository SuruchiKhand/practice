# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).

def generate_tuple():
    list1= list()
    for i in range(1, 21):
        list1.append(i**2)
    
    return tuple(list1)


if __name__ == "__main__":
    print(generate_tuple())