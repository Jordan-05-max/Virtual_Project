"""Lecture Française"""

import pyttsx3
import PyPDF2

# from PyPDF2 import PdfReader
link = "D:/Personal Development & Business Audio-E books/L'art de négocier avec la méthode Harvard.pdf"
file = open(link, "rb")
pdf = PyPDF2.PdfReader(file)
pages = len(pdf.pages)
#speaker = pyttsx3.init()

def read(texts: str):
    """
    sets the voice in French and reads the value stored in parameter texts
    :param texts: stores string value that passes through the function

    """
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
    speaker.setProperty('voices', fr_voice_id)
    speaker.say(texts)
    speaker.runAndWait()
    # return speaker.say(texts)


for i in range(1, pages + 1):
    page = pdf.pages[i - 1]
    text = page.extract_text()
    read(text)
speaker.stop()