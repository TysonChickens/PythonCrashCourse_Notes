# Python Crash Course Chapter 8: Functions

Named blocks of code that are designed to do one specific job are called ***functions***. We can call a function to perform a particular task that we defined inside a function. Using functions makes programs easier to write, read, test, and fix because functions can be dedicated to handling a specific task. We don't have to type all the code for the same task over again multiple times throughout a program.

## Defining a Function

Here is a simple named *greet_user* that prints a greeting:

``` python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

This example shows the simplest structure of a function. We use the keyword on the first line, `def`, to inform Python that we are defining a function. This is the ***function definition***, which tells Python the name of the function, and if applicable, what kind of information the function needs to do its job. In this case, the parentheses are empty because it needs no information to do its job. Finally, the definition ends in a colon.

Any indented lines that follow *def greet_user():* make up the ***body*** of the function. The text in triple quotes is called a ***docstring***, which describes what the function does.

The only code in the function is the line *print("Hello!")*. To use this function, we call it. A ***function call*** tells Python to execute the code in the function. To ***call*** a function, write the name of the function, followed by any necessary information in parentheses. Since no information is needed here, calling our function is simple as entering *greet_user()*.

``` markdown
Hello!
```
