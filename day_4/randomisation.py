#Random Numnber Generator

import random   

random_integer = random.randint(1, 10)
random_float = random.random()
random_float = random_float * 5

print(random_integer)
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")


#Heads or Tails

import random
random_side = random.random()
if random_side<0.5:
    print("Heads")
else:
    print("Tails")  


#Input into array

names = input("Enter names separated by a comma and a space: ").split(", ")
import random
num_items = len(names)
random_index = random.randint(0, num_items - 1)
person_who_is_going_to_buy = names[random_index]
print(f"{person_who_is_going_to_buy} is going to buy the meal today!")

#List 

dirty_dozen = [
    "Strawberries",
    "Spinach",
    "Kale",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
    "Tomatoes",
    "Celery",
    "Potatoes"
]   
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozens = [fruits, vegetables]

print("Dirty Dozen Fruits:")
for fruit in dirty_dozens[0]:
    print(fruit)    

print("\nDirty Dozen Vegetables:")
for vegetable in dirty_dozens[1]:
    print(vegetable)

    

