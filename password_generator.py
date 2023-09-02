import random
import string
from datetime import datetime
from password_Db import dbpassword

db = dbpassword("psw.db")

name = input("Enter your name: ")
purpose = input("Enter the purpose: ")
length = int(input("Input length: "))


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


def add() -> None:
    """
    Connected to a database, it adds details into psw database
    :return: none
    """
    db.inserts(name, purpose, psw, length, dates(), timez())


# timez()
# dates()
psw = generate_password(length)
add()
