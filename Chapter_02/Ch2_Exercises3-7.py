# 2-3 Personal Message
first_name = "Tyson"
message = f"Hello, {first_name}! This is a simple greeting message!"
print(message)

# 2-4 Name Cases
full_name = "lou will"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# 2-5 Famous Quote
quote = 'Bill Gates once said, "I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it." \nI agree with this statement. Work smarter, not harder!'
print(quote)

# 2-6 Famous Quote 2
author = "Bill Gates"
quote = "I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it."
message = f'{author} once said, "{quote}"'
print(message)

# 2-7 Stripping Names
full_name = " \tAllison Parker\n"
print(full_name)

## Strip the whitespace around the name.
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())
