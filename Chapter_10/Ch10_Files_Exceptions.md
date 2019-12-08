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

### TRY IT YOURSELF: Learning Python

**10-1. Learning Python**: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by stor- ing the lines in a list and then working with them outside the with block.

**10-2. Learning C**: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:

``` python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

---

