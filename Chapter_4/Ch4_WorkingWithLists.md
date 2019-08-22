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

## Making Numerical Lists

Many reasons exist to store a set of numbers. For example, it is sometimes necessary to keep track of the position of each character in a game, and to keep track of a player's high scores as well. In data visualizations, you will almost always work with sets of numbers, such as temperatures, distances, population sizes, or latitude and longitude values, among other types of numerical sets.

Lists are ideal for storing sets of numbers, and Python provides a variety of tools to help work efficiently.

## Using the range() Function

Python's `range()` function makes it easy to generate a series of numbers like this:

``` python
for value in range(1, 5):
    print(value)
```

Although this code looks like it should print the numbers from 1 to 5, it doesn't print the number 5:

``` markdown
1
2
3
4
```

In this example, it only prints numbers 1 through 4. This is a result of the off-by-one behavior often seen in programming languages. The `range()` function starts counting at the first value, and it stops when it reaches the second value provided. The output will never contain the end value or the second value given.

To print the numbers from 1 to 5, a `range(1, 6)` is used. This time the output start at 1 and ends at 5:

``` markdown
1
2
3
4
5
```

If the output is different than expected, try adjusting the end value by 1. The `range()` argument can also pass one argument, and it will start the sequence of numbers at 0. For example, `range(6)` would return the numbers from 0 to 5.

## Using range() to Make a List of Numbers

To make a list of numbers, convert the results of `range()` directly into a list using the `list()` function. The `list()` around a call to the `range()` function will output a list of numbers.

``` python
numbers = list(range(1, 6))
print(numbers)
```

This is the result:

``` markdown
[1, 2, 3, 4, 5]
```

We can also use the `range()` function to tell Python to skip numbers in a given range. If a third argument to `range()` is given, Python uses that value as a step size when generating numbers.

For example, here's how to list the even numbers between 1 and 10.

``` python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```

In this example, the `range()` function starts with a value of 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value of 11.

``` markdown
[2, 4, 6, 8, 10]
```

Almost any set of numbers can be created using the `range()` function. For example, consider how to make a list of the first 10 square numbers. In Python, two asterisks (**) represent exponents. Here is how to put the first 10 square numbers into a list:

``` python
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
```

First, we start with an empty list called *squares*. Python loops through each value from 1 to 10 using the `range()` function. Inside the loop, the current value is raised to the second power and assigned to the variable *square*. Next, each new value of *square* is appended to the empty list of *squares*. Finally, when the loop has finished running, the list of *squares* is printed:

``` markdown
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

For more concise code, omit the temporary variable *square* and append each new value directly to the list:

``` python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
```

The code does the same work as the previous example. Sometimes using a temporary variable makes code easier to read; other times it makes the code unnecessarily long. Focus first on writing code that is easy to understand and works properly. Then look for more efficient approaches when review over code.

## Simple Statistics with a List of Numbers

A few Python functions are helpful when working with lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers:

``` python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

## List Comprehension

Earlier, we generated the list *squares* using three or four lines of code. A *list comprehension* allows to generate the same list in just one line of code. A *list comprehension* combines a `for` loop and the creation of new elements into one line, and automatically appends each new element.

The following example builds the same list of square numbers but uses a list comprehension:

``` python
squares = [value**2 for value in range(1, 11)]
print(squares)
```

The open set of square brackets and define the expression for the values to store in the new list. In this example, the expression is *value**2*, which raises the value to the second power. Then, write a `for` loop to generate the numbers to feed into the expression and close the square brackets. In this case, the `for` loop is `for value in range(1, 11)`, which feeds the values 1 through 10 into the expression *value**2*. Notice there is no colon used at the end of the `for` statement.

The result is:

`[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`

---

### TRY IT YOURSELF: Making Numerical Lists

* **4-3. Counting to Twenty**: Use a for loop to print the numbers from 1 to 20, inclusive.

* **4-4. One Million**: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl -C or by closing the output window.)

* **4-5. Summing a Million**: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

* **4-6. Odd Numbers**: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

* **4-7. Threes**: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

* **4-8. Cubes**: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

* **4-9. Cube Comprehension**: Use a list comprehension to generate a list of the first 10 cubes.

---

## Working with Part of a List

In chapter 3, we learned how to access single elements in a list, and will now learn how to work through all the elemtents in a list. In Python, there is something called a *slice* to work with a specific group of items in a list.

## Slicing a List

To make a slice, specify the index of the first and last elements to work with similar to the `range()` function. When slicing, Python stops one item before the second index specified. To output the first three elements in a list, indices 0 through 3 would return elements 0, 1, and 2.

The following example involves a list of players on a team:

``` python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

The code prints a slice of this list, which includes just the first three players. The output retains the structure of the list and includes the first three players in the list:

``` markdown
['charles', 'martina', 'michael']
```

Any subset of a list can be generated. For example, the second, third, and fourth items in a list can be extracted with a start slice at index 1 and end at index 4:

``` python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```

This time the slice starts with *martina* and ends with *florence*:


`['martina', 'michael', 'florence']`

If the first index is omitted, Python automatically starts the slice at the beginning of the list:

``` python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```

Without a start index, Python starts at the beginning of the list:

`['charles', 'martina', 'michael', 'florence']`

A similar syntax works when wanting to slice that includes the end of a list. For example, all items from the third item through the last item starts with an index 2 and omit the second index:

``` python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
```

Python returns all items from the third item through the end of the list:

`['michael', 'florence', 'eli']`

This syntax allows to output all of the elements from any point in a list regardless of the length of the list. Recall that a negative index returns an element a certain distance from the end of a list; therefore, can output any slice from the end of a list. For example, to output the last three players on the roster, slice players[-3]:

``` python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```

This prints the names of the last three palyers and would continue to work as the list of players change in size.

***When slicing, a third value can be included in the brackets. If a third value is included, this tells Python how many items to skip between items in the specified range.***

## Looping Through a Slice

Use a slice in a `for` loop if want to loop through a subset of the elements in a list. In the next example, we loop through the first players and print their names as part of a simple roster:

``` python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())
```

Instead of looping through the entire list of players, Python loops through the only the first three names:

``` markdown
Here are the first three players on my team:
Charles
Martina
Michael
```

Slices are very useful in a number of situations. For instance, when creating a game, adding a player's final score to a list every time that player finishes playing. Then retrive a top a player's top three scores by sorting the list in decreasing order and taking a slice that includes just the first three scores. When working with data, the use of slices to process data in chunks of specific size to display appropriate amount of information.

## Copying a List

Often, starting with an existing list and making an entirely new list based on the first one is useful in situations.

To copy a list, make a slice that includes the entire original list by omitting the first index and the second index (`[:]`). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

For example, imagine we have a list of our favorite foods and want to make a separate list of foods that a friend likes. This friend likes everything in our list so far, so we can create their list by copying ours:

``` python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

We make a copy of *my_foods* list to make a new list called *friend_foods*. When we print each list, they both contain the same foods:

``` markdown
My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```

If we assign *friend_foods* equal to *my_foods*, both variables will point to the same list. As a result, any changes made to *my_foods* will also appear in *friend_foods*.

***When trying to copy a list, slice the list.***

---

### TRY IT YOURSELF: Copying a List

* **4-10. Slices**: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

  * Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
  * Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
  * Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

* **4-11. My Pizzas, Your Pizzas**: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

  * Add a new pizza to the original list.
  * Add a different pizza to the list friend_pizzas .
  * Prove that you have two separate lists. *Print the message My favorite pizzas are:*, and then use a for loop to print the first list. Print the message *My friend’s favorite pizzas are:*, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

* **4-12. More Loops**: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

---
