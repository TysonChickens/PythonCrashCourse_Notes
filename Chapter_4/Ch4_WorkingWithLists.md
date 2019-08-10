# Python Crash Course Chapter 4: Working With Lists

## Looping Through an Entire List

Looping allows to take the same action, or set of actions, with every item in a list regardless of how long the list is. This will be useful when performing the same statistical operation on every element in a list of numbers. Or display each headline from a list of articles on a website. When you want to perform the same action with every item in a list, you use can Python's `for` loop.

We have a list of magicians' names, and we want to print out each name in the list. We could retrieve each name individually, but it would be repetitive to do with a long list of names. For example, use a `for` loop to print out each magician's name in a list:

``` python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```
Inside the for loop, we tell Python to pull a name from the list of *magicians*, and associate it with the variable *magician*. Lastly, print the name just assigned to *magician*. Python then repeats each name once in the list. The output is a simple print of each name in the list: 

``` python
alice
david
carolina
```
