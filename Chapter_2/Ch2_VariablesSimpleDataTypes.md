# Python Crash Course Chapter 2: Variables and Simple Data Types

``` python
message = "Hello Python world!"
print(message)
```

When we run this program, the output should return "`Hello Python world!`".

Here, we have added a *variable* named **message**. Every variable is connected to a *value*, which is the information associated with that variable. The value is the "Hello Python world!" text for our variable.

Let's expand on *hello_world.py* to print a second message. Add two new lines of code:

``` python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

Now the two lines of output:

``` python
Hello Python world!
Hello Python Crash Course world!
```

You can change the value of a variable in your program at any time, and Python will always keep track of its current value.

## Naming and Using Variables

When using variables in Python, there are a few rules and guidelines to follow. Breaking some of these rules will cause errors; other guidelines just help you write code that's easier to read and understand. Here are the rules to keep in mind:

* Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable *message_1* but not *1_message*.

* Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, *greeting_message* works, but *greeting message* will cause errors.

* Avoid using Python keywords and function names as variable names. Python has words reserved for particular programmatic purpose, such as the word `print`.
  * Here is a list:
  
    ![Python Functions](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/master/PythonKeywordFunctions.png)

* Variable names should be short but descriptive. For example, *name* is better than *n, student_name* is better than *s_n*, and *name_length* is better than *length_of_persons_name*.

***Python variables at this point should be lowercase to reduce the amount of errors with uppercase letters. Variable name with uppercase letters have special meanings that are discussed in later chapters.***

## Avoiding Name Errors When Using Variables

Every programmer makes mistakes, and most make mistakes every day. Here is a simple error to make and learn how to fix it. The following code has a misspelled word *mesage* inside *print()*.

``` python
message = "Hello Python Crash Course reader!"
print(mesage)
```

When an error occurs, the Python interpreter does its best to help you figure out where the problem is. The interpreter returns a *traceback* when a program cannot run successfully, and shows a record where the interpreter ran into trouble when trying to execute the code.

``` python
Traceback (most recent call last):
File "hello_world.py", line 2, in <module>
print(mesage)
NameError: name 'mesage' is not defined
```

The output reports an error on line 2 of the file *hello_world.py*. On the last line, it helps us spot the error quickly and tells us what kind of error it found. In this case, it found a *name error* and the variable printed, *mesage*, has not been defined. This means we forgot either forgot to set a variable's value before using it, or we made a spelling mistake when entering the variable's name.

Many programming languages are strict, but they disregard good and bad spelling. As a result, you don't need to consider English spelling and grammar rules when trying to create variable names and writing code. Many programming errors are simple, single-character typos in one line of a program. Many experienced and talented programmers spend hours hunting down these kinds of tiny errors. Fix it, laugh about it, and move on.

---

## Strings

Most programs define and gather some sort of data, and then do something useful with it, it helps to classify different types of data. The first data type we'll look at is string. Strings are simple at first glance, but you can use them in many different ways.

A *string* is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this:

``` python
"This is a string."
'This is also a string.'
```

This flexibility allows you to use quotes and apostrophes within your strings:

``` python
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

## Changing Case in a String with Methods

One of the simplest tasks to do with strings is change the case of the words in a string.

``` python
name = "ada lovelace"
print(name.title())
```

The output should be `Ada Lovelace`. The method `title()` appears after the variable in the `print()` call. A *method* is an action that Python can perform on a piece of data.

The `title()` method changes each word to title case, where each word begins with a capital letter. This is useful because you'll often want to think of a name as a piece of information. For example, we might want a program to recognize the input values of **Ada**, **ADA**, and **ada**, and display all of them as **Ada**.

You can also change a string to all uppercase or all lowercase letters with several other useful methods.

``` python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

This will display the following:

``` python
ADA LOVELACE
ada lovelace
```

The `lower()` method is particularly useful for storing data because you won't want to trust the capitalization that users provide. Therefore, you will have to convert strings to lowercase before storing them.

## Using Variables in Strings

In some situations, you will want to use a variable's value inside a string. For example, you might want two variables to represent a first name and a last name respectively, and then combine those values to display someone's full name:

``` python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

To insert a variable's value into a string, place the letter *f* immediately before the opening quotation mark. Put braces around the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed. These strings are called *f-strings* where *f* stands for *format*, because Python formats the string by replacing the name of any variable in braces with its value. The output from previous code is:

`ada lovelace`

You can do a lot with *f-strings*. For example, you can use f-strings to compose complete messages using the information associated with a variable, as shown here:

``` python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")
```

The full name is used in a sentence that greets the user, and the `title()` method changes the name to title case. The code returns a simple but nicely formatted greeting:

`Hello, Ada Lovelace!`

You can also use f-strings to compose a message, and then assign the entire message to a variable to make the final `print()` call much simpler:

``` python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

message = f"Hello, {full_name.title()}!"
print(message)
```

***F- strings were first introduced in Python 3.6. If you’re using Python 3.5 or earlier,
you’ll need to use the format() method rather than this f syntax. To use format() , list
the variables you want to use in the string inside the parentheses following format .
Each variable is referred to by a set of braces; the braces will be filled by the values
listed in parentheses in the order provided:***

`full_name = "{} {}".format(first_name, last_name)`

## Adding Whitespace to Strings with Tabs or Newlines

In programming, *whitespace* refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it's easier for users to read.

``` python
# To add a tab to your text, use the character combination `\t`:
print("Python")
print("\tPython")

# To add a newline in a string, use the character combination `\n`:
print("Languages:\nPython\nC\nJavascript")

# Combine tabs and newlines in a single string.
print("Languages: \n\tPython\n\tC\n\tJavascript")
```

Newlines and tabs will be useful in the next two chapters when you start to produce many lines of output from just a few lines of code.

## Stripping Whitespace

Extra whitespace can be confusing in programs. `"python"` and `"python "` may look the same, but to a program, they are two different strings. Python detects the extra space in `"python "` and considers it significant unless tell it otherwise.

It is important to think about whitespace, because often to compare two strings to determine whether they are the same. For example, checking people's usernames when log in to a website. Fortunately, Python makes it easy to eliminate extraneous whitespace from data that people enter.

Python can look for extra whitespace on the right and left sides of a string. To remove whitespace from the right end of a string, use the `rstrip()` method.

``` python
favorite_language = "python "
favorite_langauge = favorite_langauge.rstrip()
favorite_language
```

To remove the whitespace from the string, we strip the whitespace from the right side of the string and associate this new value with the original variable to update it. We can also strip whitespace from the left side of a string using `lstrip()` method, or from both sides at once using `strip()`:

``` python
favorite_language = " python "
favorite_langauge.rstrip() # " python"
favorite_language.lstrip() # "python "
favorite_language.strip() # "python"
```

In the real world, these stripping functions are used most often to clean up user input before it's stored in a program.

## Avoiding Syntax Errors with Strings

An error commonly seen is a syntax error. A *syntax error* is where Python doesn't recognize a section of your program as valid Python code. For example, if you use an apostrophe within single quotes, you'll produce an error. This happens because Python interpreters everything between the first single quote and the apostrophe as a string. How to use single and double quotes correctly:

``` python
message = "One of Python's strengths is its diverse community."
print(message)
```

The apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the string correctly:

`One of Python's strengths is its diverse community.`

If you use single quotes, Python can't identify where the string should end:

``` python
message = 'Python's strengths is its diverse community.'
print(message)
```

The following will return with `SyntaxError: invalid syntax`, and the error shows where it occurred right after the second single quote.

Syntax errors are also the least specific kind of error, so they can be difficult and frustrating to identify and correct.

---

### TRY IT YOURSELF: Strings

* **2-3. Personal Message**: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

* **2-4. Name Cases**: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

* **2-5. Famous Quote**: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

* **2-6. Famous Quote 2**: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person . Then compose your message and represent it with a new variable called message . Print your
message.

* **2-7. Stripping Names**: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n" , at least once.
Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

---

## Numbers

Numbers are used often in programming to keep score in games, represent data in visualizations, store information in web applications, and so on. Python treats numbers in several different ways, depending on how they're being used.

## Integers

You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.

``` python
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

Python also supports the order of operations, so you can use multiple operations in one expression. You can also use parentheses to modify the order of operations so Python can evaluate expression in the order you specify. For example:

``` python
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

## Floats

Python calls any number with a decimal point a *float*. This term is used in most programming languages, and it refers that a decimal point can appear at any position in a number. Every programming language must be carefully designed to properly manage decimal numbers so numbers behave appropriately.

In Python, you can use decimals without worrying about how they behave. Simply enter the numbers you want to use, and Python will most likely do what you expect:

``` python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

Sometimes you get an arbitrary number of decimal places in your answer:

``` python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

This happens in all languages and is of little concern. Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally.

## Integers and Floats

When you divide any two numbers, even if they are integers that result in a whole number, the result will always be a float:

`4 / 2 >>> 2.0`

Mixing an integer and a float, you'll get a float value as well:

``` python
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

Python defaults to a float in any operation that uses a float, even if the output is a whole number.

## Underscores in Numbers

When writing long numbers, you can group digits using underscores to make large numbers more readable:

`universe_age = 14_000_000_000`

When printing a number with underscores, Python will print only the digits:

`14000000000` from the universe_age variable.

To Python, 1000 is the same as 1_000, which is the same as 10_00. Python ignores the underscores when storing these kinds of values. This feature only works for integers and floats and only available in Python 3.6 and later.

## Multiple Assignments

You can assign values to more than one variable using just a single line. This can help shorten programs and make them easier to read; a technique used most often when initializing a set of numbers. For example, here is how you can initialize multiple variables:

`x, y, z = 0, 0, 0`

You need to separate the variable names with commas, and do the same with the values. Python will assign each value to its respective positioned variable and match them up correctly.

## Constants

A *constant* is like a variable whose value stays the same throughout the life of a program. Python does not have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:

`MAX_CONNECTIONS = 5000`

Make the name of the variable in all capital letters to treat as a constant in code.

---

### TRY IT YOURSELF: Numbers

* **2-8. Number Eight**: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this: `print(5+3)`

Your output should simply be four lines with the number 8 appearing once on each line.

* **2-9. Favorite Number**: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.

---

## Comments

Comments are extremely useful feature in most programming languages. Everything written so far is Python code. As programs become longer and more complicated, adding notes within programs that describe overall approach to the problem trying to solve. A *comment* allows you to write notes in English within your programs.

In Python the `#` indicates a comment. Anything following a hash mark in code is ignored by the Python interpreter.

``` python
# Say hello to everyone
print("Hello Python people!")
```

Python ignores the first line and executes the second line.

The main reason to write comments is to explain what your code is supposed to do and how you are making it work. When working on a project, it is helpful to understand how all the pieces fit together. When you return to a project after some time away, it is a good reminder for the forgotten details.

Today, most software is written collaboratively, whether by a group of employees at one company or a group of people working together on an open source project. Skilled programmers expect to see comments in code, so it's best to start adding descriptive comments to programs now. Writing clear, concise comments in code is one of the most beneficial habits as a new programmer.

---

### TRY IT YOURSELF: Comments

* **2-10. Adding Comments**: Choose two of the programs you’ve written, and
add at least one comment to each. If you don’t have anything specific to write
because your programs are too simple at this point, just add your name and
the current date at the top of each program file. Then write one sentence
describing what the program does.

---

## Zen of Python

The purpose is to avoid simplicity and aim for simplicity whenever possible. In programming, people solve problems. If you have a choice between a simple and complex solution, and both works, use the simple solution. The code will be easier to main, and it will be easier to build on that code later on. Keep this philosophy of simplicity and clarity in mind.

Run `import this` into Python terminal session and look through the additional principles.

## Summary

What we learned in this chapter:

* Working with and using descriptive variables.

* Solving name errors and syntax errors.

* What strings are and how to manipulate strings using lowercase, uppercase, and title case. Also, using whitespace to organize output, and strip unneeded whitespace from different parts of a string.

* Working with integers and floats and some ways to work with numerical data.

* Explanatory comments to make code easier to understand.
