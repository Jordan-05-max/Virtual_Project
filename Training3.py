import pyttsx3
import PyPDF2

link = "D:/Personal Development & Business Audio-E books/L'art de négocier avec la méthode Harvard.pdf"
pdf_book = open(link, "rb")
reading_pdf = PyPDF2.PdfFileReader(pdf_book)
pdf_pages = reading_pdf.numPages

pdf_speaker = pyttsx3.init()
choose_page = reading_pdf.getPage(10)
pdf_text = choose_page.extract_text()
pdf_speaker.say(pdf_text)
pdf_speaker.runAndWait()