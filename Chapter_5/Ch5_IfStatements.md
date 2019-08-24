# Python Crash Course Chapter 5: If Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's `if` statement allows to examine the current state of a program and respond appropriately to that state. The ability to write conditional tests allow the program to check any condition of interest.

## Conditional Tests

In every `if` statement, there is an expression that can be evaluated as `True` or `False` and it is called a *conditional test*. Python uses values of `True` and `False` to decide whether the code in an `if` statement should be executed. If a conditional statement evaluates to `True`, Python executes the code following the `if` statement. If the test evaluates to `False`, Python ignores the code following the `if` statement.

## Checking for Equality

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

## Ignoring Case When Checking for Equality

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

## Checking for Inequality

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

## Numerical Comparisons

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

## Checking Multiple Conditions

It is possible to check for multiple conditions at the same time. Sometimes, a program might need two conditions to be `True` to take action. Other times, one condition being `True` is good enough. The keywords `and` and `or` can help in these situations.

## Using and to Check Multiple Conditions

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

## Using or to Check Multiple Conditions

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

## Checking Whether a Value Is in a List

To find out whether a particular value is already in a list, use the keyword `in`. For a pizzeria, we will make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.

``` python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True

>>> 'pepperoni' in requested_toppings
False
```

They keyword `in` tells Python to check for the existence of *'mushrooms'* and *'pepperoni'* in the list of *requested_toppings*. This technique is helpful because it can easily check whether the value being tested matches one of the values in the list.

## Checking Whether a Value is Not in a List

Other times, it is important to know if a value does not appear in a list. The keyword to use is `not` in this situation. For example, consider a list of users who are banned from commenting in a forum. This can check if a user has been banned before allowing that person to submit a comment:

``` python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

If the value of *user* is not in the list of *banned_users*, Python returns `True` and executes the indented line. Therefore, the user *'marie'* is not in the list *banned_users*, so she sees a message inviting her to post a response:

`Marie, you can post a response if you wish.`

## Boolean Expressions

A *Boolean expression* is another name for a conditional test. A *Boolean value* is either `True` or `False`, just like the value of a conditional expression after it has been evaluated.

Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:

``` python
game_active = True
can_edit = False
```

Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

---

## TRY IT YOURSELF: Conditional Tests

**5-1. Conditional Tests**: Write a series of conditional tests. Print a statement describing each test and your prediction for 
the results of each test. Your code should look something like this:

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
