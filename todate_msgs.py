import datetime
# from tkinter import Tk
import openpyxl as xl
from tkinter.filedialog import askopenfilename


def getfile():
	# Tk().withdraw()
	xl_file = askopenfilename()
	return xl_file


def tuday():
	"""
	This function helps in getting today's date
	:return: current date
	"""
	current_date = datetime.date.today().strftime("%d/%m")
	print(f"Current Date = {current_date}")
	return current_date


file = getfile()
print(f'file_path: {file}')

wb = xl.load_workbook(file)
# ws = wb.active
sht = wb['Feuil1']
for row in sht:
	for cell in row:
		if cell.coordinate[0] == 'B':
			values = sht[cell.coordinate].value
			print(f'value: {values}')
