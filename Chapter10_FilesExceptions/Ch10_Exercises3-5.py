# 10-3 Program that prompts the user for their name and save their response to guest.txt

filename = 'Chapter10_FilesExceptions/guest.txt'

prompt_name = input("Enter your name to be on the guest list: ")
with open(filename, 'w') as file_object:
    file_object.write(prompt_name)



# 10-4 Write a while loop that prompts the users for name.

filename = 'Chapter10_FilesExceptions/guest_book.txt'

prompt = "Enter your name to be on the guest list:"
prompt += "\nEnter 'quit' to end the program.\n"

while True:
    prompt_name = input(prompt)
    if prompt_name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(prompt_name + "\n")
        print(f"Welcome to the guest list {prompt_name}!\n")



# 10-5 Programming poll and store all the answers.

filename = 'Chapter10_FilesExceptions/programming_poll.txt'

responses = []

while True:
    response = input("\nWhy do you like programming?\n")
    responses.append(response)

    continue_prompt = input("\nWould you like to continue? (yes/no) ")
    if continue_prompt == 'no':
        break

with open(filename, 'a') as file:
    for response in responses:
        file.write(f"{response}\n")




    


