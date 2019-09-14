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
