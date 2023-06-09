# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def showNumbers(limit):
    for i in range(0,limit):
        if i == 0 or i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")


if __name__ == "__main__":
    showNumbers(3)
    showNumbers(9)