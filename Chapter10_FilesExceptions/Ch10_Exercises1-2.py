# 10-1 Learning Python

filename = 'Chapter10_FilesExceptions/learning_python.txt'

print("Reading the entire file...")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print("\nLooping line by line...")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\nReading by storing the lines in a list and outside the with block...")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())



# 10-2 Learning C by using replace() any word in a string with a different word.

with open('Chapter10_FilesExceptions/learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))