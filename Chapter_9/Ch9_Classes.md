# Python Crash Course Chapter 9: Classes

**Object-oriented programming** is one of the most effective approaches to writing software. We write **classes** that represent real-world things and situations, and create **objects** based on these classes. When we write a class, we define the general behavior that a whole category of objects can have. Each object can then be given unique traits along with their general behavior.

Making an object from a class is called **instantiation**, and we work with **instances** of a class. We will write classes and create instances of those classes. We will specify the information that can be stored in instances, and define actions that can be taken with these instances.

Understanding object-oriented programming will help see the world as a programmer and understand the logic to write programs effectively.

## Creating and Using a Class

We can model almost anything using classes. Start with a simple class, *Dog*, that represents a dog - not one dog but any dog. We know all dogs have a name and age, and know most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go in our *Dog* class because they are most common to dogs. Then, use it to make individual instances, each of which represents one specific dog.

### Creating the Dog Class

Each instance created from the *Dog* class will store a *name* and an *age*, and give each dog the ability to *sit()* and *roll_over()*:

``` python
class Dog:
    """A simple attempt to model a dog."""

    def__init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

We first define a class called *Dog*. By convention, capitalized names refer to classes in Python. There are no parentheses in the class definition because we're creating this class from scratch. Then, we write a docstring describing what this class does.

### The `__init__()` Method

A function that is part of a class is a **method**. Everything learned about functions applies to methods as well; the only difference for now is the way we will call methods. The `__init__()` method is a special method that Python runs automatically whenever we create a new instance based on the *Dog* class. This method has two leading underscores and two trailing underscores, a convention that helps prevent Python's default method names from conflicting with method names.
We define `__init__()` method to have three parameters: *self*, *name*, and *age*. The *self* parameter is required in the method definition, and must come first before other parameters. It is required because Python calls this method later to create an instance of *Dog*, and method call will automatically pass the *self* argument. It allows individual instance access to the attributes and methods in the class. When we make an instance of *Dog*, Python will call the `__init__()` method from the *Dog* class. We pass *Dog()* a name and an age as arguments; *self* is passed automatically. Whenever we want to make an instance from the *Dog* class, we have to provide values for only the last two parameters, *name* and *age*.

The two variables defined have the prefix *self*. Any variable prefixed with the *self* is available to every method in the class, and we'll be able to access these variables through any instance created from the class. The line `self.name = name` takes the value associate with the parameter *name* and assigns it to the variable *name*, which is then attached to the instance being created. The same process occurs with `self.age = age`. Variables that are accessible through instances like this are called **attributes**.

The *Dog* class has two other methods defined: *sit()* and *roll_over()*. Because these methods don't need additional information to run, we just define them to have one parameter, *self*. The instances we create later will have access to these methods. For now, *sit()* and *roll-over()* print a message saying the dog is sitting or rolling over. However, this concept can be extended to realistic situations: if this class were part of an actual computer game, these methods would contain code to make an animated dog sit and roll over. If this class was written to control a robot, these methods would direct movements that cause a robotic dog to sit and roll over.

### Making an Instance from a Class

Think of a class as a set of instructions for how to make an instance. The class *Dog*, is set of instructions that tells Python how to make individual instances representing specific dogs.

``` python
class Dog:
    """A simple attempt to model a dog."""

    def__init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

Python creates a dog named 'Willie' with age is 6. When Python reads *my_dog*, it calls the `__init__()` method in *Dog* with the arguments 'Willie' and 6. It creates an instance representing this particular dog and sets the *name* and *age* attributes using the values we provided. Python then returns an instance representing this dog, and we assign it to the variable *my_dog*. Usually, we can assume that a capitalized name like *Dog* refers to a class, and a lowercase name like *my_dog* refers to a single instance created from a class.

#### Accessing Attributes

To access the attributes of an instance, we can use dot notation. We can access the value of *my_dog*'s attribute *name*:

``` python
my_dog.name
```

Dot notation is often used in Python. This syntax demonstrates how Python finds an attribute's value. Python looks at the instance *my_dog* and then finds the attribute *name*. associated with *my_dog*. This is the same referred to as *self.name* in the class *Dog*. The same approach works with the attribute age.

The output summary about *my_dog*:

``` markdown
My dog's name is Willie.
My dog is 6 years old.
```

#### Calling Methods

After we create an instance from the class *Dog*, we can use dot notation to call any method defined in *Dog*.

``` python
class Dog:
    """A simple attempt to model a dog."""

    def__init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```

To call a method, give the name of the instance (my_dog) and the method to call, separated by a dot. When Python reads *my_dog.sit()*, it looks for the method *sit()* in the class *Dog* and runs that code. Python interprets *my_dog.roll_over()* in the same way.

``` markdown
Willie is now sitting.
Willie rolled over!
```

This syntax is helpful when attributes and methods have been given appropriate descriptive names to easily infer what a block of code is supposed to do.

#### Creating Multiple Instances

Many instances can be created from a class. We can create a second dog called *your_dog*:

``` python
class Dog:
    """A simple attempt to model a dog."""

    def__init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

In this example, we create a dog named Willie and a dog named Lucy. Each dog is separate instance with its own set of attributes, capable of the same set of actions.

``` markdown
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
```

Even if we used the name and age for the second dog, Python would still create a separate instance from the *Dog* class. We can create as many instances from one class as we need, as long we give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

---

### TRY IT YOURSELF: Creating and Using a Class

**9-1. Restaurant**: Make a class called Restaurant. The `__init__()` method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

**9-2. Three Restaurants**: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

**9-3. Users**: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

---

## Working with Classes and Instances

Classes can be used to represent many real-world situations. Once a class is created, we spend most of our time working with instances created from that class. The first task is to modify the attributes of an instance directly or write methods that updates attributes in specific ways.

### The Car Class

Our class will store information about a car, and a method that will summarize the information.

``` python
class Car:

    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
```

In the *Car* class, we define the `__init__()` method with the *self* parameter first. There are also three parameters: *make, model, year*. The `__init__()` method takes in these parameters and assigns them to the attributes that will be associated with instances made from this class.

The *get_descriptive_name()* method puts the car's *year*, *make*, and *model* into one string neatly describing the car.

We finally make an instance from the *Car* class and assign it to the variable *my_new_car*. Then we call *get_descriptive_name()* to show what kind of car we have:

``` markdown
2019 Audi A4
```

To make the class more interesting, we can add an attribute that changes over time that stores the car's overall mileage.

### Setting a Default Value for an Attribute

When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the `__init__()` method, where they are assigned a default value.

Let's add an attribute called *odometer_reading* that always starts with a value of 0. We also add a method *read_odometer()* that helps us read each car's odometer:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

This time Python when Python calls the `__init__` method to create a new instance, it stores the make, model, and year values as attributes like it did in the previous example. Then Python creates a new attribute called *odometer_reading* and sets its initial value to 0. We also have a new method called *read_odometer()* that makes it easy to read a car's mileage.

The car starts with a mileage of 0:

``` markdown
2019 Audi A4
This car has 0 miles on it.
```

### Modifying Attribute Values

There are three ways to change an attribute's value: directly through an instance, set the value through the method, or increment the value (add a certain amount to it) through a method.

#### Modifying an Attribute's Value Directly

The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

We use the dot notation to access the car's *odometer_reading* attribute and set its value directly. This tells Python to take the instance *my_new_car*, find the attribute *odometer_reading* with it, and set the value to 23:

``` markdown
2019 Audi A4
This car 23 miles on it.
```

Sometimes, we will want to access attributes directly like this, but other times to write a method that updates the value.

#### Modifying an Attribute's Value Through a Method

Instead of accessing the attribute directly, we can pass the new value to a method that handles updating.

Here is an example showing a method called *update_odometer()*:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")



my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

The method of *update_odometer()* takes in a mileage value and assigns it to *self.odometer_reading*. We call *update_odometer()* and give it 23 as an argument (corresponding to *mileage* parameter), and *read_odometer()* prints the reading:

``` markdown
2019 Audi A4
This car has 23 miles on it.
```

We can extend the method *update_odometer()* to do additional work every time the odometer reading is modified. Let's add some logic to make sure no one tries to roll back the odometer reading:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
```

Now *update_odometer()* checks that the new reading makes sense before modifying the attribute.

#### Incrementing an Attribute's Value Through a Method

Here's a method that allows us to pass an incremental amount and add the value to the odometer reading:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

The new method *increment_odometer()* takes in a number of miles, and adds this value to *self.odometer_reading*. We set *my_used_car* odometer to 23,500 by passing it to *update_odometer()*. Later, we call *increment_odometer()* and pass it to 100 to add the 100 miles that we drove between buying the car and registering it:

``` markdown
2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```

We can easily modify this method later on to reject negative increments so no one uses this function to roll back an odometer.

---

### TRY IT YOURSELF: Working with Attributes

**9-4. Number Served**: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called *set_number_served()* that lets you set the number of customers that have been served. Call this method with a new number and print the value again.

Add a method called *increment_number_served()* that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

**9-5. Login Attempts**: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called *increment_login _attempts()* that increments the value of login_attempts by 1. Write another method called *reset_login_attempts()* that resets the value of login_attempts to 0.

Make an instance of the User class and call *increment_login_attempts()* several times. Print the value of login_attempts to make sure it was incremented properly, and then call *reset_login_attempts()*. Print login_attempts again to make sure it was reset to 0.

---

### Inheritance

We don't always have to start from scratch when writing a class. If the class we want to write is a specialized version of another class we wrote, we can use **inheritance**. When one class **inherits** from another, it takes on the attributes and methods of the first class. The original class is called the **parent class**, and the new class is the **child class**. The child can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.

### The `__init__()` Method for a Child Class

When writing a new class based on an existing class, we often want to call the `__init__()` method from the parent class. This will initialize any attributes that were defined in the parent `__init__()` method and make them available in the child class.

Let's model an electric car as an example, An electric car is just a specific kind of car, so we can base our new *ElectricCar* class on the *Car* from earlier. Then we'll only have to write code for the attributes and behavior specific to electric cars.

Here is a simple version of the *ElectricCar* class, which does everything the *Car* class:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
```

When creating a child class, the parent class must be part of the current file and must appear before the child class in the file. We define the child class, *ElectricCar* with the name of the parent class must be included in the parentheses. The `__init__()` method takes in the information required to make a *Car* instance.

The *super()* function is a special function that allows to call a method from the parent class. This line tells Python to call the `__init__()` method from *Car*, which gives *ElectricCar* instance all the attributes defined in that method. The name **super** comes from a convention of calling the parent class a **superclass** and the child class a **subclass**.

We test whether inheritance is working properly by trying to create an electric car with the same kind of information we provide when making a regular car. We make an instance of the *ElectricCar* class and assign it to *my_tesla*. It calls the `__init__()` method defined in *ElectricCar* to call the method defined in the parent class *Car*. We provide the arguments 'tesla', 'model s', and 2019.

There are no attributes or methods yet that are particular to an electric car. At this point, we make sure the electric car has the appropriate *Car* behaviors:

``` markdown
2019 Tesla Model S
```

The *ElectricCar* instance works just like an instance of *Car*, so now we can begin defining attributes and method specific to electric cars.

### Defining Attributes and Methods for the Child Class

Once a child class is inherited from a parent class, we can add any new attributes and methods necessary to differentiate the child class from the parent class.

Let's add an attribute that's specific to electric cars (battery, for example) and a method to report on this attribute. We'll store the battery size and write a method that prints a description of the battery:

``` python
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

We add a new attribute *self.battery_size* and set its initial value to 75. This attribute will be associated with all instances created from the *ElectricCar* class, but won't be associated with any instances of *Car*. Also, added a method called *describe_battery()* that prints information about the battery to get a description specific to an electric car:

``` markdown
2019 Tesla Model S
This car has a 75-kWh battery.
```

There is no limit how much specialize the *ElectricCar* class. We can add as many attributes and methods as we need to model an electric car. Anyone who uses the *Car* class will have that functionality available as well, and the *ElectricCar* class will only contain code for the information and behavior specific to electric vehicles.

### Overriding Methods from the Parent Class

We can override any method from the parent class that doesn't fit what we are trying to model with the child class. To do this, we define a method in the child class with the same name as the method we want to override in the parent class. Python will ignore the parent class method and only focus on the method defined in the child class.

For example, the class *Car* had a method called *filled_gas_tank()*. This method is meaningless in an all-electric vehicle, so we want to override this method.

``` python
class ElectricCar(Car):

    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```

If someone tries to call *fill_gas_tank()* with an electric car, Python will ignore the method in *Car* and run this code instead. When using inheritance, we can make sure child classes retain what we need and override anything we don't need from the parent class.

### Instances as Attributes

When modeling something from the real world, we may keep adding more and more detail to a class filled with methods and attributes and it may become lengthy. In certain situations, recognize that part of one class can be written as a separate class. We can break a large class into smaller classes that work together.

For example, if we continue adding detail to the *ElectricCar* class, we might notice that we are adding many attributes and methods specific to the car's battery. We can stop and move those attributes and methods to a separate class called *Battery*. Then we use a *Battery* instance as an attribute in the *ElectricCar* class:

``` python
class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
```

We first define a new class called *Battery* that does not inherit from any other class. The `__init__()` method has one parameter, *battery_size*, in addition to *self*. This is an optional parameter that sets the battery's size to 75 if no value is provided. The method *describe_battery()* has been moved to this class as well.

Inside the *ElectricCar* class, we now add an attribute called *self.battery*. This line tells Python to create a new instance of *Battery* (default size of 75) and assign that instance to the attribute *self.battery*. Any *ElectricCar* instance will now have a *Battery* instance created automatically.

We create an electric car and assign it to the variable *my_tesla*. When we want to describe the battery, we need to work through the car's *battery* attribute:

``` python
my_tesla.battery.describe_battery()
```

The output is identical to what we saw previously:

``` markdown
2019 Tesla Model S
This car a 75-kWh battery.
```

This looks like extra work, but now we can describe the battery in as much detail as we want without cluttering the *ElectricCar* class. Let's add another method to *Battery* that reports the range of the car based on the battery size:

``` python
class Car:
    --snip--

class Battery:
    --snip--

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    --snip--

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

The new method *get_range()* performs simple analysis to report the range depending on the battery size. When we want to use this method, we have to call it through the car's *battery* attribute.

The output tells us the range of the car based on its battery size:

``` markdown
2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

### Modeling Real-World Objects

Modeling more complicated things can be difficult to wrestle with interesting questions. There are often no right or wrong approaches to modeling real-world situations. Some are more efficient tha others, but it takes practice to find the most efficient representations. If the code is working, that is great! Don't be afraid to rip apart and rewrite using different approaches in the quest to write accurate, efficient code.

---

### TRY IT YOURSELF: Inheritance

**9-6. Ice Cream Stand**: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

**9-7. Admin**: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called *show_privileges()* that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

**9-8. Privileges**: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the *show_privileges()* method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

**9-9. Battery Upgrade**: Use the final version of electric_car.py from this section. Add a method to the Battery class called *upgrade_battery()*. This method should check the battery size and set the capacity to 100 if it isn’t already. Make an electric car with a default battery size, call *get_range()* once, and then call *get_range()* a second time after upgrading the battery. You should see an increase in the car’s range.

---

## Importing Classes

Files can get long when we add more functionality to classes, even when we use inheritance. To help reduce clutter, Python lets us store classes in modules and then import the classes into the main program.

### Importing a Single Class

Let's create a module containing just the Car class with a more specific filename such as *car.py*

``` python
""" A class that can be used to represent a car."""

class Car:
    """ A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attribute to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if attempt to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```

On the first line, we include a module-level docstring that briefly describes the contents of the module. It is recommended to write a docstring for each module created.

Now we make a separate file called *my_car.py* to import the *Car* class and then create an instance from that class:

``` python
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

The `import` statement tells Python to open the *car* module and import the class *Car*. Now we can use the *Car* class as if it were defined in this file. The output is the same earlier:

``` markdown
2019 Audi A4
This car has 23 miles on it.
```

Importing classes is an effective way to program. Moving classes to a module and importing them help keep the main program file stay clean and easy to read. Also, store most of the logic in separate files; once classes work, leave those files alone and focus on the higher-level logic of the main program.

### Storing Multiple Classes in a Module

We can store many classes in a single module, although each class in a module should be related. The classes *Battery* and *ElectricCar* both help represent cars, so let's add them in the module *car.py*.

``` python
"""A set of classes used to represent gas and electric cars."""

class Car:
    """ A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attribute to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if attempt to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range of this battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 345
        print(f"This car can go about {range} miles on a full charge.")

    class ElectricCar(Car):
        """Models aspects of a car, specific to electric vehicles."""

        def __init__(self, make, model, year):
            """
            Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car.
            """
            super().__init__(make, model, year)
            self.battery = Battery()
```

Now we can make a new file called *my_electric_car.py*, import the *ElectricCar* class, and make an electric car:

``` python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

This has the same output we saw earlier, even though most of the logic is hidden away in a module:

``` markdown
2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

### Importing Multiple classes from a Module

We can import as many classes into a program file. If we want to make a regular car and an electric car in teh same file, we need to import both classes, *Car* and *ElectricCar*:

``` python
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

We import multiple classes from a module by separating each class with a comma. Once imported the necessary classes, we can make as many instances of each class as needed.

In this example, we make a regular Volkswagen Beetle and an electric Tesla Roadster.

``` markdown
2019 Volkswagen Beetle
2019 Tesla Roadster
```

### Importing an Entire Module

We can also import an entire module and the access the classes using dot notation. This approach is simple and results in code that is easy to read. Because every call that creates an instance of a class includes the module name, we won't have naming conflicts with any names used in the current file.

Here what it looks like to import the entire car module and then create a regular car and an electric car:

``` python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

We import the entire car module and then access the classes through `module_name.ClassName` syntax to create the cars.

### Importing All Classes from a Module

Every class from a module can be imported using the following syntax:

``` python
from module_name import *
```

This method is not recommended because it is unclear which classes are used from the module and cause confusion. It is better to import the entire module and use `module_name.ClassName` syntax to avoid naming conflicts and clearly understand where the module is used in the program.

### Importing a Module in a Module

Sometimes we will want to spread out classes over several modules to keep any one file from growing too large and avoid unrelated classes in the same module. When one module depends on a class in another module, we can import the required class into the first module.

For example, store the *Car* class in one module, and the *ElectricCar* and *Battery* classes in a separate module. We will make a new module called *electric_car.py* - replacing the file created earlier - and copy just the *Battery* and *ElectricCar* classes into the file:

``` python
"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    --snip--

class ElectricCar(Car):
    --snip--
```

The class *ElectricCar* needs to access to its parent class *Car*, so we import *Car* directly into the module. We also need to update the *Car* module so it contains only the *Car* class:

``` python
"""A class that can be used to represent a car."""

class Car:
    --snip--
```

Now we can import from each module separately and create whatever kind of car we need:

``` python
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

We import *Car* from its module, and *ElectricCar* from its module. We then create one regular car and one electric car. Both kinds of cars are created correctly:

``` markdown
2019 Volkswagen Beetle
2019 Tesla Roadster
```

### Using Aliases

Seen in Chapter 8, aliases can be helpful when using modules to organize code.

As an example, consider a program where we want to make a variety of electric vehicles. It might get tedious to type *ElectricCar* multiple times. We can give *ElectricCar* an alias in the import statement:

``` python
from electric_car import ElectricCar as EC
```

Now we can use this alias when making an electric car:

``` python
my_tesla = EC('tesla', 'roadster', 2019)
```

### Finding Your Own Workflow

Python provides many options to structure code in a large project. It is important to know all the possibilities to determine best ways to organize projects and others.

Keep the code structure simple in one file and once everything is working, try to separate and organize in modules. Just write code that works and go from there.

---

### TRY IT YOURSELF: Importing Classes

**9-10. Imported Restaurant**: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

**9-11. Imported Admin**: Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call *show_privileges()* to show that everything is working correctly.

**9-12. Multiple Modules**: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call *show_privileges()* to show that everything is still working correctly.

---
