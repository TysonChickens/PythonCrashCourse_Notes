import random
from random import randint

# 9-13 Make a class Die with one attribute called sides with a default value.
class Die:
    """Model a die with 6-sides to print a random number between 1 and the number of sides."""

    def __init__(self, sides=6):
        self.sides = sides

    """Rolls a random number between 1 and the number of sides the die has 10 times."""
    def roll_die(self):
        results = []

        for num in range(10):
            result = randint(1, self.sides)
            results.append(result)
        return(results)

# Roll each die 10 times.
# This is a six-sided die with default value of 6.
six = Die()
print(f"Here are results for a 6-sided die rolled 10 times: {six.roll_die()}")


# This is a ten-sided die.
ten = Die(10)
print(f"Here are results for a 10-sided die rolled 10 times: {ten.roll_die()}")

# This a twenty-sided die.
twenty = Die(20)
print(f"Here are results for a 20-sided die rolled 10 times: {twenty.roll_die()}")



# 9-14 Make a list or tuple containing a series of 10 numbers and five letters for the lottery.
lottery = [1, 2, 5, 7, 10, 15, 50, 44, 13, 100, 'f', 'a', 'z', 't', 'y']

win_ticket = random.choices(lottery, k=4)
print(f"Here is the matching ticket to win the lottery! {win_ticket}")


# 9-15 Use a loop to analyze the results until winning the lottery.
my_ticket =  [10, 'f', 'y', 2]

# Loop until my_ticket pulls the winning ticket and count how many attempts.
counter = 0
while my_ticket != win_ticket:
    counter += 1
    my_ticket = random.choices(lottery, k=4)
    if my_ticket == win_ticket:
        print(f"It took {counter} attempts to win the lottery! My ticket is: {my_ticket}")
        break


# 9-16 Exploring Python Standard Library with datetime module.
import datetime

today = datetime.date.today()
print("Today: ", today)

five_days = datetime.timedelta(days=5)
print("Five days: ", five_days)


print("Today date - five days: ", today - five_days)