import PyPDF2
import pyttsx3
from pyttsx3 import engine

link = "D:/Personal Development & Business Audio-E books/L'art de négocier avec la méthode Harvard.pdf"
file = open(link, "rb")
pdf_read = PyPDF2.PdfReader(file)
pages = len(pdf_read.pages)
speaker = pyttsx3.init()

def read(texts: str):
    """
    sets the voice in French and reads the value stored in parameter texts
    :param texts: stores string value that passes through the function

    """

    speaker.setProperty('rate', 150)
    fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
    speaker.setProperty('voices', fr_voice_id)
    speaker.say(texts)
    speaker.runAndWait()
    return speaker.say(texts)

for i in range(1, pages+1):
    pdf = pdf_read.pages[i-1]
    read_pdf = pdf.extract_text()
    print(f"page:{i} {read_pdf}")
    read(f"page {i} {read_pdf}")
    speaker.save_to_file(read_pdf, "L'art de négocier avec la méthode Harvard.wav")
