# 3-1 List names of friends

## I have no friends!
friends = ['nobody', 'myself', 'computer', 'phone']

print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())

# 3-2 Greetings to print each person's name in a list

friends = ['nobody', 'myself', 'computer', 'phone']

print(f"Hey {friends[0].title()}! Welcome to my beautiful world of paradise!")
print(f"Hey {friends[1].title()}! Welcome to my beautiful world of paradise!")
print(f"Hey {friends[2].title()}! Welcome to my beautiful world of paradise!")
print(f"Hey {friends[3].title()}! Welcome to my beautiful world of paradise!")

# 3-3 My own list of my favorite transportation method
vehicles = ['electric skateboard', 'tesla model 3', 'gas car']

print(f"My favorite toy transporation is my {vehicles[0]}. It is so fun to ride around!")
print(f"My dream car is a {vehicles[1].title()}. Electric is the future!")
print(f"A {vehicles[2]} is disgusting. It is time to move on!")

# 3-4 Guest list to invite people to dinner

## Invite these people to the party!
guests = ['Bill Gates', 'Elon Musk', 'Lisa Su']

## Time to send invites!
print(f"The man who makes about $114 per second and donates billions to philanthropic causes! Who doesn't {guests[0].title()} at my dinner?")
print(f"Is {guests[1].title()} Iron Man in disguise? Come to my dinner party!")
print(f"Please tell me your secrets to be named one of world's best CEOs and to lead AMD back in the computing market against competition. {guests[2].title()}. Dinner?")

# 3-5 Changing the guest list
## Someone could not make it to dinner. Modify the list, replace with someone new and print out who could not make dinner.
busy_man = 'Elon Musk'
guests.remove(busy_man)
guests.append('corgi puppies')

print(f'{busy_man} is too busy saving the world! He can not make it to dinner.')
print(f'At least my new guest of {guests[-1]} could make it! {guests[0]} and {guests[1]} are still arriving for dinner.')

# 3-6 Invite more guests to the party since we found a bigger dinner table.
print('Luckily, we found a bigger dinner table to invite more guests!')

guests.insert(0, 'huskies')
guests.insert(2, 'Jeff Bezos')
guests.append('ghosts')
print(f'Our new invited guests, {guests[0]}, {guests[2]}, and {guests[-1]} to dinner. Luckily, Bill Gates and Lisa Su are still going.')

# 3-7 Shrinking the guest list because the table is now broken and only space left is for two guests. Finally, delete the two people left to end up with an empty list.
print('Sadly, my new table is broken and can now only invite two people.')
print(f'{guests.pop().title()}. I am sorry, I can no longer invite you to dinner.')
print(f'{guests.pop().title()}. I am sorry, I can no longer invite you to dinner.')
print(f'{guests.pop().title()}. I am sorry, I can no longer invite you to dinner.')
print(f'{guests.pop().title()}. I am sorry, I can no longer invite you to dinner.')

print(f'Congrats to {guests[0]} and {guests[1]}! You two are the only ones still invited to the dinner.')
del guests[0]
del guests[0]
print(guests)


