"""Q4. Develop following functions in Python
AddMe() – the purpose of this function is to get country name and its capital from user and develop a database to store
this country, capital pairs. Use suitable data structure for this task.
FindMe(input) – the purpose of this function is to take country name as input and return its capital.
DelMe(input) – the purpose of this function is to delete entry on the basis of input country name.(10 MARKS)"""

# Creating a dictionary to store inputted values
"""worldCity = {}

country = input("Enter the country name: ")
capital = input("Enter capital city: ")



def AddMe():
    worldCity = {country.title(): capital}
    worldCity[country] = capital
    worldCity.update()  # The update() method inserts the specified items to the dictionary. The specified items can be a dictionary, or an iterable object with key value pairs.
    # print(worldCity)
    return worldCity


#AddMe()


def FindMe(country):

    
       # :type country: str(key)
    
    print(worldCity)
    print(country)
    city = worldCity.get(country, "NA")
    print(city)
    return city


#FindMe(country)


def DelMe(country):
    worldCity.pop(country)

def quit():
    exit()

#DelMe(country)

def
def choices():
    while True:
        print("Make choice :")
        print("1 for Adding country and capital city")
        print("2 for Finding capital")
        print("3 for Deleting entry")
        print("4 Quit")
        choice = int(input())

        if choice == 1:
            AddMe()

        elif choice == 2:
            key = input("country: ")
            FindMe(key)
        elif choice == 3:
            DelMe()
        elif choice == 4:
            quit()
choices()



"""
"""Q4. Develop following functions in Python
AddMe() – the purpose of this function is to get country name and its capital from user and develop a database to store
this country, capital pairs. Use suitable data structure for this task.
FindMe(input) – the purpose of this function is to take country name as input and return its capital.
DelMe(input) – the purpose of this function is to delete entry on the basis of input country name.(10 MARKS)"""

# Creating a dictionary to store inputted values
#worldCity = {}

country = input("Enter the country name: ")
capital = input("Enter capital city: ")

worldCity = {country.title(): capital}

def AddMe():

    worldCity[country] = capital
    worldCity.update()  # The update() method inserts the specified items to the dictionary. The specified items can be a dictionary, or an iterable object with key value pairs.
    print(worldCity)
    # return worldCity


AddMe()


def FindMe(country):

    """
    :type country: str(key)
    """

    city = worldCity.get(country)
    print(city)
    return city


FindMe(country)


def DelMe(country):
    worldCity.pop(country)
DelMe(country)