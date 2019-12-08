# 7-4 Pizza toppings: Write a loop that prompts the user to enter a series of toppings until they 'quit'.
# For each topping, print a message saying added to their pizza.
prompt = "\nWhat kind of toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are done. "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("I am current adding " + topping + " to your pizza!")
    else:
        break

# 7-5 Movie tickets: A movie theater charges different ticket prices depending on age.
prompt = "\nHow old are you? I will check how much a ticket costs."
prompt += "\nEnter 'quit' to close the program. "


while True:
    message = input(prompt)
    if message == 'quit':
        break
    
    ## If age is less than 3, the ticket is free. $10 between age 3 and 12. $15 over age 12.
    age = int(message)
    if age < 3:
        print("The ticket is free.")
    elif age < 13:
        print("The ticket costs $10.")
    else:
        print("The ticket costs $15.") 


