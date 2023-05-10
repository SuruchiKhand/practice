# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

def count_upperlower(str):
    upper = sum(1 for i in str if i.isupper())
    lower = sum(1 for i in str if i.islower())
    print("No. of Uppercase characters : ", upper, "No. of Lower case Characters : ", lower)

if __name__ == "__main__":
    count_upperlower("abcSdefPghijQkl")
                     