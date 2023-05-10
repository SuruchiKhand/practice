# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT


def all_capitalize(given_str):
    capitalized_string = given_str.upper()
    print(capitalized_string)

if __name__ == "__main__":
    all_capitalize("this is me")
