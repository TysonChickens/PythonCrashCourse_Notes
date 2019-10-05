# Python Crash Course Chapter 8: Functions

Named blocks of code that are designed to do one specific job are called ***functions***. We can call a function to perform a particular task that we defined inside a function. Using functions makes programs easier to write, read, test, and fix because functions can be dedicated to handling a specific task. We don't have to type all the code for the same task over again multiple times throughout a program.

## Defining a Function

Here is a simple named *greet_user* that prints a greeting:

``` python
def greet_user():
"""Display a simple greeting."""
print("Hello!")

greet_user()
```

This example shows the simplest structure of a function. We use the keyword on the first line, `def`, to inform Python that we are defining a function. This is the ***function definition***, which tells Python the name of the function, and if applicable, what kind of information the function needs to do its job. In this case, the parentheses are empty because it needs no information to do its job. Finally, the definition ends in a colon.

Any indented lines that follow *def greet_user():* make up the ***body*** of the function. The text in triple quotes is called a ***docstring***, which describes what the function does.

The only code in the function is the line *print("Hello!")*. To use this function, we call it. A ***function call*** tells Python to execute the code in the function. To ***call*** a function, write the name of the function, followed by any necessary information in parentheses. Since no information is needed here, calling our function is simple as entering *greet_user()*.

``` markdown
Hello!
```

### Passing Information to a Function

The function *greet_user()* can tell the user `Hello!` by name with slight modification. For the function to do this, add *username* in the parentheses of the function's definition. Adding it inside the parentheses of the function allows to accept any value specified. The function now expects a provided value for *username* each time it is called. When we call *greet_user()*, pass it a name, such as 'jesse', inside the parentheses:

``` python
def greet_user(username):
"""Display a simple greeting."""
print(f"Hello, {username.title()}!")

greet_user('jesse')
```

The function accepts the name and displays the greeting for that name:

``` markdown
Hello, Jesse!
```

We can call the function as often we want and pass it any name to produce a predictable output every time.

### Arguments and Parameters

Earlier, we defined *greet_user()* to require a value for the variable *username*. Once we called the function and gave it the information (a person's name), it printed the right greeting.

The variable *username* in the definition of *greet_user()* is an example of a ***parameter***, a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function work with in the parentheses. In this case the argument 'jesse' was passed to the function *greet_user()*, and the value was assigned to the parameter *username*.

---

### TRY IT YOURSELF: Defining a Function

**8-1. Message**: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

**8-2. Favorite Book**: Write a function called favorite_book() that accepts one parameter,title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

---

## Passing Arguments

Because a function definition can have multiple parameters, a function call may need multiple arguments. We can use ***positional arguments***, which need to be in the same order the parameters were written; ***keyword arguments***, where each argument consists of variable name and a value; and lists and dictionaries of values.

### Positional Arguments

In a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called ***positional arguments***.

Consider a function that displays information about a pet's name and kind of animal:

``` python
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
```

The definition shows that this function needs a type of animal and the animal's name. When we call *describe_pet()*, we need to provide an animal type and a name, in that order. The two parameters in the function body are used to display information about the pet being described:

``` markdown
I have a hamster.
My hamster's name is Harry.
```

#### Multiple Function Calls

We can call a function as many times as needed. To describe a second, different pet by adding another call to *describe_pet()*:

``` python
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

In the second function call, the function does its job as before with a set of arguments we used, but this time it prints value for a dog named Willie. Now we have a hamster named Harry and a dog named Willie:

``` markdown
I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.
```

Calling a function multiple times is a very efficient way to work. We can describe a new pet anytime by calling the function with the new information.

Positional arguments can be used as many times needed in a function. Python works through the arguments and matches each one with the corresponding parameter in the function's definition.

#### Order Matters in Positional Arguments

Unexpected results will happen if the order of the arguments are mixed up in a function call when using positional arguments:

``` python
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
```

In this function call, we list the name first and the type of animal second. Now 'harry' value is assigned to the parameter *animal_type* and 'hamster' is assigned to *pet_name*.

``` markdown
I have a harry.
My harry's name is Hamster.
```

If there are strange results, double check the order of arguments in the function call matches the order of the parameters in the function's definition.

### Keyword Arguments

A ***keyword argument*** is a name-value pair that pass to a function. We directly associate the name and the value within the argument to prevent confusion. Keyword arguments free us from having to worry about correctly ordering arguments in the function call, and they clarify the role of each value in the function call.

``` python
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
```

The overall function of *describe_pet()* is the same. The only difference is we explicitly tell Python which parameter each argument should be matched with. We clarify to assign the argument 'hamster' to the parameter *animal_type* and the argument 'harry' to *pet_name*.

The order of keyword arguments doesn't matter because Python knows where each value should go and still output correctly with a hamster named Harry. The following two function calls are equivalent:

``` python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

***When using keyword argument, be sure to use exact names of the parameters in the function's definition.***

### Default Values

When writing a function, we can define a ***default value*** for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter's default value. Using default values can simplify function calls and clarify the ways in which functions are typically used.

For example, if we notice most calls to *describe_pet()* are being used to describe dogs, we can set the default value of *animal_type* to 'dog'. Now anyone calling *describe_pet()* for a dog can omit that information:

``` python
def describe_pet(pet_name, animal_type='dog'):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
```

Python knows to use the value 'dog' as a default value for *animal_type* when the function is called with no type specified.

``` markdown
I have a dog.
My dog's name is Willie.
```

Python still interprets this as a positional argument, so if the function is called with just a pet's name, that argument will match up with the first parameter listed in the function's definition. Therefore, the first parameter needs to be *pet_name*.

The simplest way to use this function now is to provide just a dog's name in the function call:

``` python
describe_pet('willie')
```

The only argument provided is 'willie', so it is matched up with the first parameter in the definition, *pet_name*. Because no argument is provided for *animal_type*, Python uses the default value 'dog'.

To describe an animal other than a dog, use a function call like this:

``` python
describe_pet(pet_name='harry', animal_type='hamster')
```

Python will ignore the parameter's default value because an argument for *animal_type* is provided.

***When using default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.***

## Equivalent Function Calls

Often, there are several equivalent ways to call a function because positional arguments, keyword arguments, and default values can all be used together. Consider the following definition with one default value provided:

``` python
def describe_pet(pet_name, animal_type='dog'):
```

With this definition, an argument always needs to be provided *pet_name*, and this value can be provided using the positional or keyword format. If the animal being described is not a dog, an argument for *animal_type* must be included in the call, and this argument can also be specified using the positional or keyword format.

All of the following calls would work for this function:

``` python
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

Each of these function calls would have the same output as the previous examples.

***It does not really matter which calling style is used. As long as the function calls produce the output desired, just use the style more easy to understand.***

## Avoiding Argument Errors

Unmatched arguments error occur when we provide fewer or more arguments than a function needs to do its work. For example, here is what happens if we try to call *describe_pet()* with no arguments:

``` python
def describe_pet(pet_name, animal_type='dog'):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()
```

Python recognizes some information is missing from the function call, and the traceback tells us:

``` markdown
Traceback (most recent call last):
File "pets.py", line 6, in <module>
describe_pet()
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
```

The traceback tells us the location of the problem, allowing us to look back and see that something went wrong in our function call. It also tells us the offending function call and the two missing arguments with names of them.

Python is helpful in that it reads the function's code for us and tells us the names of the arguments we need to provide. If we provide too many arguments, we should receive a similar traceback that can help identify our mistakes and correct them to match the function call to the function definition.

---

### TRY IT YOURSELF: Passing Arguments

**8-3. T-Shirt**: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

**8-4. Large Shirts**: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

**8-5. Cities**: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

---
