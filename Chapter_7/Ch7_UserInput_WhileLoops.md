# Python Crash Course Chapter 7: User Input and While Loops

Most programs are written to solve an end user's problem. First, we need to get some information from the user. For example, let's say someone wants to find out whether they're old enough to vote. We need to write a program to answer this question, and know the user's age before provide an answer. The program will need to ask the user to enter, or *input*, their age; the program can compare it to the voting age to determine if the user is old enough and then report the result.

We will learn how to accept user input so the program can work with it. When the program needs a name, it will prompt the user for a name. When a program needs a list of names, it will prompt the user for a series of names by utilizing the `input()` function.

Also, keep programs running as long as users want them to, so they can enter as much information as they need to. Python's `while` loop will be used to keep programs running as long as certain conditions remain true.

The ability to work with user input and the ability to control how long programs run will alow us to write fully interactive programs.

## How the input() Function Works

The `input()` function pauses the program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to work with.

For example, the following program asks the user to enter some text, then displays that message back to the user:

``` python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

The `input()` function takes one argument: the *prompt*, or instructions, that we want to display to the user so they know what to do. In this case, Python runs the first line, the user sees the prompt: *Tell me something, and I will repeat it back to you:*. The program waits while the user enters their response and continues after the user presses ENTER. The response is assigned to the variable *message*, then print(message) displays the input back to the user:

``` markdown
Tell me something, and I will repeat it back to you: **Hello everyone!**

Hello everyone!
```

### Writing Clear Prompts

Each time the `input()` function is used, it should include a clear, easy-to-follow prompt that tells the user exactly what kind of information we are looking for. Any statement that tells the user what to enter should work. For example:

``` python
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```

Add a space at the end of prompts (after the colon) to separate the prompt from the user's response and to make it clear to the user where to enter their text.

Sometimes, a prompt might be longer than one line. For example, we might want to tell the user why we're asking for certain input. We can assign a prompt to a variable and pass that variable to the `input()` function. This allows to build our prompt over several lines, when write a clean `input()` statement.

``` python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
```

This example shows one way to build a multi-line string. The first line assigns the first part of the message to the variable *prompt*. In the second line, the operator += takes the string that was assigned to *prompt* and adds the new string onto the end.

The prompt now spans two lines with space after the question mark for clarity:

``` markdown
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```