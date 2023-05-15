# 2. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}


students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']

# using for loop
# result = {}
# for key in students:
#     for value in subjects:
#         result[key] = value
#         subjects.remove(value)
#         break
# print(str(result))

# using dictionary comprehension
result = {students[i]:subjects[i] for i in range(len(students))}
print(result)