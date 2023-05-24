# Lecture Française
import pyttsx3
import PyPDF2

# from PyPDF2 import PdfReader
link = "D:/Personal Development & Business Audio-E books/L'art de négocier avec la méthode Harvard.pdf"
f = open(link, "rb")
pdf = PyPDF2.PdfReader(f)
pages = len(pdf.pages)
print(pages)
print("type: ", type(pages))

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
speaker.setProperty('voice', fr_voice_id)
speaker.say("Mes salutations chers auditeurs, auditrices")
speaker.say("Cette lecture se fera en Français")
speaker.say("Bonne Lecture!!")
for i in range(1, pages + 1):
    page = pdf.pages[i - 1]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
