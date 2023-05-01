# 8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2


all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def calculate_digits_letters(str):
    total_digits = 0
    total_letters = 0
    for s in str:
            
        if s in all_digits:
            total_digits += 1

        else:
            total_letters += 1

    print("Total letters found: ", total_letters)
    print("Total digits found:  ", total_digits)

if __name__ == "__main__":
    calculate_digits_letters("consul72")

