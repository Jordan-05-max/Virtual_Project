# English reading
import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
link = "D:\Personal Development & Business Audio-E books\L'art de négocier avec la méthode Harvard.pdf"
f = open(link, "rb")
pdf = PyPDF2.PdfReader(f)
pages = len(pdf.pages)
print(pages)
print("type: ", type(pages))


speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.say("Hello Jordan")
for i in range(1, pages+1):
    page = pdf.pages[i-1]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()