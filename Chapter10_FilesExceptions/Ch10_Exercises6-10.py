# 10-6 Addition of numbers with ValueError exception by providing text instead of a number.
# 10-7 Use a while loop for the calculator to continue.

print("Provide two numbers, and I will try to add them.")
print("Enter 'q' to quit the program.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please type in numbers for input. I don't understand text!")
    else:
        print(f"{first_number} + {second_number} = {answer}")


# 10-8 Cats and Dogs with FileNotFoundError.
# 10-9 Modify except block to fail silently if file is missing.

def open_file(filename):
    """Open the file and print the contents of them with try-except block."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # pass
        print(f"Sorry, the file {filename} is missing!")
    else:
        print(contents)

# Correct file paths to run without any errors.      
# filenames = ['Chapter10_FilesExceptions/cats.txt', 'Chapter10_FilesExceptions/dogs.txt']

# Wrong file paths to fail silently.
filenames = ['Chapter10_FilesExceptions/cat.txt', 'Chapter10_FilesExceptions/dog.txt']
for filename in filenames:
    open_file(filename)




# 10-10 Find common words between texts analyzed.

def count_words(filename):
    """Open the file and print the contents of them with try-except block."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} is missing!")
    else:
        # Match all cases with lowercase words.
        words = contents.lower().split()
        print(f"In {filename}, there are {words.count('and')} for the word 'and'.")

filenames = [
    'Chapter10_FilesExceptions/ion.txt',
    'Chapter10_FilesExceptions/prideprejudice.txt',
    'Chapter10_FilesExceptions/ulysses.txt']

for filename in filenames:
    count_words(filename)

