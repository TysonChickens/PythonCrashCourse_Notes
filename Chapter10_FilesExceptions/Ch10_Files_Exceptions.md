# Python Crash Course Chapter 10: Files and Exceptions

What we will learn in this chapter:

* Work with files so programs can quickly analyze lots of data.
* Handle errors so programs don't crash when they encounter unexpected situations.
* ***Exceptions*** which are special objects Python creates to manage errors that arise while a program is running.
* The ***json*** module to allow us to save user data so it isn't lost when the program stops running.

Learning to work with files and save data will make programs easier for people to use. Users will be able choose what data to enter and when to enter it. Learning how to handle exceptions will help deal with situations in which files don't exist and deal with other problems that can cause programs to crash. This will make programs more robust when they encounter bad data, whether from innocent mistakes or from malicious attempts to break programs. The skills learned in this chapter will make programs more applicable, usable, and stable.

## Reading from a File

An incredible amount of data is available in text files. Text files can contain weather data, traffic data, socioeconomic data, literary works, and more. Reading from a file is useful in data analysis applications, but also applicable to any situation in which to analyze or modify information stored in a file.

When we want to work with information in a text file, the first step is to read the file into memory. The entire contents of a file can be read, or one line at a time.

### Reading an Entire File

To begin, we need a file with a few lines of text in it. Let's start with a file that contains *pi* to 30 decimal places, with 10 decimal places per line:

pi_digits.txt

``` markdown
3.1415926535 8979323846 2643383279
```

Here's a program that opens this file, reads it, and prints the contents of the file to the screen:

``` python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
```

The `open()` function allows us to work with any file by opening to access the contents. The `open()` function needs one argument: the name of the file to open. Python looks for this file in the directory where the program that's currently being executed is stored. Python assigns this object to *file_object*, which we work with later in the program.

The keyword *with* closes the file once access to it is no longer needed. We call `open()` in this program but not `close()` because a bug can prevent the method from being executed, and the file may never close. Improperly closed files can cause data to be lost or corrupted and a file closed too early can lead to more errors. With the structure here, Python will figure that out for us when it should close a file. All we have to do is open the file and work with it, trusting that Python will close it automatically when the *with* block finishes execution.

Once we have the file object, we use the `read()` method on the second line to read the entire contents of the file and store it as one long string in *contents*. When we print the value of *contents*, we the get the entire text file back:

``` markdown
3.1415926535 8979323846 2643383279

```

The only difference between this output and the original file is the extra blank line at the end of the output. The blank line appears because `read()` returns an empty string when it reaches the end of the file. If we want to remove the extra blank line, use the `rstrip()` in the call to `print()`:

``` python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```

Recall that Python's `rstrip()` method removes, or strips, any whitespace characters from the right side of a string.

### File Paths

Sometimes, the file we want to open won't be in the same directory with the program file. For Python to open files from a directory, we need to provide a ***file path*** to look in a specific location on the computer.

We can also provide an ***absolute file path*** to tell Python exactly where the program is stored. It is an alternative if relative path doesn't work.

Absolute paths are usually longer than relative paths, so it's helpful to assign them to a variable and then pass that variable to `open()`:

``` python
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```

### Reading Line by Line

When reading a file, going through each line of the file is helpful when looking for certain information, or to modify the text in some way. For example, reading through a file of weather data and work with any line that includes the word *sunny* in the description of the day's weather. In a news report, we might want to look for any line with the tag *headline* and rewrite that line with a specific kind of formatting.

We can use a for loop on the file object to examine each line from a file one a time:

``` python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
```

To examine the file's contents, we work through each line in the file by looping over the file object.

When we print each line, we find even more blank lines:

``` markdown
3.1415926535

8979323846

2643383279
```

The blank lines appear because an invisible newline character is at the end of each line the text file. The `print` function adds its own new line each time we call it. Using `rstrip()` on each line in the `print()` call eliminates these extra blank lines:

``` python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

Now the output matches the contents of the original file again:

``` markdown
3.1415926535
8979323846
2643383279
```

### Making a List of Lines from a File

When using *`with`*, the file object returned by `open()` is only available inside the *`with`* block that contains it. If we want to retain access to a file's contents outside, we can store the file's lines in a list inside the block and then work with that list.

The following example stores the lines of *pi_digits.txt* in a list inside the *`with`* block and then prints the lines outside the block:

``` python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

The `readlines()` method takes each line from the file and stores it in a list. This list is assigned to *lines*, which we can continue to work with after the *`with`* block ends. We then use a simple *for* loop to print each lines from *lines*. Because each item in *lines* corresponds to each line in the file, the output matches the contents fo the file exactly.

### Working with a File's Contents

After reading a file into memory, we can manipulate the data. First, we will try to attempt to build a single string containing all the pi digits in the file with no whitespace in it:

``` python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```

We start by opening the file and storing the each line of digits in a list. We create a variable, *pi_string*  to hold the digits of *pi*. We then create a loop that adds each line of digits to *pi_string* and removes the newline character from each line. We finally print this string and also show how long the string is:

``` markdown
3.1415926535 8979323846 2643383279
36
```

The variable *pi_string* contains the whitespace that was on the left side of the digits in each line, but we can get rid by using `strip()` instead of `rstrip()`:

``` python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

Now we have a string containing *pi* to 30 decimal places. The string is 32 characters long because it also includes the leading 3 and a decimal point:

``` markdown
3.141592653589793238462643383279
32
```

***When Python reads from a text file, it interprets all text in the file as a string. To read a number and work with numerically, convert it to an integer using `int()` function or convert it to a float using the `float()` function.***

### Large Files: One Million Digits

If we start with a text file that contains *pi* to 1,000,000 decimal places instead of just 30, we can create a single string containing all these digits.

``` python
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file _object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
```

The output shows that we do have a string containing *pi* to 1,000,000 decimal places:

``` markdown
3.14159265358979323846264338327950288419716939937510...
1000002
```

Python has no limit to how much data we can work with as much we have enough system memory to handle it.

### Is Your Birthday Contained in Pi

We can use the program from previous examples to determine if someones' birthday appears anywhere in the first million digits of *pi*. We can do this by expressing each birthday as a string of digits and seeing if that string appears anywhere in *pi_string*:

``` python
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file _object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

We prompt for the user's birthday, and then we check if that string is in *pi_string*.

``` markdown
Enter your birthday, in the form mmddyy: **120372**
Your birthday appears in the first million digits of pi!
```

We can analyze contents from any file in about any way imagined.

---

### TRY IT YOURSELF: Reading from a File

**10-1. Learning Python**: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by stor- ing the lines in a list and then working with them outside the with block.

**10-2. Learning C**: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:

``` python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

---

## Writing to a File

One of the simplest ways to save data is to write to a file. The output is still available after the terminal closes when writing to a text file.

### Writing to an Empty File

To write text to a file, we need to call `open()` with a second argument telling Python to write to the file. See how this works by writing a simple message and store it in a file instead of printing it to the screen:

``` python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming!")

```

The call to `open()` has two arguments. The first is the file we want to open, and the second argument, 'w', tells Python that we want to open the file in ***write mode***. We can open a file in ***read mode ('r'), write mode ('w'), append mode ('a')***, or a mode that allows to read and write to a file ('r+'). Python opens files in read-only mode by default if the argument mode is blank.

The `open()` function automatically created the file if it doesn't already exist. Be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.

We use the `write()` method on the file object to write a string to the file. This program has no terminal output, but the file *programming.txt* will see one line:

``` markdown
I love programming.
```

This file behaves like any other file. We can open, copy, and paste new text in it.

***Python can only write strings to a text file. To store numerical data in a text file, we have to convert the data to string format first using the `str()` function.***

### Writing Multiple Lines

The `write()` function doesn't add any newlines to the text. If we write more than one line without including newline characters, the file may not look the way we want it to:

``` python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```

If we open *programming.txt*, we see two lines squished together:

``` markdown
I love programming. I love creating new games.
```

Including newlines in calls to `write()` makes each string appear on its own line:

``` python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

Now the output is on separate lines:

``` markdown
I love programming.
I love creating new games.
```

We can also use spaces, tab characters, and blank lines to format output similar to terminal-based output.

### Appending to a File

If we want to add content to a file instead of writing over a existing content, we can open the file in ***append mode***. Python doesn't erase the contents of the file before retuning the file object when opening it. Any lines written to the file will be added at the end of the file. If the file doesn't exist yet, Python will create an empty file.

Modify *write_message.py* by adding new reasons we love programming to the existing file *programming.txt*:

``` python
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large data sets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

We use the 'a' argument to open the file for appending rather than writing over the existing file. We write two new lines, which are added to *programming.txt*:

``` markdown
I love programming.
I love creating new games.
I also love finding meaning in large data sets.
I love creating apps that can run in a browser.
```

We combine the original contents of the file with our new lines of content we added.

---

### TRY IT YOURSELF: Appending to a File

**10-3. Guest**: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

**10-4. Guest Book**: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

**10-5. Programming Poll**: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

---

## Exceptions

Python uses special objects called ***exceptions*** to manage errors that arise during a program's execution. Whenever an error occurs that makes Python unsure what to do, it creates an exception object. If we handle the exception, the program will continue running. If not, the program will halt and show a ***traceback*** error.

Exceptions are handled with ***try-except*** blocks. A ***try-except*** block asks Python to do something, but it also tells it what to do when an exception is raised. Instead of tracebacks, which can be confusing for users to understand, users will see a friendly error message that we write.

### Handling the *ZeroDivisionError* Exception

Let's handle an exception to divide a number by zero in Python:

division_calculator.py

``` python
print(5/0)
```

Python is unable to do this, so we get a traceback:

``` python
Traceback (most recent call last):
    File "division_calculator.py", line 1, in <module>
        print(5/0)
ZeroDivisionError: division by zero
```

In the traceback error, *ZeroDivisionError*, is an exception object Python created when it runs to an error and stops the program. Next time, we can use this information and properly handle the exception to modify our program if it happens again.

### Using ***try-except*** Blocks

Here is an example of a ***try-except*** block for handling the *ZeroDivisionError* exception:

``` python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

We try to print the line that is causing the error inside the `try` block. If the code in the try block works, Python skips over the `except` block. If the code in the `try` block causes an error, Python runs the `except` block that matches the exception raised.

In this example, the code produces a *ZeroDivisionError*, so Python looks for the `except` block on how to respond instead of a traceback:

``` markdown
You can't divide by zero!
```

### Using Exceptions to Prevent Crashes

Handling errors correctly is important when a program has more work to do after an error occurs. If the program manages to invalid input, it can prompt for more valid input instead of crashing the program.

Let's create a simple calculator does only division:

``` python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```

This program prompts the user for two numbers. We divide two numbers to get an answer. This program does nothing to handle errors, so asking to divide by zero causes it to crash.

It is bad the program crashed, but also a bad idea to let users see traceback errors. A nontechnical user will be confused, and a malicious user could exploit the flaw in code.

### The else Block

We can make this program more error resistant by wrapping the line that might produce errors in a `try-except` block. When the code in the `try` successfully runs, it goes to the `else` block:

``` python
--snip--

while True:
    --snip--
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

We tell Python on how to respond in case the division operation runs to an error with the *ZeroDivsionError*, or what to do when the code is successful with the `else` block.

``` markdown
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: **5**
Second number: **0**
You can't divide by 0!

First number: **5**
Second number: **2**
2.5

First number: q
```

In a `try-except-else` block: Python attempts to run the code in the `try` block. The only code that should go inside the try block is code that might cause an exception. If it was successful, the code should be inside the `else` block. The `except` block tells Python what to do in case an exception arises inside the try block.

### Handling the FileNotFoundError Exception

A common issues when working with files is handling missing files. The file could be in a different location, filename misspelled, or may not exist. The `try-except` block can handle errors in these situations.

Let's try to read a file that does not exist. The following program tries to read the contents of *Alice in Wonderland*, but no saved file as *alice.txt* in the same directory as *alice*.*py*:

``` python
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
```

The **encoding** argument is needed when system's default encoding doesn't match the encoding of the file that's being read.

Python can't read from a missing file, so it raises an exception:

``` python
Traceback (most recent call last):
    File "alice.py", line 3, in <module>
        with open(filename, encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

The last line of the traceback indicates a *FileNotFoundError*: the exception Python creates when it can't the file it is trying to open.

In this example, the `open()` function produces the error, so we can handle it using the `try` block.

``` python
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
```

The `try` block produces a *FileNotFoundError*, so Python looks for the `except` block that matches the error and prints the approriate message instead of a traceback:

``` markdown
Sorry, the file alice.txt does not exist.
```

The program has nothing to do if the file doesn't exist, but we can build on this example and see how exception handling is useful when working with multiple files.

### Analyzing Text

We can analyze text files containing entire books. We can pull in the text of *Alice in Wonderland* and try to count the number of words in the text. We use the string method `split()`, which can build a list of words from a string.

``` python
title = "Alice in Wonderland"
title.split()
```

The `split()` method separates a string into parts wherever it finds a space and stores all the parts of the string in a list.

``` markdown
['Alice', 'in', 'Wonderland']
```

The result is a list of words from a string, although some punctuation may also appear with some of the words. To count the number of words in *Alice in Wonderland*, we use `split()` on the entire text. Then we count the items in the list to get an approximate word count in the text:

``` python
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
```

The string *contents* stores the entire text of *Alice in Wonderland* as one long string, and use the `split()` method to produce a list of all words in the book. Then `len()` is used on the list to examine its length to retrieve an approximate of number of words. The code placed in the `else` block only works if the code in the `try` block was successfully executed:

``` markdown
The file alice.txt has about 29465 words.
```

The count is a little high because extra information is provided by the publisher in the text file used here.

### Working with Multiple Files

Let's add more books to analyze. Before we do, we can move a chunk of the program to a function called *count_words()*. It will be easier to run the analysis for multiple books:

word_count.py

``` python
def count_words(filename):
    """Count the approximate words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)
```

Most of the code is unchanged. We simply moved the body into *count_words()* function.

Now we can write a simple loop to count the word in any text we want to analyze. We do this by storing the names of the files we want to analyze in a list, and then call *count_words()* for each file in the list. The texts used in this section comes from Project Gutenberg (<http://www.gutenberg.org/>).

``` python
def count_words(filename):
    --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

The missing *siddhartha.txt* is to see how well our program handles a missing file and has no effect on the rest of the program.

``` markdown
The file alice.txt has about 29465 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

The `try-except` block in this example is significant because it allows our program to continue analyzing the texts without issue despite the missing file. It would never analyze *Moby Dick* or *Little Women*.

### Failing Silently

In the previous example, we informed our users that one of the files was unavailable. But we don't need to report every exception we catch. We can allow the program to fail silently when an exception occurs and continue as if nothing happened.

To make a program fail silently, write a `try` block as usual, but explicitly tell Python to do nothing in the `except` block. Python has a `pass` statement that tells it do nothing in a block:

``` python
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

The only difference between the previous example is the `pass` statement inside the `except` block. When it runs, nothing happens and there's no output in response to the error that was raised:

``` markdown
The file alice.txt has about 29465 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

The `pass` statement acts as a placeholder. It is a reminder choosing to do nothing at a specific point in a program's execution and might use later. For example, in this program we might decide to write any missing filenames to a file called *missing_files.txt*. Our users wouldn't see this file, but we'd be able to read the file and deal with any missing texts.

### Deciding Which Errors to Report

Python's error handling capabilities gives us control over how much to share with users when things go wrong. It all depends on the usability of the program and the purpose of it. There is always a possibility of an exception being raised from something external, such as user input, the existence of a file, or the availability of a network connection. More experience will help to know where to include exception handling blocks in programs and how much to report to users about errors that arise.

---

### TRY IT YOURSELF: Exceptions

**10-6. Addition**: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

**10-7. Addition Calculator**: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

**10-8. Cats and Dogs**: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a `try-except` block to catch the *FileNotFound* error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

**10-9. Silent Cats and Dogs**: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

**10-10. Common Words**: Visit Project Gutenberg (<https://gutenberg.org/>) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:

``` python
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
```

Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.

Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.

---

