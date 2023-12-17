import random
import string
from datetime import datetime
from password_Db import dbpassword

db = dbpassword("psw.db")




def generate_password(Length: int) -> str:
    """
    Generates strong password with a specific length
    :param Length: Integer value given by the user
    :return: password
    """
    caractere = string.ascii_letters + string.digits + string.punctuation
    passwords = ''.join(random.choice(caractere) for _ in range(Length))
    print(f"password: {passwords}")
    return passwords


def timez() -> str:
    """
    Gives exact time of creation of password in format HH:MM:SS
    :return: current time
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print(f"Current Time = {current_time}")
    return current_time


def dates() -> str:
    """
    Gives date on which password is being generated in format DD/MM/YYYY
    :return: current date
    """
    import datetime
    current_date = datetime.date.today().strftime("%d/%m/%Y")
    # print(f"Current Date = {current_date}")
    return current_date


def add_psw() -> None:
    """
     Connects to psw database, it adds details into psw database
     :return: none
     """
    db.inserts(name, purpose, psw, length, dates(), timez())


def get_psw() -> None:
    """
    Fetches data from database,and display data saved into psw database
    :return: None
    """
    db.fetch()


def delete_psw(Purpose) -> None:
     """
     Deletes latest generated password from database
     :param Purpose: a string primary key
     :return: None
     """
     db.remove(Purpose)


def display_menu() -> int:
    """
    Displays a menu for password generation
    :return: integer
    """
    print("What do you wish to do?: \n")
    print("1-Generate password\n")
    print("2-Display database data \n")
    choice = input("Please enter your numbers wish: ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 2:
            return choice
        else:
            print("Invalid Option")
            exit()
    else:
        raise Exception("Incorrect Input")


# timez()
# dates()

def saving():
    """
    Menu to save generated password or not
    :return: choix
    """
    print("Do you want to save the password?\n")
    print("1-Yes\n")
    print("2-No")
    choix = int(input("Your choice please: "))
    if 1 <= choix <= 2:
        return choix
    else:
        print("Invalid option")
        exit()


menu: int = display_menu()

match menu:
    case 1:
        try:
            name = input("Enter your name: ")
            purpose = input("Enter the purpose: ")
            length = int(input("Input length: "))

            psw = generate_password(length)
            saving_opt = saving()

            match saving_opt:
                case 1:
                    try:
                        add_psw()
                        print("Successfully saved into database")
                    except:
                        print("An error occurred")

                case 2:
                    try:
                        delete_psw(purpose)
                        print("Password unsaved in database")
                        # exit()
                    except:
                        print("An error occurred while deleting")

        except:
            print("Mismatch!\nNot able to save")
    case 2:
        try:
            get_psw()
            print("Password list printed")
        except:
            print("Mismatch!\nNot able to get database")
