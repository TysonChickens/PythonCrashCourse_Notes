# Python Crash Course Chapter 5: If Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's `if` statement allows to examine the current state of a program and respond appropriately to that state. The ability to write conditional tests allow the program to check any condition of interest.

## Conditional Tests

In every `if` statement, there is an expression that can be evaluated as `True` or `False` and it is called a *conditional test*. Python uses values of `True` and `False` to decide whether the code in an `if` statement should be executed. If a conditional statement evaluates to `True`, Python executes the code following the `if` statement. If the test evaluates to `False`, Python ignores the code following the `if` statement.

### Checking for Equality

Most conditional statements compare the current value of a variable specific value of interest. The simplest conditional test checks whether the value of a variable is equal to the value of interest:

``` python
>>> car = 'bmw'
>>> car == 'bmw'
True
```

The second line checks whether the value of car is *'bmw'* using a double equal sign (==). This *equality operator* returns `True` if the values on the left and right side of the operator match, and `False` if they don't match. When the value of car is anything other other than *'bmw'*, the test returns `False`:

``` python
>>> car = 'audi'
>>> car =='bmw'
False
```

A single equal sign is a statement to assign a value. With a double equal sign, is almost asking a question to double check if the value exists. Most programming languages use equal signs in this way.

### Ignoring Case When Checking for Equality

Testing for equality is case sensitive in Python. For example, two values with different capitalization are not considered equal:

``` python
>>> car = 'Audi'
>>> car == 'audi'
False
```

If case matters, this behavior is advantageous. But if case does not matter and instead want to test the value of variable, convert the variable's value to lowercase before doing the comparison:

``` python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True

>>> car
'Audi'
```

The variable *car* is converted to all lowercase and compare the lowercase value to the string *'audi*'. The two strings match, so Python returns `True`. In the last line, the original variable value has not been affected by the `lower()` method.

Websites enforce certain rules for the data that users enter in a manner similar to this. For example, a site might use a conditional test to ensure that every user has a truly unique username, not just a variation on the capitalization of another person's username. When someone submits a new username, that new username is converted to lowercase and compared to the lowercase versions of all existing usernames. During this check, a username like 'John' will be rejected if any variation of 'john' is already in use.

### Checking for Inequality

To determine whether two value are not equal, combine an exclamation point and an equal sign (!=). The exclamation point represents *not*, as it does in many programming languages.

Let's use another `if` statement to examine how to use the inequality operator. In a variable, store a requested pizza topping and then print a message if the person did not order anchovies:

``` python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
print("Hold the anchovies!")
```

Because the value of *requested_topping* is not *'anchovies'*, the `print()` function is executed. If the two values match, Python returns `False` and does not run the code following the `if` statement. If these two values do not match, Python returns `True` and executes the code following the `if` statement.

`Hold the anchovies!`

Most conditional expressions will test for equality, but sometimes it is more efficient to test for inequality.

### Numerical Comparisons

Testing numerical values is straightforward. For example, the following code checks whether a person is 18 years old:

``` python
>>age = 18
>>age == 18
True
```

Also test to see if two numbers are not equal. For example, the following code prints a message if the given answer is not correct:

``` python
answer = 17

if answer != 42:
print("That is not the correct answer. Please try again!")
```

The conditional test passes, because the value of *answer (17)* is not equal to *42*. Because the test passes, the indented code block is executed:

`That is not the correct answer. Please try again!`

Various mathematical comparisons in conditional statements can be included as well.

``` python
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

Each mathematical comparison can be used as part of an `if` statement, which can help detect exact conditions of interest.

### Checking Multiple Conditions

It is possible to check for multiple conditions at the same time. Sometimes, a program might need two conditions to be `True` to take action. Other times, one condition being `True` is good enough. The keywords `and` and `or` can help in these situations.

### Using and to Check Multiple Conditions

To check whether two conditions are both `True` simultaneously, use the keyword `and` to combine the two conditional tests; if each test passes, the overall expression evaluates to `True`. If either test fails or if both tests fail, the expression evaluates to `False`.

A check whether two people are both over 21:

``` python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False

>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

In the first part of the code, one test passes, but the other test fails and the overall expression evaluates to `False`. When *age_1* is changed to 22, both individual tests pass causing the overall conditional expression to evaluate as `True` since age is now greater than 21.

To improve readability, the use of parentheses around the individual tests, but they are not required. The test would look like this using parentheses:

``` python
(age_0 >= 21) and (age_1 >= 21)
```

### Using or to Check Multiple Conditions

The keyword `or` allows to check multiple conditions when it passes either or both of the individual tests. An `or` expression fails only when both individual tests fail.

Let's consider two ages again, but only one person has to be over 21:

``` python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True

>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### Checking Whether a Value Is in a List

To find out whether a particular value is already in a list, use the keyword `in`. For a pizzeria, we will make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.

``` python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True

>>> 'pepperoni' in requested_toppings
False
```

They keyword `in` tells Python to check for the existence of *'mushrooms'* and *'pepperoni'* in the list of *requested_toppings*. This technique is helpful because it can easily check whether the value being tested matches one of the values in the list.

### Checking Whether a Value is Not in a List

Other times, it is important to know if a value does not appear in a list. The keyword to use is `not` in this situation. For example, consider a list of users who are banned from commenting in a forum. This can check if a user has been banned before allowing that person to submit a comment:

``` python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

If the value of *user* is not in the list of *banned_users*, Python returns `True` and executes the indented line. Therefore, the user *'marie'* is not in the list *banned_users*, so she sees a message inviting her to post a response:

`Marie, you can post a response if you wish.`

### Boolean Expressions

A *Boolean expression* is another name for a conditional test. A *Boolean value* is either `True` or `False`, just like the value of a conditional expression after it has been evaluated.

Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:

``` python
game_active = True
can_edit = False
```

Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

---

### TRY IT YOURSELF: Conditional Tests

**5-1. Conditional Tests**: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

``` python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
```

* Look closely at your results, and make sure you understand why each line
evaluates to True or False .
* Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False .

**5-2. More Conditional Tests**: You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for
each of the following:

* Tests for equality and inequality with strings
* Tests using the lower() method
* Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
* Tests using the and keyword and the or keyword
* Test whether an item is in a list
* Test whether an item is not in a list

---

## if Statements

With knowledge of conditional tests, it is time to write `if` statements. Several different kinds of `if` statements exist to use depends on the number of conditions to test.

### Simple if Statements

The simplest kind of `if` statement has one test and one action:

``` python
if conditional_test:
    do something
```

Any conditional test in the first line and about any action in the indented block following the test can be used. If the conditional test evaluates to `True`, Python executes the following `if` statement. If the test evaluates to `False`, Python ignores the code following the `if` statement.

The following code tests whether the person's age is old enough to vote:

``` python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

Python checks to see whether the value of *age* is greater than or equal to 18. Therefore, Python executes the indented `print()` call:

`You are old enough to vote!`

Indentation plays the same role in `if` statements as it did in `for` loops. All indented lines after an `if` statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.

There can be as many lines of code in the block following the `if` statement. Let's add another line of output if the person is old enough to vote, asking if the individual has registered to vote yet:

``` python
age = 19
if age >= 18:
print("You are old enough to vote!")
print("Have you registered to vote yet?)
```

The conditional tests passes, and both `print()` calls are indented, so both lines are printed:

``` markdown
You are old enough to vote!
Have you registered to vote yet?
```

If the value of *age* is less than 18, this program would produce no output.

### if-else Statements

Often, we will want to take one action when a conditional test passes and a different action in all other cases. Python's `if-else` syntax makes this possible. An `if-else` block is similar to a simple `if` statement, but the `else` statement allows to define an action or set of actions that are executed when the conditional test fails.

Now add a message for anyone who is not old enough to vote:

``` python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

Because *age* is less than this time, the conditional test fails with `False` and the code in the `else` block is executed:

``` markdown
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

This code works because it has only two possible solutions to evaluate: a person it either old enough to vote or not old enough to vote. The `if-else` structure works well in situations in where Python will always execute one of two possible actions.

### The if-else Chain

To test more than two possible situations, and to evaluate these by the use of Python's `if-elif-else` syntax. Python executes only one block in an `if-elif-else` chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.

Many real-world situations involve more than two possible conditions. For example, consider an amusement park that charges different rates for different age groups:

* Admission for anyone under age 4 is free.
* Admission for anyone between the ages of 4 and 18 is $25.
* Admission for anyone age 18 or older is $40.

The following code tests for the age group of a person and then prints an admission price message:

``` python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```

In this example, the test evaluates to `False`, so the first code block is not executed. However, the second test evaluates to `True` (12 is less than 18) so its code is executed. The output is one sentence, informing the user of the admission cost:

`Your admission cost is $25.`

Any age greater than 17 would cause the first two tests fail. In these situations, the `else` block would be executed and the admission price would be $40.

It would be more concise to set just the price inside the `if-elif-else` chain and then have a simple `print()` call that runs after the chain has been evaluated:

``` python
age = 12

if age < 4 :
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission price is ${price}.")
```

The code produces the same output as the previous example, but the purpose of the `if-elif-else` chain is narrower. Instead of determining a price and displaying a message, it simply determines the admission price. This approach is more efficient and easier to modify than the original approach. To change the text of the output message, the only need to change is one `print()` call rather than three separate `print()` calls.

### Using Multiple elif Blocks

There can be as many `elif` blocks in a piece of code. For example, if the amusement part were to implement a discount for seniors, it is possible to add one more conditional test to the code to determine if someone qualified for the senior discount. Let's say anyone 65 or older pays half the regular admission, or $20:

``` python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

Most of the code is unchanged. Now there is a second `elif` block that checks to make sure a person is less than age 65 before assigning them full admission rate of $40. Notice the value assigned to the `else` block needs to be changed to $20, because the only ages that make it to this block are people 65 or older.

### Omitting the else Block

Python does not require en `else` block at the end of an `if-elif` chain. sometimes an `else` block is useful; sometimes it is clearer to use an additional `elif` statement that catches the specific condition of interest:

``` python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

The extra `elif` block near the end assigns a price of $20 when the person is 65 or older, which is a bit clearer than the general `else` block. With the new change, every block of code must pass a specific test in order to be executed.

The `else` block is a catchall statement to match any condition that wasn't matched by a specific `if` or `elif` statement. If there is a specific final condition to test for, consider using an `elif` block and omit the `else` block. This will add extra confidence that the code will run only under the correct conditions.

### Testing Multiple Conditions

The `if-elif-else` chain is powerful, but only appropriate to use when only one test is required to pass. As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial because it's efficient and allows to test for one specific condition.

Sometimes, it is important to check all of the conditions. In this case, use a series of simple `if` statements with no `elif` or `else` blocks. This technique makes sense when more than one condition could be `True`, and want to act on every condition that is `True`.

Let's reconsider the pizzeria example. If someone requests a two-topping pizza, be sure to include both toppings on their pizza:

``` python
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

We start with a list containing the requested toppings. The `if` statement checks to see whether the person requested mushrooms on their pizza. If so, a message is printed confirming that topping. The test for pepperoni is another simple `if` statement, not an `elif` or `else` statement, so this test is run regardless of whether the previous test passed or not. The last `if` statement checks whether extra cheese was requested regardless of the results from the first two tests. These three independent tests are executed every time this program is run.

Because every condition is evaluated, both mushrooms and extra cheese are added to the pizza:

``` markdown
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

This code will not work properly if used with `if-elif-else` block, because the code would stop running after only one test passes.

``` python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

The test for *mushrooms* is the first test to pass, so mushrooms are added to the pizza. The rest of the code is not checked by Python because doesn't run any tests beyond the first test that passes in an `if-elif-else` chain. The first topping will be added, but all other toppings will be missed:

``` markdown
Adding mushrooms.

Finished making your pizza!
```

In summary, use an `if-elif-else` chain to run only one block of code. If more than one block of code needs to run, use a series of independent `if` statements.

---

### TRY IT YOURSELF: if Statements

**5-3. Alien Colors #1**: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red' .

* Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
* Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

**5-4. Alien Colors #2**: Choose a color for an alien as you did in Exercise 5-3, and write an if - else chain.

* If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
* If the alien’s color isn’t green, print a statement that the player just earned 10 points.
* Write one version of this program that runs the if block and another that runs the else block.

**5-5. Alien Colors #3**: Turn your if - else chain from Exercise 5-4 into an if - elif - else chain.

* If the alien is green, print a message that the player earned 5 points.
* If the alien is yellow, print a message that the player earned 10 points.
* If the alien is red, print a message that the player earned 15 points.
* Write three versions of this program, making sure each message is printed for the appropriate color alien.

**5-6. Stages of Life**: Write an if - elif - else chain that determines a person’s stage of life. Set a value for the variable age and then:

* If the person is less than 2 years old, print a message that the person is a baby.
* If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
* If the person is at least 4 years old but less than 13, print a message that the person is a kid.
* If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
* If the person is at least 20 years old but less than 65, print a message that the person is an adult.
* If the person is age 65 or older, print a message that the person is an elder.

**5-7. Favorite Fruit**: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

* Make a list of your three favorite fruits and call it favorite_fruits .
* Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

---

## Using if Statements with Lists

Interesting work can be done when lists and `if` statements are used together. You can be manage changing conditions efficiently, such as the availability of certain items in a restaurant throughout a shift. Also begin to prove that code works as you expect it to in all possible situations.

### Checking for Special Items

Let's take a look at how you can watch for special values in a list and handle those values appropriately.

With the pizzeria example, the pizzeria displays a message whenever a topping is added to your pizza being made. The code for this action can be written very efficiently by making a list of toppings the customer has requested and using a loop to announce each topping added to the pizza:

``` python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

The output is straightforward:

``` markdown
Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!
```

What if the pizzeria runs of green peppers? An `if` statement inside for `for` loop can handle this situation appropriately:

``` python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

This time we check each requested item before adding it to the pizza. The code checks to see if the person requested green peppers, and displays a message informing them they can't have green peppers. The `else` block ensures all other toppings will be added to the pizza.

``` markdown
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### Checking That a List Is Not Empty

So far, we assumed that each list has at least one item in it. It is useful to check whether a list is empty before running a `for` loop.

As an example, let's check whether the list of requested toppings is empty before building the pizza. If the list is empty, we'll prompt the user and make sure they want a plain pizza. If the list is not empty, build the pizza just as we did in the previous examples:

``` python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

Python returns `False` because it is an empty list. Since the conditional test fails, we print a message asking the customer if they really want a plain pizza. If *requested_toppings* passes the conditional test, we run the same `for` loop in the previous example.

The list is empty, so the output asks if the user really wants a plain pizza:

`Are you sure you want a plain pizza?`

If the list is not empty, the output will show each requested topping being added to the pizza.

### Using Multiple Lists

What if a customer actually wants french fries on their pizza? You can use lists and `if` statements to make sure input makes sense before you act on it.

Let's watch out for unusual topping requests before we build a pizza. The following example defines two lists. The first is a list of available toppings at the pizzeria, and the second is the list of toppings that the user has requested. This time, each item in *requested_toppings* is checked against the list of available toppings before it's added to the pizza:

``` python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

This code syntax produces clean, informative output:

``` markdown
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

In just a few lines of code, we’ve managed a real-world situation pretty effectively!

---

### TRY IT YOURSELF: Using if Statements with Lists

**5-8. Hello Admin**: Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

* If the username is 'admin' , print a special greeting, such as Hello admin, would you like to see a status report?
* Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

**5-9. No Users**: Add an if test to hello_admin.py to make sure the list of users is not empty.

* If the list is empty, print the message We need to find some users!
* Remove all of the usernames from your list, and make sure the correct message is printed.

**5-10. Checking Usernames**: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

* Make a list of five or more usernames called current_users.
* Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
* Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used print a message saying that the username is available.
* Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

**5-11. Ordinal Numbers**: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in *th*, except 1, 2, and 3.

* Store the numbers 1 through 9 in a list.
* Loop through the list.
* Use an if - elif - else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th" , and each result should be on a separate line.

---

## Summary

What we learned in this chapter:

* Write conditional tests, which always evaluate to `True` or `False`.
* Write simple `if` statements, `if-else` chains, and `if-elif-else` chains.
* Identify particular conditions needed to test and known when those conditions have been met in programs.
* Handle certain items in a list differently than all other items while continuing to utilize the efficiency of a `for` loop.
