"""A company has a minimum and maximum limit of the quantity of products to be ordered. Allow the user to order from
the company product list ( create a list of any ten products).
Apply proper constraints if user orders more than the quantity available with the company.
Based on the quantity generate the customer bill"""

import time

obj = time.gmtime()
epoch = time.asctime(obj)

"""fruits = {'Water': 20, 'Papaye': 30, 'Mangue': 25, 'Orange': 35, 'Banana': 40, 'Pomme': 50, 'Tomate': 80, 'Carotte': 60,
          'Pastèque': 70, 'Ananas': 90}"""

fruits = [
            {"fruit_name": "Water", "quantity": 100, "price": 20},
            {"fruit_name": "Papaye", "quantity": 100, "price": 30},
            {"fruit_name": "Mangue", "quantity": 100, "price": 25},
            {"fruit_name": "Orange", "quantity": 100, "price": 35},
            {"fruit_name": "Banana", "quantity": 100, "price": 40},
            {"fruit_name": "Pomme", "quantity": 100, "price": 50},
            {"fruit_name": "Tomate", "quantity": 100, "price": 80},
            {"fruit_name": "Carotte", "quantity": 100, "price": 60},
            {"fruit_name": "Pastèque", "quantity": 100, "price": 70},
            {"fruit_name": "Ananas", "quantity": 100, "price": 90}
          ]

# Getting fruits length and list
length = len(fruits) + 1

# Getting fruit names
fruit_names = []
for fruit in fruits:
    fruit_names.append(fruit.get("fruit_name"))

name = input("Enter your name: ")


print("Welcome! " + name + "\nWhat do you wish?")

for counter, fruit_name in enumerate(fruit_names):
    print("{} - {}".format((counter + 1), fruit_name))


print("\n")
# si le choix n'est pas entre 1 et long ça veut dire le numéro
choice = int(input("Enter Your Order number: "))
fruit = ""

if choice in range(1, length):
    index = choice - 1
    #y = fruit_names[index]
    #p = fruits.get(y)
    fruit = fruits[index].get("fruit_name")

else:
    print("Choice out of range. Valid range is  {} to {}".format(1,length-1))
    exit()

print(fruit)
exit()