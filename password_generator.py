import random
import string
from datetime import datetime
from password_Db import dbpassword

db = dbpassword("psw.db")

name = input("Enter your name: ")
purpose = input("Enter the purpose: ")
length = int(input("Input length: "))


def generate_password(length):
    caractere = string.ascii_letters + string.digits + string.punctuation
    passwords = ''.join(random.choice(caractere) for _ in range(length))
    print(f"password: {passwords}")
    return passwords


def Time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # print(f"Current Time = {current_time}")
    return current_time

def Date():
    import datetime
    current_date = datetime.date.today().strftime("%d/%m/%Y")
    # print(f"Current Date = {current_date}")
    return current_date
def add():
    db.inserts(name, purpose, psw, length, Date(), Time())


Time()
Date()
psw = generate_password(length)
add()

