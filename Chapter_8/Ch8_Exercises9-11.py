# 8-9 Messages: Make a list containing a series of short text messages.
def show_messages(messages):
    """Print each text message in a list."""
    for message in messages:
        print(message)



# 8-10 Sending Messages: Start with a copy of program from Exercise 8-9 and write a function called send_messages().
def send_messages(messages, sent_messages):
    while messages:
        sent_text = messages.pop()
        sent_messages.append(sent_text)

# Lists to store all text messages.
texts = ['this is fun.', 'testing.', 'I like you.']
sent_messages = []

# 8-9
show_messages(texts)

# 8-11 Archived Messages: Call the function send_messages() with a copy of the list of messages.
send_messages(texts[:], sent_messages)

# Print to verify both lists show original has list has retained its messages.
print("\nHere is the original text messages:")
print(texts)
print(sent_messages)

# 8-10
send_messages(texts, sent_messages)
# Print to verify the messages have moved correctly to the lists.
print("\nWe are going to send these messages:")
print(texts)
print(sent_messages)

