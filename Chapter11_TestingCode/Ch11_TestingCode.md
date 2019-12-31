# Python Crash Course Chapter 11: Testing Code

What we will learn in this chapter:

* Write test case for functions or classes to prove code responds correctly to all input types it's designed for.
* Test new code being added without breaking program's existing behavior.
* Catch problems before users encounter them.
* Use Python's `unittest` module to test code.

## Testing a Function

name_function.py

We need code to test for a simple function that takes in a first and last name to return a neatly formatted full name:

``` python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

The function *get_formatted_name* combines the first and last name with a space in between to complete a full name, and then capitalizes and return the full name. To make sure it works, the program *names.py* allows users to enter a first and last name to see a formatted full name:

names.py

``` python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```

When running the program, the names generated are correct. Let's try to modify the *get_formatted_name()* function to include middle names without breaking how the function handles the first and last names. We could test our code by running the program every time we modify *get_formatted_name()*, but that would become tedious.

Python provides an efficient way to automate the testing of a function's output. If we automate the testing of *get_formatted_name()*, we can always be confident that the function will work when given the names written tests for.

### Unit Tests and Test Cases

The module `unittest` from the Python standard library provides tools for testing code.

* ***Unit test*** verifies that one specific aspect of a function's behavior is correct.
* ***Test case*** is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations to handle. A good test case considers all the possible kinds of input a function could receive and includes test to represents each of these situations. 
* A test case with ***full coverage*** includes a full range of unit tests covering all the possible ways to use a function.

It is often good enough to write tests for code's critical behaviors and then aim for full coverage only if the project starts to see widespread use.

### A Passing Test

