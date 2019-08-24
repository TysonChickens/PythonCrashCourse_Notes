# Python Crash Course Chapter 5: If Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's `if` statement allows to examine the current state of a program and respond appropriately to that state. The ability to write conditional tests allow the program to check any condition of interest.

## Conditional Tests

In every `if` statement, there is an expression that can be evaluated as `True` or `False` and it is called a *conditional test*. Python uses values of `True` and `False` to decide whether the code in an `if` statement should be executed. If a conditional statement evaluates to `True`, Python executes the code following the `if` statement. If the test evaluates to `False`, Python ignores the code following the `if` statement.

## Checking for Equality

Most conditional statements compare the current value of a variable specific value of interest. The simplest conditional test checks whether the value of a variable is equal to the value of interest:

``` python
car = 'bmw'
car == 'bmw'
> True
```

The second line checks whether the value of car is *'bmw'* using a double equal sign (==). This *equality operator* returns `True` if the values on the left and right side of the operator match, and `False` if they don't match. When the value of car is anything other other than *'bmw'*, the test returns `False`:

``` python
car = 'audi'
car =='bmw'
> False
```

A single equal sign is a statement to assign a value. With a double equal sign, is almost asking a question to double check if the value exists. Most programming languages use equal signs in this way.

## Ignoring Case When Checking for Equality

Testing for equality is case sensitive in Python. For exmaple, two values with different capitalization are not considered equal:

``` python
car = 'Audi'
car == 'audi'
> False
```

If case matters, this behavior is advantageous. But if case does not matter and instead want to test the value of variable, convert the variable's value to lowercase before doing the comparison:

``` python
car = 'Audi'
car.lower() == 'audi'
> True

print(car)
> 'Audi'
```

The variable *car* is converted to all lowercase and compare the lowercase value to the string *'audi*'. The two strings match, so Python returns `True`. In the last line, the original variable value has not been affected by the `lower()` method.

Websites enforce certain rules for the data that users enter in a manner similar to this. For example, a site might use a conditional test to ensure that every user has a truly unique username, not just a variation on the capitalization of another person's username. When someone submits a new username, that new username is converted to lowercase and compared to the lowercase versions of all existing usernames. During this check, a username like 'John' will be rejected if any variation of 'john' is already in use.

