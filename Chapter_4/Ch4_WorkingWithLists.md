# Python Crash Course Chapter 4: Working With Lists

## Looping Through an Entire List

Looping allows to take the same action, or set of actions, with every item in a list regardless of how long the list is. This will be useful when performing the same statistical operation on every element in a list of numbers. Or display each headline from a list of articles on a website. When you want to perform the same action with every item in a list, you use can Python's `for` loop.

We have a list of magicians' names, and we want to print out each name in the list. We could retrieve each name individually, but it would be repetitive to do with a long list of names. For example, use a `for` loop to print out each magician's name in a list:

``` python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

Inside the `for` loop, we tell Python to pull a name from the list of *magicians*, and associate it with the variable *magician*. Lastly, print the name just assigned to *magician*. Python then repeats each name once in the list. The output is a simple print of each name in the list:

``` python
alice
david
carolina
```

Python prints the current value of *magician* and repeats the entire loop until the last value in the list. When using loops, keep in mind that the set of steps is repeated once for each item in the list, no matter how many items are in the list. If there is a million items in the list, Python repeats these steps a million times - and usually very quickly.

Keep in mind that any temporary variable name that will be associated with each value in the list can be used when writing `for` loops. However, it is helpful to choose a meaningful name that represents a single item from the list. For example, here's a good way to start a `for` loop for a list of cats, a list of dogs, and a general list of items:

``` python
for cat in cats:
for dog in dogs:
for item in list_of_items:
```

These naming conventions can help follow the action being done on each item within a `for` loop. Using singular and plural names can help identify whether a section of code is working with a single element from the list or the entire list.

## Doing More Work Within a for Loop

You can do just about anything with each item in a `for` loop. Let's build on the previous example by printing a message to each magician, telling them that they performed a great trick:

``` python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
```

The only difference in this code is where we compose a message to each magician, starting with that magician's name. The output shows a personalized message in a `for` loop each magician in the list starting from the first value of *alice* until the last value of *carolina*.

``` markdown
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

There can be many lines of code inside the `for` loop. Every indented line following the line for *magician in magicians* is considered **inside the loop**, and each indented line is executed once for each value in the list. Therefore, we can add as many lines to do work with each value in the list.

## Doing Something After a for Loop

What happens once a `for` loop has finishing executing? Usually, it is best to summarize the block of output or move on to other work that the progam must accomplish.

Any lines of code after the `for` loop that are not indented are executed once without repetition. Let's write a thank you to the group of magicians as a whole, thanking them for putting on an excellent show. To display this group message after all of the individual messages have been printed, we place the thank y ou message after the `for` loop without indentation:

``` python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

The first two calls to `print()` are repeated once for each magician in the list. However, because the last `print()` is not indented, it is only printed once:

``` markdown
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
David, that was a great trick!
I can't wait to see your next trick, David.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
Thank you, everyone. That was a great magic show!
```

When processing data using a `for` loop, this is a good way to summarize an operation that was performed on an entire data set. For example, a `for` loop might be used to initialize a game by running through a list of characters and displaying each character on the screen. After all the characters have been drawn to the screen, some additional code may be added that displays a *Play Now* button.

## Avoiding Indentation Errors

Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. In the previous examples, the lines that printed messages to individual magicians were part of the `for` lopp because they were indented. Python's use of indentation makes code very easy to read. It uses whitespace to force to write neatly formatted code with a clear visual structure. The indentation levels help gain a general sense of the overall program's organization.

When code written relies on proper indentation, we need to watch for a few common ***indentation errors***. For example, people sometimes indent lines of code that don't need to be indented or forget to indent lines that need to be indented. Here are some examples of these errors to avoid them in the future and correct them when they do appear in programs.

## Forgetting to Indent

Always indent the line after the `for` statement in a loop. If you forget, Python will remind you:

``` python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```

The call to `print()` should be indented, but it's not. When Python expects an indented block and doesn't find one, it lets you know which line it had a problem with.

``` python
File "magicians.py", line 3
print(magician)
^
IndentationError: expected an indented block
```

This can usually be resolved by indenting the line or lines immediately after the `for` statement.

## Forgetting to Indent Additional Lines

Sometimes a loop will run without any erros but won't produce the expected result. This can happen when trying to do several taks in a loop and forget to indent some of its lines.

This is what happens when we forget to indent the second line in the loop that tells each magician we're looking forward to their next trick:

``` python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

The last line with the call `print()` is supposed to be indented, but Python finds at least one indented line after the `for` statement, and does not report an error. As a result, the first `print()` call is executed once for each name in the list because it is indented as expected. The second `print()` call is not indented, so it is executed only once after the loop has finished running. Since the final value associated with magician is *carolina*, she is the only one who receives the "looking forward to the next trick" message:

``` markdown
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

This is a *logical error*. The syntax is valid Python code, but the code does not produce the desired result because a problem occurs in its logic.

## Indenting Unnecessarily

If you accidentally indent a line that doesn't need to be indented, Python will inform you about the unexpected indent:

``` python
message = "Hello Python World!"
    print(message)
```

There is no need to indent the `print()` call, because it is not part of a loop. Therefore, Python reports an error:

`IndentationError: unexpected indent`

Avoid indentation errors by indenting only when there is a specific reason to do so. At this point, the only lines to indent are actions to be repeated for each item in a `for` loop.

## Forgetting the Colon

The colon at the end of a `for` statement tells Python to interpret the next line as the start of a loop. If the colon is missing, there will be a syntax error because Python does not understand.

---

### TRY IT YOURSELF: Looping Through Lists

* **4-1. Pizzas**: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

  * Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like *I like pepperoni pizza*.
  * Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as *I really love pizza!*

* **4-2. Animals**: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
  
  * Modify your program to print a statement about each animal, such as *A dog would make a great pet*.
  * Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!

---
