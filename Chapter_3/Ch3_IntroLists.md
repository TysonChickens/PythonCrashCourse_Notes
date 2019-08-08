# Python Crash Course Chapter * 3: Introducing Lists

## What Is a List

A *list* is a collection of items in a particular order. A list consist of letters of the alphabet, the digits from 0-9, or the names of all the people in a family. Any thing can be entered into a list, and items in the list don't have to be related in any particular way. It is good practice to make the name of the list plural, such as **letters**, **digits**, or **names**.

In Python, square brackets `[]` indicate a list, and individual ements in the list are separated by commas.

``` python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

Returns `['trek', 'cannondale', 'redline', 'specialized']`.

## Accessing Elements in a List

Lists are ordered collections, so you can access any element in a list by telling Python the position, or *index*, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets. Let's pull out the first bicycle in the list of `bicycles`:

``` python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

Python will return just the element at that position `trek`.

The use of string methods will work on any element in the list to have a clean, neatly formatted output by using the `title()` method.

`print(bicycles[0].title())` will capitalize the word to `Trek`.

## Index Positions Start at 0, Not 1

Python considers the first item in a list to be at position 0, not position 1. This is true for most programming languages because of how list operations are implemented at a lower level.

The second item in a list has an index of 1. Using this counting system, you can retrieve any elemnt you want from a list by substracting one from its position in the list. If you want the fourth item in a list, you can request the item at index * 3.

Python has a special syntax for accessing the last element in a list. At index -1, Python always returns the last item in the list:

`bicycles[-1]` will return `specialized`.

This convention also extends to other negative index values as well. At index -2, returns the second item from the end of the list, and index -* 3 returns the third item from the end, and so on.

## Using Individual Values from a List

You can use individual values from a list just as you would with any other variable. For example, use f-strings to create a message based ona a value from a list.

``` python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
```

We built a sentence using the value at `bicycle[0]` and assign it to the variable `message`.

`My first bicycle was a Trek.`

---

### TRY IT YOURSELF: Lists

Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises to keep
them organized.

* **3-1. Names**: Store the names of a few of your friends in a list called names . Print
each person’s name by accessing each element in the list, one at a time.

* **3-2. Greetings**: Start with the list you used in Exercise * 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

* **3-3. Your Own List**: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

---

## Changing, Adding, and Removing Elements

Most lists created will be dynamic, meaning a built list and then add and remove elements as program runs its course. For example, a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. Each time a new alien appears on screen, you add it to the list. The list of aliens will increase and decrease in length throughout the game.

## Modifying Elements in a List

The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value. For example, a list of motorcycles, and the first item in the list is `honda`. How could we change it?

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

The original list with `honda` in the first element is now replaced with `ducati`. The rest of the list stays the same. You can change the value of any item in the list, not just the first item.

## Adding Elements to a List

You might want to add a new element to a list for many reasons. For example, make aliens appear in a game, add new data to a visualization, or add new registered users to a website. Python provides several ways to add new data to existing lists.

## Appending Elements to End of a List

The simplest way to add a new element to a list is to `append` the item to the list. When an item is append to a list, the new element is added to the end of the list.

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
```

The `append()` method adds `ducati` to the end of the list without affecting any other of the elements in the list:

``` python
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

The `append()` method makes it easy to build lists dynamically. Start with an empty list and then add items to the list using a series of `append()` calls.

``` python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```

The resulting list looks exactly the same: `['honda', 'yamaha', 'suzuki']`.

Building lists this way is very common, because you often won't know the data users want to store in a program until after the program is running. To put users in control, start defining an empty list that will the users' values. Finally, append each new value provided to the list just created.

## Inserting Elements into a List

You can add a new element at any position in a list by using the `insert()` method. This is achieved by specifying the index of the new element and the value of the new item.

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')

print(motorcycles)
```

The code inserts the value `ducati` at the beginning of the list. The `insert()` method opens a space at position 0 and stores the value `ducati` at that location. This shifts every other value in the list one position to the right:

`['ducati', 'honda', 'yamaha', 'suzuki']`

## Removing Elements from a List

Often, you will want to remove an item or a set of items from a list. For example, when a player shotos down an alien from the sky, most likely want to remove it from the list of active aliens. Or when a user decides to cancel their account on a web application, you will want to remove that user from the list of active users. You can remove an item according to its position in the list or according to its position in the list or according to its value.

## Removing an Item Using the del Statement

If you the position of the item you want to remove from the list, you can use the `del` statement.

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles
```

The code uses `del` to remoev the first item, `honda`, from the list of motorcycles:

``` python
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

You can remove an item from any position in a list using the `del` statement if you know its index.

## Removing an Item Using the pop() Method

Sometimes, you will want to use the value of an item after you remove it from a list. For example, get the x and y position of an alien that was just shot down to draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.

The `pop()` method removes the last item in the list, but allows to work with that item after removing it. The term comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this case, the top of the stack refers to the end of the list.

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
```

The popped value returns `suzuki` and is now removed from the original motorcycles list. This is useful when the motorcycles list are stored in chronological order according to when we owned them. The pop value will tell about the last motorcycle we bought:

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
```

`The last motorcycle I owned was a Suzuki.` A simple sentence about the most recent motorcycle we owned.

## Popping Items from any Position in a List

You can use `pop()` to remove an item from any position in a list by including the index of the item you want to remove in parentheses.

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
```

`The first motorcycle I owned was a Honda.` By popping the first motorcycle in the list, then print a message about first motorcycle ever owned.

Remember, each time `pop()` is used, the item is no longer stored in the list.

If unsure whether to use `del` statement or `pop()` method, use `del` when to delete an item from a list and not use that item in any way. If you want to use an item as you remove it, use the `pop()` method instead.

## Removing an Item by Value

Sometimes, the position of the value you want to remove from a list is unknown. The `remove()` method is used if you only know the value of the item you want to remove. For example, we want to remove the value 'ducati' from the list of motorcycles:

``` python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
```

`['honda', 'yamaha', 'suzuki']`. Python figures out wher 'ducati' appears in the list and removes that element.

The `remove()` method can also be used to work with a value that's being removed from a list. Let's remove the value 'ducati' and print a reason for removing it from the list:

``` python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```

`A Ducati is too expensive for me.`

We used the `too_expensive` variable and assigned to `'ducati'` with a reason to remove from the list. The value is still accessible through the variable despite being removed from the motorcycles list.

***The `remove()` method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed.***

---

### TRY IT YOURSELF: Modifying Lists

* **3-4. Guest List**: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

* **3-5. Changing Guest List**: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

  * Start with your program from *Exercise 3-4*. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
  * Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
  * Print a second set of invitation messages, one for each person who is still in your list.

* **3-6. More Guests**: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
  * Start with your program from *Exercise 3-4 or Exercise 3-5*. Add a print() call to the end of your program informing people that you found a bigger dinner table.

  * Use insert() to add one new guest to the beginning of your list.
  * Use insert() to add one new guest to the middle of your list.
  * Use append() to add one new guest to the end of your list.
  * Print a new set of invitation messages, one for each person in your list.

* **3-7. Shrinking Guest List**: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
  * Start with your program from Exercise * 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
  * Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
  * Print a message to each of the two people still on your list, letting them know they’re still invited.
 Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

---

## Organizing a List

Often, list will be created in an unpredicatable order, because it is not possible to always control the order in which users provide their data. Sometimes, information is best presented in a particular order or preserve the original order of the list. Other times, changing the original order is useful. Python provides a number of different ways to organize a list, depending on the situation.

## Sorting a List Permanently with the sort() Method

Python's `sort()` method makes it relatively easy to sort a list. Imagine a list of cars and want to change the order of list to store them alphabetically. To keep the task simple, let's assume that all the values in the list are lowercase.

``` python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

`['audi', 'bmw', 'subaru', 'toyota']`

The sort() method changes the order ofthe list permanently in alphabetical order, and can no longer revert to the original order. This can also be sorted in reverse alphabetical order by passing the argument `reverse = True` to the `sort()` method.

``` python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

`['toyota', 'subaru', 'bmw', 'audi']`. Again, the order of the list is permanently changed.

## Sorting a List Temporarily with the sorted() Function

To maintain the original order of a list but present it in a sorted order, the `sorted()` function is used. This allows to display a list in a particular order but doesn't affect the actual order of the list.

``` python
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
```

The original list still exists in its original order after the `sorted()` function has been used. The function can also accept a `reverse = True` argument if want to display in reverse alphabetical order.

***Sorting a list alphabetically is a bit more complicated when all the values are not in
lowercase. There are several ways to interpret capital letters when determining a sort
order, and specifying the exact order can be more complex than we want to deal with
at this time.***

## Printing a List in Reverse Order

To reverse the original order of a list, the `reverse()` method is used. If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into reverse chronological order:

``` python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
```

Notice `reverse()` doesn't sort backward alphabetically; it simply reverse the order of the list:

``` python
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

The method changes the order of a list permanently, but can revert to the original order anytime by applying `reverse()` to the same list a second time.

## Finding the Length of a List

The `len()` function is used to quickly find the length of a list. The list in this example has four item, so its length is 4:

``` python
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
```

Finding the length will be usefil when to identify the number of aliens that still need be to be shot down in a game, determine the amount of data to manage in visualization, or figure out the number of registered users on a website, among other tasks.

***Python counts the items in a list starting with one, so there shouldn't be any off-by-one erros when determining the length of a list.***

---

### TRY IT YOURSELF: Organizing a List

* **3-8. Seeing the World**: Think of at least five places in the world you’d like to visit.

  * Store the locations in a list. Make sure the list is not in alphabetical order.
  * Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
  * Use sorted() to print your list in alphabetical order without modifying the actual list.
  * Show that your list is still in its original order by printing it.
  * Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
  * Show that your list is still in its original order by printing it again.
  * Use reverse() to change the order of your list. Print the list to show that its order has changed.
  * Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
  * Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
  * Use sort() to change your list so it’s stored in reverse alphabetical order.
  * Print the list to show that its order has changed.

* **3-9. Dinner Guests**: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.

* **3-10. Every Function**: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or any thing else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

---

## Avoiding Index Errors When Working With Lists

One type of error is common to see when working with lists for the first time. For example, a list with three items, and try to ask for the fourth item:

``` python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
```

The code will return results as an *index error*:

``` python
Traceback (most recent call last):
File "motorcycles.py", line 2, in <module>
print(motorcycles[3])
IndexError: list index out of range
```

Python attempts to print the item at index 3 but no item exists in the list that has an index of 3. This is because of the off-by-one nature of indexing in lists and is a common error. Python starts indexing at 0, therefore, the third item in the list is at index 2 of the list.

***If an index error occurs and can't figure out how to resolve it, try printing the list or just printing the length of the list. It helps to see the actual list, or the exact number of items in the list since it might look different than expected.***

---

### TRY IT YOURSELF: Errors With Lists

* **3-11. Intentional Error**: If you haven't received an index error in one your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure to correct the error before closing the program.

---

## Summary

What we learned in this chapter:

* What lists are and how to work with individual items in a list.

* How to define a list and how to add and remove elements.

* Sort lists permanently and temporarily for display purposes.

* Find the length of a list and how to avoid index errors.
