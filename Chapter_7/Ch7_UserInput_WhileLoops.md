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

### Using int() to Accept Numerical Input

Python interprets everything the user enters as a string when we use the `input()` function.

``` python
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

The user enters the number 21, when we ask Python for value of age, it returns '21', the string representation of the numerical value entered. We know Python interpreted the input as a string because the number is now enclosed in quotes. If we want try to use the input as a number, we will get an error:

``` python
>>> age = input("How old are you? ")
How old are you? 21
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
```

When trying to do a numerical comparison, Python produces an error because it can't compare a string to an integer.

This issue can be resolved with the `int()` function, which tells Python to treat the input as a numerical value. The `int()`function converts a string representation of a number to a numerical representation:

``` python
>>> age input("How old are you? ")
How old are you? 21
>>> age = int(age)
>>> age >= 18
True
```

Now, Python can run the conditional test since the value is converted to a numerical value. We compare age to see if greater than or equal to 18. This test evaluates to True.

We can use the `int()` function in a program that determines whether people are tall enough to ride a roller coaster:

``` python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

This program can compare *height* to *48* because *height = int(height)* converts the input value to a numerical representation before the comparison is made.

When using numerical input to do calculations and comparisons, be sure to convert the input value to a numerical first.

### The Modulo Operator

A useful tool for working with numerical information is the *modulo operator (%)*, which divides one number by another number and returns the remainder:

``` python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

The modulo operator tells us what the remainder is of a number being divided.

When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0. This is useful to determine if a number is even or odd:

``` python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
  print(f"\nThe number {number} is even.")
else:
  print(f"\nThe number {number} is odd.")
```

Even numbers are always divisible by two, so if the modulo of a number and two is zero, the number is even. Otherwise, it's odd.

``` markdown
Enter a number, and I'll tell you if it's even or odd: 42

The number 42 is even.
```

---

### TRY IT YOURSELF: Input() Function

**7-1. Rental Car**: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

**7-2. Restaurant Seating**: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

**7-3. Multiples of Ten**: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

---

## Introducing while Loops

The `for` loop takes a collection of items and executes a block once for each item in the the collection. In contrast, the `while` loop runs as long as, or *while*, a certain condition is true.

### The while Loop in Action

A `while` loop can be used to count up through a series of numbers. For example, this loop counts from 1 to 5:

``` python
current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1
```

Python repeats the loop as long as the condition *current_number <= 5* is true. Because 1 is less than 5, Python prints 1 and then adds 1 until the value of *current_number* is greater than 5, and the loops stops running:

``` markdown
1
2
3
4
5
```

The programs we use every day most likely contain `while` loops. For example, a game needs a `while` loop to keep running as long to keep playing, and so it can stop running as soon we ask to quit out. Programs would not be fun to use if they stopped running before we told them to or kept running after we wanted to quit.

### Letting the User Choose When to Quit

We can define a *quit value* and then keep the program running as long as the user has not entered the quit value:

``` python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "


message = ""
while message != 'quit':
  message = input(prompt)
  print(message)
```

Python will keep running the loop as long as the value of *message* is not 'quit'. The first time through the loop, *message* is a just an empty string so Python compare the value. Python displays the prompt and waits for the user to enter their input. As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. When the user finally enters 'quit', Python stops executed the `while` loop and the program ends:

``` markdown
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit

```

This program works well, except that it prints the word 'quit' as if it were an actual message. A simple `if` test fixes this:

``` python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "


message = ""
while message != 'quit':
  message = input(prompt)
  print(message)

  if message != 'quit':
    print(message)
```

Now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value:

``` markdown
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### Using a Flag

A program that should run only as long as many conditions are true, we can define one variable that determines whether or not the entire program is active. A ***flag*** acts as a signal to the program. We can write programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. The flag we will be called *active* (can be called anything), will monitor whether or not the program should continue running:

``` python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message)
```

The variable *active* is set to `True` so the program starts in an active state. This makes the while statement simpler because no comparison is made in the statement itself. As long as the *active* variable remains `True`, the loop will continue running. In the `if` statement, we check the value of *message* once the user enters their input. If the user enters 'quit', we set *active* to `False`, and the `while` loop stops.

This program has the same output as the previous example where we placed the conditional test directly in the `while` statement. But now that we have a flag to indicate whether the overall program is an active state, it would be easy to add more tests (such as `elif` statements) for events that should cause *active* to become `False`. This is useful in complicated programs like games in which there may be many events that should each make the program stop running. When any of these events causes the *active* flag to become `False`, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play again.

### Using break to Exit a Loop

To exit a `while` loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the ***break*** statement. The ***break*** statement directs the flow of the program; can use it to control which lines of code are executed and which are ignored.

For example, consider a program that asks the user about places they've visited. We can stop the `while` loop in this program by calling `break` as soon as the user enters the 'quit' value:

``` python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' to end the program. "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I would love to go to {city.title()}!")
```

A loop that starts with `while True` will run forever unless it reaches a `break` statement. The loop will continue asking the user to enter the names of cities until they enter 'quit'.

``` markdown
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

***The `break` statement can be used in any of Python's loops. For example, `break` can be used to quit a `for` loop that's working through a list or a dictionary.***

### Using continue in a Loop

Rather than breaking out of a loop entirely without executing the rest of its code, we can use the `continue` statement to return to the beginning of the loop based on the result of a conditional test. For example, consider a loop that ocunts from 1 to 10 but prints only the odd numbers in that range:

``` python
current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:
    continue

  print(current_number)
```

The `continue` statement tells Python to ignore the rest of the loop and return to the beginning. If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number:

``` markdown
1
3
5
7
9
```

### Avoiding Infinite Loops

Every `while` loops needs a way to stop running so it won't continue to run forever. For example, this counting loop should count from 1 to 5:

``` python
x = 1
while x <= 5:
  print(x)
  x += 1
```

If we accidentally omit the line `x += 1`, the loop will run forever:

``` python
# This loop runs forever
x = 1
while x <= 5:
  print(x)
```

The value of *x* will start 1 but never change:

``` markdown
1
1
1
1
--snip--
```

If a program gets in an infinite loop, press *CTRL + C* or close the terminal window displaying the program's output. To avoid writing infinite loops, test every `while` loop to make sure the loop's condition can be `False` or reach a `break` statement.

---

### TRY IT YOURSELF: while Loops

**7-4. Pizza Toppings**: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

**7-5. Movie Tickets**: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

**7-6. Three Exits**: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:

* Use a conditional test in the while statement to stop the loop.
* Use an active variable to control how long the loop runs.
* Use a break statement to exit the loop when the user enters a 'quit' value.

**7-7. Infinity**: Write a loop that never ends, and run it. (To end the loop, press Ctrl -C or close the window displaying the output.)

---
