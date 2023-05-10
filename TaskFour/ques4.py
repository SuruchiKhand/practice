# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

given_words = input("Enter hypen separated sequence of words: ")
list1 = list(given_words.split("-"))
sorted_words = list1.sort()
print('-'.join(list1))

