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

