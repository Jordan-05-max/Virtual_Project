import PyPDF2
import pyttsx3
from tkinter import Tk
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename


def display_menu():
    """
        Displays a menu for password generation
        :return: integer
    """
    print("What do you wish to do?: \n")
    print("1-Reading in French\n")
    print("2-Reading in English\n")
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


#
def french(texts: str):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
    speaker.setProperty('voices', fr_voice_id)
    for i in range(1, pages + 1):
        page = pdf.pages[i - 1]
        text = page.extract_text()
        print(f"page:{i} {text}\n")
        speaker.say(text)
        speaker.runAndWait()
    return speaker.say(texts)


#
def english(texts: str):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    for i in range(1, pages + 1):
        page = pdf.pages[i - 1]
        text = page.extract_text()
        print(f"page:{i} {text}\n")
        speaker.say(text)
        speaker.runAndWait()
    return speaker.say(texts)


def prompt() -> str:
    Tk().withdraw()
    file_link = askopenfilename()
    return file_link


get_file = prompt()

menu = display_menu()

match menu:
    case 1:
        try:
            # print(file_link)
            file_book = open(get_file, "rb")
            pdf = PyPDF2.PdfReader(file_book)
            pages = len(pdf.pages)
            french(file_book)
        except:
            print("Mismatch\nInvalid option")
    case 2:
        try:

            # print(file_link)
            file_book = open(get_file, "rb")
            pdf = PyPDF2.PdfReader(file_book)
            pages = len(pdf.pages)
            english(file_book)
        except:
            print("Mismatch\nTry again!!")
