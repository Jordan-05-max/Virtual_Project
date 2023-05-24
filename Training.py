"""A company has a minimum and maximum limit of the quantity of products to be ordered. Allow the user to order from
the company product list ( create a list of any ten products).
Apply proper constraints if user orders more than the quantity available with the company.
Based on the quantity generate the customer bill"""

import time

obj = time.gmtime()
epoch = time.asctime(obj)

list1 = ["Water", "Papaye", "Mangue", "Orange", "Banana", "Pomme", "Tomate", "Carotte", "Pastèque", "Ananas"]
fruits = {'Water': 20, 'Papaye': 30, 'Mangue': 25, 'Orange': 35, 'Banana': 40, 'Pomme': 50, 'Tomate': 80, 'Carotte': 60,
          'Pastèque': 70, 'Ananas': 90}
length = len(list1)+1
Name = input("Enter your name: ")


print("Welcome! " + Name + "\nWhat do you wish?")
Min_quan = 1
Max_quan = 100

for list1_index, list1_name in enumerate(list1):
    print("{} - {}".format((list1_index + 1), list1_name))


print("\n")
# si le choix n'est pas entre 1 et long ça veut dire le numéro
x = int(input("Enter Your Order number: "))

if x in range(1, length):
    index = x-1
    y = list1[index]
    p = fruits.get(y)
else:
    print("Choice out of range. Valid range is  {} to {}".format(1,length-1))
    exit()

if x in list1 and x in fruits:

    quantity = abs(int(input("Enter the quantity: ")))
    if Max_quan >= quantity >= Min_quan:
        print("Available")

        def bill():
            print("Name: " + Name)
            line = "=" * 2 * len(Name)
            print(line)
            print("Product ordered: " + y)
            line1 = "=" * 4 * len(y)
            print(line1)
            print("Quantity ordered: ", quantity)
            line2 = "=" * 10 * 2
            print(line2)
            print("Price: ", p)
            print(line2)
            print("Total Amount: ", p * quantity)
            print(line2)
            print("Order date:", epoch)
            print(line2)

    elif quantity != Min_quan or quantity != Max_quan:
        print("Quantity out of range")
        print("The quantity available is: ", Max_quan)
        exit()

else:
    print("Sorry!! Product out of Stock")
    exit()


print("\n")
bill()
