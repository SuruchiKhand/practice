values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
def roman_to_int(str):
    total = 0
    i = 0

    while (i < len(str)):
        str1 = values[str[i]]
        if (i + 1 < len(str)):
            str2 = values[str[i + 1]]
            if (str1 >= str2):
                total = total + str1
                i = i + 1
            else:
                total = total - str1
                i = i + 1
        else:
            total = total + str1
            i = i + 1
    return total
    

if __name__ == "__main__":
    print(roman_to_int("LVIII"))



