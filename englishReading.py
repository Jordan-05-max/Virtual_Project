# English reading
import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_link = askopenfilename()
# link = "D:\Personal Development & Business Audio-E books\L'art de négocier avec la méthode Harvard.pdf"
file_book = open(file_link, "rb")
pdf = PyPDF2.PdfReader(file_book)
pages = len(pdf.pages)
print(pages)
print("type: ", type(pages))


def read(texts: str):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)

    for i in range(1, pages+1):
        page = pdf.pages[i-1]
        text = page.extract_text()
        print(f"page:{i} {text}\n")
        speaker.say(text)
        speaker.runAndWait()
    return speaker.say(texts)
# speaker.stop()

read(file_book)