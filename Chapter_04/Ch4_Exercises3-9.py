# 4-3: Counting to Twenty with a for loop to print the numbers from 1 to 20, inclusive.
twenty_num = []
for value in range(1, 11):
    twenty_num.append(value)
    print(value)

# 4-4: One Million numbers from one to one million.
# 4-5: Summing a Million from one to one million list. Use min() and max() to verify start and end numbers.
one_million = []
for value in range(1, 1000001):
    one_million.append(value)

print(min(one_million))
print(max(one_million))
print(sum(one_million))

# 4-6: Odd Numbers using the third argument of the range() function to make a list from 1 to 20.
odd_num = []
for value in range(1, 21, 2):
    odd_num.append(value)
    print(value)

# 4-7: Make a list of the mulitples of 3 from 3 to 30.
multiples_three = []
for value in range(3, 31, 3):
    multiples_three.append(value)
    print(value)

# 4-8: Cubes of numbers starting from 1 through 10.
cubes = []
for value in range(1, 11):
    value **= 3
    cubes.append(value)
    print(value)

# 4-9: Create a list of numbers of the first 10 cubes using list comprehension.
cubes = [value**3 for value in range(1, 11)]
print(cubes)