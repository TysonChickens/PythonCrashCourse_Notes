# 5-1.2 Conditional Tests: 5 True and 5 False statements.
favorite_food = 'bacon'
print(f"Does your favorite food == 'bacon'? I think it is True.")
print(favorite_food == 'bacon')
print("I don't like that food.")
print(favorite_food == 'chicken')

age_0 = 25
age_1 = 17
print("\nI believe you are legal age limit for drinking alcohol.")
print(age_0 >= 21)
print("Are you both legal drinking age for alcohol? It doesn't look like it.")
print(age_0 >= 21 and age_1 >= 21)

job = True
print("\nIt looks like you are currently working.")
print(job == True)
print("Do you have a job? It doesn't look like it.")
print(job != True)

vote_age = 18
print("\nIt is time to vote! The age is 18 years or older.")
print(vote_age >= 18)
print("age_1 is not old enough to vote. Therefore, False and can not vote.")
print(vote_age <= age_1)

phone_brand = ['samsung', 'apple', 'huawei', 'oneplus']
my_phone = 'samsung'
print("\nI have a popular smartphone brand!")
print('samsung' in phone_brand)
print("Do I have a popular phone? I use a Sony phone")
print('sony' in phone_brand)



