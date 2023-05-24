list1 = ["Water", "Papaye", "Mangue", "Orange", "Banana", "Pomme", "Tomate", "Carotte", "Pastèque", "Ananas"]
fruits = {'Water': 20, 'Papaye': 30, 'Mangue': 35, 'Orange': 25, 'Banana': 40, 'Pomme': 50, 'Tomate': 60, 'Carotte': 80,
          'Pastèque': 70, 'Ananas': 90}
desired_order = []
for list1_index, list1_name in enumerate(list1):
    print("{} - {}".format((list1_index + 1), list1_name))
print("\n")

x = list1[int(input("Enter Your Order number: "))-1]
p = fruits.get(x)
print(x, "\n", p)
command = input("Do you want something else? y = yes, n = no \n")
while command not in ["y", "n","Y","N"]:
        command = input("Do You want to play again? y = yes, n = no \n")
        if command == "y":
            list1 = ["Water", "Papaye", "Mangue", "Orange", "Banana", "Pomme", "Tomate", "Carotte", "Pastèque", "Ananas"]
            fruits = {'Water': 20, 'Papaye': 30, 'Mangue': 35, 'Orange': 25, 'Banana': 40, 'Pomme': 50, 'Tomate': 60,
                      'Carotte': 80, 'Pastèque': 70, 'Ananas': 90}

            for list1_index, list1_name in enumerate(list1):
                print("{} - {}".format((list1_index + 1), list1_name))

            z = list1[int(input("Enter Your Order 2 number: "))-1]
            p = fruits.get(z)



        elif command == "n":
            print("Thanks For Playing! We expect you back again!")
            exit()

desired_order.append(x, z)
# print(type(x))
print(desired_order)
