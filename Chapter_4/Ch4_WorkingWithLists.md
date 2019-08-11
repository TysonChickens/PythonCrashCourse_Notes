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

``` python
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

