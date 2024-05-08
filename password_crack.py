# from pathlib import path
import time

start = time.process_time()
lien = "C:/Users/jorda/Downloads/francais.txt"


def find_password(correct_psw: str):
    """

    :type correct_psw: object
    """
    with open(lien, "r") as word_list:
        words = word_list.read().split("\n")

        try_number = 1
        for word in words:
            print(word)
            if word == correct_psw:
                print(f"connexion réussi, ça a pris: {start} seconde")
                print(try_number)
                return correct_psw


guess_psw = input("Enter psw: ")

find_password(guess_psw)
