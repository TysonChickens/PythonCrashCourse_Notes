# Python Crash Course Chapter 8: Functions

Named blocks of code that are designed to do one specific job are called ***functions***. We can call a function to perform a particular task that we defined inside a function. Using functions makes programs easier to write, read, test, and fix because functions can be dedicated to handling a specific task. We don't have to type all the code for the same task over again multiple times throughout a program.

## Defining a Function

Here is a simple named *greet_user* that prints a greeting:

``` python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

This example shows the simplest structure of a function. We use the keyword on the first line `def`, to inform Python that we are defining a function. This is the ***function definition***, which tells Python the name of the function and if applicable, what kind of information the function needs to do its job. In this case,                       the parentheses are empty because it needs no information to do its job. Finally, the definition ends in a colon.

Any indented lines that follow *def greet_user():* make up the ***body*** of the function. The text in triple quotes is called a ***docstring***, which describes what the function does.

The only code in the function is the line *print("Hello!")*. To use this function, we call it. A ***function call*** tells Python to execute the code in the function. To ***call*** a function, write the name of the function, followed by any necessary information in parentheses. Since no information is needed here, calling our function is simple as entering *greet_user()*.

``` markdown
Hello!
```

### Passing Information to a Function

The function *greet_user()* can tell the user `Hello!` by name with slight modification. For the function to do this, add *username* in the parentheses of the function's definition. Adding it inside the parentheses of the function allows to accept any value specified. The function now expects a provided value for *username* each time it is called. When we call *greet_user()*, pass it a name, such as 'jesse', inside the parentheses:

``` python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

The function accepts the name and displays the greeting for that name:

``` markdown
Hello, Jesse!
```

We can call the function as often we want and pass it any name to produce a predictable output every time.

### Arguments and Parameters

Earlier, we defined *greet_user()* to require a value for the variable *username*. Once we called the function and gave it the information (a person's name), it printed the right greeting.

The variable *username* in the definition of *greet_user()* is an example of a ***parameter***, a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function work with in the parentheses. In this case the argument 'jesse' was passed to the function *greet_user()*, and the value was assigned to the parameter *username*.

---

### TRY IT YOURSELF: Defining a Function

**8-1. Message**: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

**8-2. Favorite Book**: Write a function called favorite_book() that accepts one parameter,title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

---

## Passing Arguments

Because a function definition can have multiple parameters, a function call may need multiple arguments. We can use ***positional arguments***, which need to be in the same order the parameters were written; ***keyword arguments***, where each argument consists of variable name and a value; and lists and dictionaries of values.

### Positional Arguments

In a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called ***positional arguments***.

Consider a function that displays information about a pet's name and kind of animal:

``` python
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
```

The definition shows that this function needs a type of animal and the animal's name. When we call *describe_pet()*, we need to provide an animal type and a name in that order. The two parameters in the function body are used to display information about the pet being described:

``` markdown
I have a hamster.
My hamster's name is Harry.
```

#### Multiple Function Calls

We can call a function as many times as needed. To describe a second, different pet by adding another call to *describe_pet()*:

``` python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

In the second function call, the function does its job as before with a set of arguments we used, but this time it prints value for a dog named Willie. Now we have a hamster named Harry and a dog named Willie:

``` markdown
I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.
```

Calling a function multiple times is a very efficient way to work. We can describe a new pet anytime by calling the function with the new information.

Positional arguments can be used as many times needed in a function. Python works through the arguments and matches each one with the corresponding parameter in the function's definition.

#### Order Matters in Positional Arguments

Unexpected results will happen if the order of the arguments are mixed up in a function call when using positional arguments:

``` python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
```

In this function call, we list the name first and the type of animal second. Now 'harry' value is assigned to the parameter *animal_type* and 'hamster' is assigned to *pet_name*.

``` markdown
I have a harry.
My harry's name is Hamster.
```

If there are strange results, double check the order of arguments in the function call matches the order of the parameters in the function's definition.

### Keyword Arguments

A ***keyword argument*** is a name-value pair that pass to a function We directly associate the name and the value within the argument to prevent confusion Keyword arguments free us from having to worry about correctly ordering arguments in the function call and they clarify the role of each value in the function call.

``` python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
```

The overall function of *describe_pet()* is the same. The only difference is we explicitly tell Python which parameter each argument should be matched with. We clarify to assign the argument 'hamster' to the parameter *animal_type* and the argument 'harry' to *pet_name*.

The order of keyword arguments doesn't matter because Python knows where each value should go and still output correctly with a hamster named Harry. The following two function calls are equivalent:

``` python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

***When using keyword argument, be sure to use exact names of the parameters in the function's definition.***

### Default Values

When writing a function, we can define a ***default value*** for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter's default value. Using default values can simplify function calls and clarify the ways in which functions are typically used.

For example, if we notice most calls to *describe_pet()* are being used to describe dogs, we can set the default value of *animal_type* to 'dog'. Now anyone calling *describe_pet()* for a dog can omit that information:

``` python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
```

Python knows to use the value 'dog' as a default value for *animal_type* when the function is called with no type specified.

``` markdown
I have a dog.
My dog's name is Willie.
```

Python still interprets this as a positional argument, so if the function is called with just a pet's name, that argument will match up with the first parameter listed in the function's definition. Therefore, the first parameter needs to be *pet_name*.

The simplest way to use this function now is to provide just a dog's name in the function call:

``` python
describe_pet('willie')
```

The only argument provided is 'willie', so it is matched up with the first parameter in the definition, *pet_name*. Because no argument is provided for *animal_type*, Python uses the default value 'dog'.

To describe an animal other than a dog, use a function call like this:

``` python
describe_pet(pet_name='harry', animal_type='hamster')
```

Python will ignore the parameter's default value because an argument for *animal_type* is provided.

***When using default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.***

## Equivalent Function Calls

Often, there are several equivalent ways to call a function because positional arguments, keyword arguments, and default values can all be used together. Consider the following definition with one default value provided:

``` python
def describe_pet(pet_name, animal_type='dog'):
```

With this definition, an argument always needs to be provided *pet_name*, and this value can be provided using the positional or keyword format. If the animal being described is not a dog, an argument for *animal_type* must be included in the call, and this argument can also be specified using the positional or keyword format.

All of the following calls would work for this function:

``` python
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

Each of these function calls would have the same output as the previous examples.

***It does not really matter which calling style is used. As long as the function calls produce the output desired, just use the style more easy to understand.***

## Avoiding Argument Errors

Unmatched arguments error occur when we provide fewer or more arguments than a function needs to do its work. For example, here is what happens if we try to call *describe_pet()* with no arguments:

``` python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()
```

Python recognizes some information is missing from the function call, and the traceback tells us:

``` markdown
Traceback (most recent call last):
    File "pets.py", line 6, in <module>
        describe_pet()
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
```

The traceback tells us the location of the problem, allowing us to look back and see that something went wrong in our function call. It also tells us the offending function call and the two missing arguments with names of them.

Python is helpful in that it reads the function's code for us and tells us the names of the arguments we need to provide. If we provide too many arguments, we should receive a similar traceback that can help identify our mistakes and correct them to match the function call to the function definition.

---

### TRY IT YOURSELF: Passing Arguments

**8-3. T-Shirt**: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

**8-4. Large Shirts**: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

**8-5. Cities**: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

---

### Return Values

A function does not always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a ***return value***. The ***return*** statement takes a value from inside a function and sends it back to the line that called the function.

### Returning a Simple Value

Here is a function that takes a first and last name to return a formatted full name:

``` python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

The definition of *get_formatted_name()* takes as parameters a first and last name. The function combines these two names, and assigns them to a variable *full_name*. The value of *full_name* is converted to title case, and then returned to the calling line.

When we call a function that returns a value, we need to provide a variable that the return value can be assigned to at *musician*. The output shows a formatted name made from parts of a person's name:

`Jimi Hendrix`

Functions can be helpful when working with a large program that needs to store many first and last names separately. We can call our previous function whenever we need to display a full name.

## Making an Argument Optional

Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. We can use default values to make an argument optional.

For example, we want to expand *get_formatted_name()* to handle middle names as well. A first attempt may look like this:

``` python
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```

This function works when given a first, middle, and last name. The function takes all three parts of a name and then builds a string out of them.

`John Lee Hooker`

Sometimes middle names are not always needed, and this function would not work if we tried to call it with only a first name and a last name. To make the middle name optional, we can give the *middle_name* argument an empty default value and ignore the argument unless the user provides a value. We set the default value of *middle_name* to an empty string and move it to the end of the list of parameters:

``` python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

In the body of the function, we check to see if a middle name has been provided. Python interprets non-empty strings as `True`, so *if middle_name* evaluates to `True` if a middle name argument is in the function call. If no middle name is provided, the empty string fails the `if` test and the `else` block runs. The full name is made with just a first and last name, and the formatted name is returned to the calling line assigned to *musician* and printed.

We have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly.

This modified version of our function works for people with just a first and last name, and it works for people who have a middle name as well:

``` markdown
Jimi Hendrix
John Lee Hooker
```

Optional values allow functions to handle a wide range of use cases while letting function calls remain as simple as possible.

## Returning a Dictionary

A function can return any kind of value, including more complicated data structures like lists and dictionaries. For example, the following function takes in parts of a name and returns a dictionary representing a person:

``` python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

The function *build_person()* takes in a first and last name, and puts these values into a dictionary. The value of *first_name* is stored with the key 'first', and the value of *last_name* is stored with the key 'last'. The entire dictionary representing the person is returned at the last line of body function. The return value is printed in the last line of the program with the original two pieces of information now stored in a dictionary:

`{'first': 'jimi', 'last': 'hendrix'}`

This function takes in simple textural information and puts it into more meaningful data structure that allows us to work with information beyond printing it. We can extend this function to accept optional values like a middle name, an age, an occupation, or any other information we want to store about a person. For example, the following change allows to store a person's age as well:

``` python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

We add a new optional parameter *age* to the function definition and assign the parameter the special value *None*, which is used when a variable has no specific value assigned to it. *None* is used as a placeholder value as it evaluates to `False` in conditional tests. The function always stores a person's name, but it can also be modified to store any other information about a person.

### Using a Function with a while Loop

We can use a *get_formatted_name()* function with a `while` loop to greet users more formally. Here is a first attempt at greeting people using their first and last names:

``` python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

We use a simple version of *get_formatted_name()* that does not include a middle name. The `while` loop asks the user the user to enter their name, and we prompt for their first and lat name separately. The problem is there is no defined quit condition inside the `while` loop. We want the user to be able to quit as easily as possible, so each prompt should offer a way to quit. The `break` statement offers a straight-forward way to exit the loop at either prompt:

``` python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit!)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

We add a message that informs the user how to quit, and then we break out of the loop if the user enters the quit value at either prompt. Now the program will continue to greet people until someone enters 'q' for either name:

``` markdown
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!
Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

---

### TRY IT YOURSELF: Function with a while Loop

**8-6. City Names**: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile" Call your function with at least three city-country pairs, and print the values that are returned.

**8-7. Album**: Write a function called make_album that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

* Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

**8-8. User Albums**: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

---

## Passing a List

We can use functions to make working with lists more efficient. The following example sends a list of names to a function called *greet_users()*, which greets each person in the list individually:

``` python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

We define *greet_users()* so it expects a list of names, which it assigns to the parameter *names*. The function loops through the list it receives and prints a greeting to each user. We define a list of users and then pass the list *usernames* to *greet_users()* in our function call:

``` markdown
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

This is the output we wanted. Every user sees a personalized greeting, and we can call the function any time to greet a specific set of users.

### Modifying a List in a Function

When we pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing us to work efficiently even when dealing with large amounts of data.

Consider a company that creates 3D printed models of designs that users submit. Designs that need to be printed are stored in a list, and after being printed moved to a separate list. The following code does this without functions:

``` python
# Start with designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#   Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

The `while` loop simulates printing each design by removing a design from the end of the list, storing it in *current_design*, and displaying a message that the current design is being printed. It then adds the design to the list of completed models until all is finished printing all the designs:

``` markdown
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

We can reorganize this code by writing two functions, each of which does one specific job. Most of the code won't change; we're just making it more carefully structured. The first function will handle printing the designs, and the second will summarize the prints that have been made:

``` python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_models)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

We first define the function *print_models()* with two parameters: a list of designs that need to be printed and a list of completed models. Given these two lists, the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models. The second function *show_completed_models()* with one parameter: the list of completed models displays the name of each model that was printed.

This program has the same output as the version without functions, but the code is much more organized. The code that does most of the work have been moved to two separate functions, which makes the main body of the program easier to understand.

``` python
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

This program is easier to extend and maintain than the version without functions. If we need to print more designs later on, we can call *print_models()* again. If we realize the printing mode needs to be modified, we can change the code once, and our changes will take place everywhere the function is called. This technique is more efficient than having to update code separately in several places in the program.

This example also demonstrates the idea that every function should have one specific job. The first function prints each design, and the second displays the completed models. When writing a function and notice the function is doing too many different tasks, try to split the code into two functions.

### Preventing a Function from Modifying a List

Sometimes we want to prevent a function from modifying a list. For example, we may decide to keep the original list of unprinted designs for our records. But since we moved all the design names out of *unprinted_designs*, the list is now empty, and the empty list is the only version we have. In this case, we can address this issue by passing the function a copy of the list, not the original. Any changes the function makes to the list will affect only the copy, leaving the original list intact.

We can send a copy of a list to a function like this:

``` python
function_name(list_name[:])
```

The slice notation `[:]` makes a copy of the list to send to the function. If we didn't want to empty the list of unprinted designs, we could call *print_models()*:

``` python
print_models(unprinted_designs[:], completed_models)
```

This time, it uses a copy of the original unprinted designs list, not the actual *unprinted_designs* list. The list *completed_models* will fill up with the names of printed models like it did before, but the original list of unprinted designs will be unaffected by the function.

Even though we can preserve the contents of a list by passing a copy to your functions, it is best to pass the original list to functions unless there is a specific reason to pass a copy. It is more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially with large lists.

---

### TRY IT YOURSELF: Passing a List

**8-9. Messages**: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

**8-10. Sending Messages**: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

**8-11. Archived Messages**: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

---

## Passing an Arbitrary Number of Arguments

Python allows a function to collect an arbitrary number of arguments from the calling statement if we don't know how many arguments a function needs to accept.

Consider a function that builds a pizza. It needs to accept a number of toppings, but can't know ahead of time how many topping a person will want. The function in the following example has one parameter, **toppings*, but this parameter collects as many arguments as the calling line provides:

``` python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

The asterisk in the parameter name of **toppings* tells python to make an empty tuple called *toppings* and pack values it receives into this tuple. Note that Python prints the arguments into a tuple, even if the function receives only one value:

``` markdown
('pepperoni')
('mushrooms', 'green peppers', 'extra cheese')
```

Now we can replace the `print()` call with a loop that runs through the list of toppings and describes the pizza being ordered:

``` python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

The function works as intended, whether it receives one value or three values:

``` markdown
Making a pizza with the following toppings:
- pepperoni

 Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

This syntax works no matter how many arguments the function receives.

### Mixing Positional and Arbitrary Arguments

For a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

If the function needs to take in a size for the pizza, that parameter must come before the parameter **toppings*:

``` python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

In the function definition, Python assigns the first value it receives to the parameter *size*. All other values that come after are stored in the tuple *toppings*.

Now each pizza has a size and a number of toppings, and each piece of information is printed in the proper place, showing size first and toppings after:

``` markdown
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### Using Arbitrary Keyword Arguments

We can write functions that accept as many key-value pairs as the calling statement provides if we don't know what kind of information will be passed to the function. One example is building user profiles: get information about a user, but not sure what kind of information to receive. The function *build_profile* in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:

``` python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
```

The definition of *build_profile()* expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. The double asterisks before ***user_info* cause Python to create an empty dictionary called *user_info* and pack whatever name-value pairs it receives into this dictionary.

In the body of *build_profile()* function, we add the first and last names to the *user_info* dictionary because we will always receive these two pieces of information from the user, and they have not been placed into the dictionary yet. Then we finally return the *user_info* dictionary to the function call line.

We assign the returned *profile* to *user_profile* and print *user_profile*:

``` markdown
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```

The returned dictionary contains the user's first and last names including the location and field of study as well. The function would work no matter how many additional key-value pairs are provided in the function call.

We can mix positional, keyword, and arbitrary values in many different ways when writing functions.

***The parameter name **kwargs used to collect non-specific keyword argument is frequently used.*****

---

### TRY IT YOURSELF: Passing Arbitrary Arguments

**8-12. Sandwiches**: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

**8-13. User Profile**: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

**8-14. Cars**: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

`car = make_car('subaru', 'outback', color='blue', tow_package=True)`

Print the dictionary that’s returned to make sure all the information was stored correctly.

## Storing Functions in Modules

An advantage of functions is the way they separate blocks of code from the main program. By using descriptive names for functions, the main program will be easier to follow. We can take an extra step by storing functions in a separate file called a **module** and then **importing** that module into the main program. An **import* statement tells Python to make the code in a module available in the current running program file.

Storing functions in a separate file allows to hide details of program's code and focus on higher-level logic. It also allows us to reuse functions in many different programs with easy sharing access to files. Knowing how to import functions also allows use to use libraries of functions that other programmers have written.

There are multiple ways to import a module.

### Importing an Entire Module

To start importing modules, we first need to create a module. A **module** is a file ending in .py that contains the code we want to import into our program. Let's make a module that contains the function *make_pizza()*.

``` python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
```

Now we make a separate file called *making_pizzas.py* in the same directory as the original file. This file imports the module we just created and then makes two calls to *make_pizza()*:

``` python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The first line tells Python to open the file *pizza.py* and copy all the function from it into this program. Python copies the code behind the scenes just before the program runs.

To call a function from an imported module, enter the name of the module imported, *pizza*, followed by the name of the function, *make_pizza()*, separated by a dot. This code produces the same output as the original problem that didn't import a module.

``` markdown
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

This approach to importing using **import** followed by the name of the module, makes every function from the module available in the program. Each function in the module is available through the following syntax:

``` markdown
module_name.function_name()
```

### Importing Specific Functions

We can import a specific function from a module:

``` python
from module_name import function_name
```

We can import as many functions from a module separating each function's name with a comma:

``` markdown
from module_name import function_0, function_1, function_2
```

From the pizza example, it would look like this to import only the function:

``` python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

With this syntax, we don't need to use the dot notation when we call a function. We explicitly imported the function *make_pizza()* in the import statement, we can call it by name when we use the function.

### Using as to Give a Function an Alias

If the function being imported might conflict with an existing name in the program or if the function name is long, use a short, unique **alias** - an alternate name similar to a nickname for the function.

Here we give the function *make_pizza()* an alias, *mp()*, by importing `make_pizza as mp`. The keyword *as* renames a function using the alias provided:

``` python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The **import** statement show here renames the function *make_pizza()* to *mp()* in this program. Any time we want to call the function, we write mp() instead, and Python will run the code while avoiding any confusion with another *make_pizza()* function in the program file.

The general syntax for providing an alias is:

``` python
from module_name import function_name as fn
```

### Using as to Give a Module an Alias

We can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows to call the module's functions more quickly. Calling *p.make_pizza()* is more concise than calling *pizza.make_pizza()*:

``` python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The module is given an alias in the import statement, but all of the module's function retain their original names. An alias helps writing concise code and redirects attention from the module name to focus on the descriptive names of its functions. These function names, which clearly tell us what each function does, are more important to the readability of code than using the full module name.

The general syntax:

``` python
import module_name as mn
```

### Importing All Functions in a Module

To import every function in a module, use the asterisk (*) operator:

``` python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The asterisk in the *import* statement tells Python to copy every function from the module *pizza* into this program file. Because every function is imported, we can call each function by name without using the dot notation. Try to avoid this approach when working with large modules because unexpected results can occur if a function has the same name. Python may see several functions or variables and may overwrite the functions.

The best approach is to import the functions, or import the entire module and use the dot notation. This leads to clear code that is easy to read and understand.

``` python
from module_name import *
```

---

### TRY IT YOURSELF: Storing Functions in Modules

**8-15. Printing Models**: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

**8-16. Imports**: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:

``` python
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
```

---

## Summary

What we learned in this chapter:

* How to write functions and to pass arguments so functions have access to information required to work.
* Use positional and keyword arguments, and to accept an arbitrary number of arguments.
* Functions that display output and functions that return values.
* Use functions with lists, dictionaries, if statements, and while loops.
* Store functions in separate files called **modules**.
* How functions can help write code for easy to read, understand, test, and debug.
