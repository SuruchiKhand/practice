# 6. Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:


f = open("try.txt")
c = f.read()
# print(c)
a = c.split(" ")
# print(a)
for word in a:
    if len(word) % 2 == 0:
        print(word)