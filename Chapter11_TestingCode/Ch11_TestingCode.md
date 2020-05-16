# Python Crash Course Chapter 11: Testing Code

What we will learn in this chapter:

* Write test case for functions or classes to prove code responds correctly to all input types it's designed for.
* Test new code being added without breaking program's existing behavior.
* Catch problems before users encounter them.
* Use Python's `unittest` module to test code.

## Testing a Function

name_function.py

We need code to test for a simple function that takes in a first and last name to return a neatly formatted full name:

``` python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

The function *get_formatted_name* combines the first and last name with a space in between to complete a full name, and then capitalizes and return the full name. To make sure it works, the program *names.py* allows users to enter a first and last name to see a formatted full name:

names.py

``` python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```

When running the program, the names generated are correct. Let's try to modify the *get_formatted_name()* function to include middle names without breaking how the function handles the first and last names. We could test our code by running the program every time we modify *get_formatted_name()*, but that would become tedious.

Python provides an efficient way to automate the testing of a function's output. If we automate the testing of *get_formatted_name()*, we can always be confident that the function will work when given the names written tests for.

### Unit Tests and Test Cases

The module `unittest` from the Python standard library provides tools for testing code.

* ***Unit test*** verifies that one specific aspect of a function's behavior is correct.
* ***Test case*** is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations to handle. A good test case considers all the possible kinds of input a function could receive and includes test to represents each of these situations.
* A test case with ***full coverage*** includes a full range of unit tests covering all the possible ways to use a function.

It is often good enough to write tests for code's critical behaviors and then aim for full coverage only if the project starts to see widespread use.

### A Passing Test

The syntax for setting up a test case takes getting used to, but it is straightforward to add more unit tests for functions later. To write a test case for a function, import the `unittest` module and function to test. Then create a class that inherits from `unittest.TestCase`, and write a series of methods to test different aspects of function's behavior.

Here is a test case with one method that verifies that the function *get_formatted_name()* works correctly when given a first and last name:

test_name_function.py

``` python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

First we import `unittest` and the function we want to test, *get_formatted_name()*. We create a class called *NamesTestCase*, which will contain a series of unit tests for *get_formatted_name()*. We can name the class anything, but is best to call it something related to the function about to test and to use the word Test in the class name. This class must inherit from the class *unittest.TestCase* so Python knows how to run the tests.

*NamesTestCase* contains a single method that tests one aspect of *get_formatted_name()*. We call this method *test_first_last_name()* to verify that names with only first and last name are formatted correctly. Any method that stats with *test_* will be run automatically when we run *test_name_function.py*. Within this test method, we call the function we want to test. In this example, we call *get_formatted_name()* with the arguments 'janis' and 'joplin', and assign the result to *formatted_name*.

One of `unittest`'s most useful features: an `assert` method. Assert methods verify that result received matches the result expected to receive. To verify the result of the formatted name, `self.assertEqual(formatted_name, 'Janis Joplin')` compares the string if they are equal. If it doesn't match, it will let us know.

When a file is imported, the interpreter executes the file as it is being imported. The `if` block looks at a special variable, `__name__`, which is set when the program is executed. If this file is being run as the main program, the value of `__name__` is set to `__main__`. In this case, we call `unittest.main()`, which runs the test case. When a testing framework imports this file, the value of `__name__` won't be `__main__` and this block will not be executed.

When we run *test_name_function.py*, we get the following input:

``` markdown
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

The dot on the first line output tells us that a single test passed. The next line tells use that Python ran one test, and it took less than 0.001 seconds to run. The final **OK** tells us that all unit tests in the test case passed.

### A Failing Test

Let's modify *get_formatted_name()*, so it can handle middle names, but purposefully break the function for names with just a first and last name, like Janis Joplin.

Here's a new version of *get_formatted_name()*, that requires a middle name argument:

name_function.py

``` python
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

This version should work for people with middle names, but when we test it, the function is broken for people only with just a first and last name. Running the file gives this output:

``` markdown
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase) ----------------------------------------------------------------------
Traceback (most recent call last):
    File "test_name_function.py", line 8, in test_first_last_name
       formatted_name = get_formatted_name('janis', 'joplin')
   TypeError: get_formatted_name() missing 1 required positional argument: 'last'
---------------------------------------------------------------------- Ran 1 test in 0.000s
FAILED (errors=1)
```

The first item in the output is a single E, which tells us one unit test in the test case resulted in an error. Next, we see that *test_first_last_name()* in *NamesTestCase* caused an error. We see a standard traceback, which reports that the function call `get_formatted_name('janis', 'joplin')` no longer works because it is missing a required positional argument.

There is a summary of information about the overall test case to quickly find out how many tests failed.

### Responding to a Failed Test

When a test fails, don't change the test. Instead, fix the code that caused the test to fail. Examine the changes made to the function, and understand how those changes broke the desired behavior.

In this case *get_formatted_name()* used to require only two parameters: a first and a last name. Now it requires a first name, middle name, and last name. The addition of the mandatory middle name parameter broke the desired behavior. The best option here is to make the middle name optional. If it passes, we will move on to making sure the function handles middle names properly.

To make middle names optional, we move the parameter *middle* to the end of the parameter list in the function definition and give it an empty default value. We also add an `if` test that builds the full name properly, depending on a middle is provided:

name_function.py

``` python
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle}, {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

This new version of *get_formatted_name()*, the middle name is optional. Now the function should work for both kinds of names. To find out if the function still works for names like Janis Joplin, let's run *test_name_function.py* again:

``` markdown
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

The test case passes now. This means the function works for names including middle names. Fixing our function was easy because the failed test helped us identify the new code tha broke existing behavior.

### Adding New Tests

Now we know *get_formatted_name()* works for simple names, we can write a second test for people include a middle name by adding another method to the class *NamesTestCase*:

``` python
--snip--

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        --snip--

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
```

We name this new method *test_first_last_middle_name()*. The method name must start with `test_` so the method runs automatically when we run *test_name_function.py*. Long method names is helpful because they need to be more descriptive to make sense of the output when tests fail.

To test the function, we call *get_formatted_name()* with a first, last, and middle name, and then we ues `assertEqual()` to check that the returned full name matches the full name (first, middle, and last) that we expect.

Both tests pass when we run *test_name_function.py*:

```markdown
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK
```

Now we know that the function still works for all names that include first and last names, including middle names.

---

### TRY IT YOURSELF: Testing a Function

**11-1. City, Country**: Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a module called city _functions.py.

* Create a file called test_cities.py that tests the function you just wrote (remember that you need to import `unittest` and the function you want to test). Write a method called *test_city_country()* to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. Run test_cities.py, and make sure *test_city_country()* passes.

 **11-2. Population**: Modify your function so it requires a third parameter, population. It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. Run test _cities.py again. Make sure *test_city_country()* fails this time.

* Modify the function so the population parameter is optional. Run test _cities.py again, and make sure *test_city_country()* passes again.
* Write a second test called *test_city_country_population()* that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'. Run test_cities.py again, and make sure this new test passes.

---

## Testing a Class

We can write tests for a class like we did for a single function.

### A Variety of Assert Methods

Python provides a number of assert methods in the `unittest.TestCase` class. Assert methods test whether a condition is true at a specific point in code. If the condition is true as expected, assumption about how that part of program behaves is confirmed; we can be confident that no errors exist. If not true, Python raises an exception.

#### Table 11-1 Assert Methods Available from the `unittest` Module

| Method                  | Use                             |
|-------------------      | ----------------------          |
| assertEqual(a, b)       | Verify that a == b              |
| assertNotEqual(a, b)    | Verify that a != b              |
| assertTrue(x)           | Verify that x is True           |
| assertFalse(x)          | Verify that x is False          |
| assertIn(item, list)    | Verify that item is in list     |
| assertNotIn(item, list) | Verify that item is not in list |

These are six commonly used assert methods to verify that returned values equal or do not equal expected values. These methods are only used in class that inherits from `unittest.TestCase`.

### A Class to Test

Testing a class similar to testing a function - testing the behavior of the methods in the class with a few differences.

A class that helps administer anonymous surveys:

survey.py

``` python
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store the responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

1. This class starts with a survey question and includes an empty list to store responses.
2. Has a method to print the survey question.
3. Add a new response to the response list.
4. Print all the responses stored in the list.

To show that the *AnonymousSurvey* class works, write a program that uses the class:

language_survey.py

``` python
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

This program defines a question and creates an *AnonymousSurvey* object with that question. The program calls *show_question()* to display the question and then prompts for responses. Each response is stored as it is received. When all responses have been entered (q to quit), *show_results()* prints the survey results:

``` markdown
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language:Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin
```

Implementing changes to allow each user to enter multiple responses could accidentally change how single responses are handled. To ensure we do not break existing behavior as we develop this module, we can write tests for the class.

### Testing the AnonymousSurvey Class

Write a test that verifies one aspect of the way *AnonymousSurvey* behaves to verify that a single response to the survey question is properly stored. We use the `assertIn()` method to verify that the response is in the list of responses after it has been stored:

test_survey.py

``` python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

We start by importing the `unittest` module and the class we want to test, *AnonymousSurvey*, which is inherited from `unittest.TestCase`.

To test the behavior of a class, we need to make an instance of the class. We create an instance called *my_survey* with the question "What language did you first learn to speak?" We store a single response, English, using the *store_response()* method. Then we verify that the response was stored correctly by asserting that English is in the list of *my_survey.responses*.

When we run *test_survey.py*, the test passes:

``` markdown
.
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK
```

A single response pass the test, and now we can test multiple responses to the survey by adding another method to *TestAnonymousSurvey*:

``` python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        --snip--

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

We call the new method *test_store_three_responses()* with a list defined containing three different responses. Once the responses have been stored, we write another loop and assert that each response is now in *my_survey.responses*.

Both tests pass for single and for three responses:

``` markdown
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s
OK
```

It works but these tests are a bit repetitive. We will use another feature of `unittest` to make them more efficient.

## The setUp() Method

In *test_survey.py* we created a new instance of *AnonymousSurvey* in each test method, and created new responses in each method. The `unittest.TestCase` class has a `setUp()` method that allows to create these objects once and then use them in each of test methods. Python runs the `setUp()` method before running each method starting with *test_*. Any objects created in the `setUp()` method are then available in each test method.

Use `setUp()` to create a survey instance and a set of responses that can be used in *test_store_single_response()* and *test_store_three_responses()*:

``` python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.response[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

The method `setUp()` does two things:

1. Create a survey instance.
2. Create a list of responses.

Each is prefixed by *self*, so they can be used anywhere in the class. This makes the two test methods simpler, because neither one has to make a survey instance or response.

When testing classes, the `setUp()` method can make test methods easier to write. Make one set of instances and attributes in `setUp()` and then use these instances in all test methods.

---

### TRY IT YOURSELF: Testing a Class

**11-3. Employee**: Write a class called Employee. The `__init__()` method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called *give_raise()* that adds $5,000 to the
annual salary by default but also accepts a different raise amount.

* Write a test case for Employee. Write two test methods, *test_give_default
_raise()* and *test_give_custom_raise()*. Use the `setUp()` method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.

---

## Summary

What we learned in this chapter:

* Write tests for functions and classes using tools in the `unittest` module.
* Write a class that inherits from `unittest.TestCase`
* Use the `setUp()` method to efficiently create instances and attributes from classes to be used in all the test methods for a class.
