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

### Passing Information to a Function

The function *greet_user()* can tell the user `Hello!` by name with slight modification. For the function to do this, add *username* in the parentheses of the function's definition. Adding it inside the parentheses of the function allows to accept any value specified. The function now expects a provided value for *username* each time it is called. When we call *greet_user()*, pass it a name, such as 'jesse', inside the parentheses:

``` python
def greet_user(username):
"""Display a simple greeting."""
print(f"Hello, {username.title()}!")

greet_user('jesse')
```

The function accepts the name and displays the greeting for that name:

``` markdown
Hello, Jesse!
```

We can call the function as often we want and pass it any name to produce a predictable output every time.

### Arguments and Parameters

Earlier, we defined *greet_user()* to require a value for the variable *username*. Once we called the function and gave it the information (a person's name), it printed the right greeting.

The variable *username* in the definition of *greet_user()* is an example of a ***parameter***, a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function work with in the parentheses. In this case the argument 'jesse' was passed to the function *greet_user()*, and the value was assigned to the parameter *username*.

---

### TRY IT YOURSELF: Defining a Function

**8-1. Message**: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

**8-2. Favorite Book**: Write a function called favorite_book() that accepts one parameter,title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

---
