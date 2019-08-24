# Python Crash Course Chapter 5: If Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's `if` statement allows to examine the current state of a program and respond appropriately to that state. The ability to write conditional tests allow the program to check any condition of interest.

## Conditional Tests

In every `if` statement, there is an expression that can be evaluated as `True` or `False` and it is called a *conditional test*. Python uses values of `True` and `False` to decide whether the code in an `if` statement should be executed. If a conditional statement evaluates to `True`, Python executes the code following the `if` statement. If the test evaluates to `False`, Python ignores the code following the `if` statement.

## Checking for Equality

Most conditional statements compare the current value of a variable specific value of interest. The simplest conditional test checks whether the value of a variable is equal to the value of interest:

``` python
car = 'bmw'
car == 'bmw'
>> True
```

The second line checks whether the value of car is *'bmw'* using a double equal sign (==). This *equality operator* returns `True` if the values on the left and right side of the operator match, and `False` if they don't match. When the value of car is anything other other than *'bmw'*, the test returns `False`:

``` python
car = 'audi'
car =='bmw'
>> False
```

A single equal sign is a statement to assign a value. With a double equal sign, is almost asking a question to double check if the value exists. Most programming languages use equal signs in this way.

## Ignoring Case When Checking for Equality
