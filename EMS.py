from tkinter import *

import tkinter
from tkinter import messagebox
from tkinter import ttk, StringVar

import country_list

from Database import Database

# connecting database and setting layout for GUI
db = Database("MyEmployees.db")
root = tkinter.Tk()
root.title("Employee Recruitment System")
root.geometry("1366x768")
root.config(bg="#323FB4")
# root.config(background="#2C3E50")
root.state("zoomed")
# style = ttk.Style()
# style.theme_use('clam')


name = StringVar()
age = StringVar()
dob = StringVar()
email = StringVar()
gender = StringVar()
contact = StringVar()
company = StringVar()
job = StringVar()
CGPA = StringVar()
address = StringVar()
country = StringVar()

# Entry frame

# text entry
entries_frame = tkinter.Frame(root, bg="#323FB4")
entries_frame.pack(side=tkinter.TOP, fill=tkinter.X)
title = tkinter.Label(entries_frame, text="Employee Recruitment System", font=("Times New Roman", 18, "bold"),
                      bg="#323FB4", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")

# Name entry
lblName = tkinter.Label(entries_frame, text="Name:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblName.grid(column=0, row=1, pady=10, padx=10, sticky="w")
txtName = tkinter.Entry(entries_frame, textvariable=name, font=("Times New Roman", 16), width=28)
txtName.grid(column=1, row=1, padx=0, pady=10, sticky="w")

# Age entry
lblAge = tkinter.Label(entries_frame, text="Age:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblAge.grid(column=0, row=2, padx=10, pady=10, sticky="w")
txtAge = tkinter.Entry(entries_frame, textvariable=age, font=("Times New Roman", 16), width=28)
txtAge.grid(column=1, row=2, padx=0, pady=10, sticky="w")

# DOB entry
lblDOB = tkinter.Label(entries_frame, text="DOB:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblDOB.grid(column=0, row=3, padx=10, pady=10, sticky="w")
txtDOB = ttk.Entry(entries_frame, textvariable=dob, font=("Times New Roman", 16), width=28)
txtDOB.grid(column=1, row=3, padx=0, pady=10, sticky="w")

# Email entry
lblEmail = tkinter.Label(entries_frame, text="Email:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblEmail.grid(column=2, row=1, padx=10, pady=10, sticky="w")
txtEmail = tkinter.Entry(entries_frame, textvariable=email, font=("Times New Roman", 16), width=28)
txtEmail.grid(column=3, row=1, padx=0, pady=10, sticky="w")

# Gender entry
lblGender = tkinter.Label(entries_frame, text="Gender:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblGender.grid(column=0, row=4, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, textvariable=gender, font=("Times New Roman", 14), width=28, state="readonly")
comboGender['values'] = (" ", "Male", "Female", "Other")
comboGender.grid(column=1, row=4, padx=0, pady=10, sticky="w")

# Contact entry
lblContact = tkinter.Label(entries_frame, text="Contact:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblContact.grid(column=2, row=2, padx=10, pady=10, sticky="w")
txtContact = tkinter.Entry(entries_frame, textvariable=contact, font=("Times New Roman", 16), width=28)
txtContact.grid(column=3, row=2, padx=0, pady=10, sticky="w")

# Company entry
lblCompany = tkinter.Label(entries_frame, text="Select Company:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblCompany.grid(column=2, row=3, padx=10, pady=10, sticky="w")
comboCompany = ttk.Combobox(entries_frame, textvariable=company, font=("Times New Roman", 16), width=28, state="readonly")
comboCompany['values'] = (
" ", "Microsoft", "Omiraï", "Amazon", "Facebook", "Google", "IBM", "Cognizant", "Bosch", "Apple", "Samsung")
comboCompany.grid(column=3, row=3, padx=0, pady=10, sticky="w")

# Job entry
lblJob = tkinter.Label(entries_frame, text="Select Job:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblJob.grid(column=2, row=4, padx=5, pady=10, sticky="w")
comboJob = ttk.Combobox(entries_frame, textvariable=job, font=("Times New Roman", 16), width=28, state="readonly")
comboJob['values'] = (
" ", "Computer Programmer", "Data Analyst", "Support Specialist", "IoT Architect", "Software Designer", "Software Engineer")
comboJob.grid(column=3, row=4, padx=0, pady=10, sticky="w")

# CGPA entry
lblCGPA = tkinter.Label(entries_frame, text="CGPA:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblCGPA.grid(column=4, row=1, padx=5, pady=10, sticky="w")
comboCGPA = ttk.Combobox(entries_frame, textvariable=CGPA, font=("Times New Roman", 16), width=28, state="readonly")
comboCGPA['values'] = (" ", "5.0", "6.0", "7.0", "8.0", "9.0")
comboCGPA.grid(column=5, row=1, padx=0, pady=10, sticky="w")

# country entry
lblCountry = tkinter.Label(entries_frame, text="Country:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblCountry.grid(column=4, row=2, padx=0, pady=0, sticky="w")
comboCountry = ttk.Combobox(entries_frame, textvariable=country, font=("Times New Roman", 16), width=28, state="write")
comboCountry['values'] = country_list.countries_for_language(lang="en", encoding="utf8")
comboCountry.grid(column=5, row=2, padx=0, pady=0, sticky="w")

# Address entry
lblAddress = tkinter.Label(entries_frame, text="Address:", font=("Times New Roman", 16), bg="#323FB4", fg="white")
lblAddress.grid(column=0, row=5, padx=10, pady=10, sticky="nw")
txtAddress = tkinter.Text(entries_frame, width=88, height=2, font=("Times New Roman", 16))
txtAddress.grid(column=0, row=6, columnspan=6, padx=0, pady=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    # print(row)
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    company.set(row[7])
    job.set(row[8])
    CGPA.set(row[9])
    country.set(row[10])
    txtAddress.delete(1.0, tkinter.END)
    txtAddress.insert(tkinter.END, row[11])


def displayAll():
    tv.delete(*tv.get_children())
    for rows in db.fetch():
        tv.insert("", tkinter.END, values=rows)


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDOB.get() == "" or txtEmail.get() == "" or comboGender.get() == "" \
            or txtContact.get() == "" or comboCompany.get() == "" or comboJob.get() == "" or comboCGPA.get() == "" \
            or comboCountry.get() == "" or txtAddress.get(1.0, tkinter.END) == "":
        messagebox.showerror("Error in input", "Please fill all details")
        return
    db.insert(txtName.get(), txtAge.get(), txtDOB.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              comboCompany.get(),
              comboJob.get(), comboCGPA.get(), comboCountry.get(), txtAddress.get(1.0, tkinter.END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()


def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDOB.get() == "" or txtEmail.get() == "" or comboGender.get() == "" \
            or txtContact.get() == "" or comboCompany.get() == "" or comboJob.get() == "" or comboCGPA.get() == "" \
            or comboCountry.get() == "" or txtAddress.get(1.0, tkinter.END) == "":
        messagebox.showerror("Error in input", "Please fill all details")
        return
    db.update(row[0], txtName.get(), txtAge.get(), txtDOB.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              comboCompany.get(),
              comboJob.get(), comboCGPA.get(), comboCountry.get(), txtAddress.get(1.0, tkinter.END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    displayAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()


def clearAll():
    name.set("")
    age.set("")
    dob.set("")
    email.set("")
    gender.set("")
    contact.set("")
    company.set("")
    job.set("")
    CGPA.set("")
    country.set("")
    txtAddress.delete(1.0, tkinter.END)


# Buttons
btn_frame = tkinter.Frame(entries_frame, bg="#323FB4")
btn_frame.grid(column=0, row=7, columnspan=6, padx=10, pady=10, sticky="w")
tkinter.Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Baskervville", 16, "bold"),
               fg="white", bg="#16A085", bd=0).grid(column=0, row=0)

tkinter.Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Baskervville", 16, "bold"),
               fg="white", bg="#0000FF", bd=0).grid(column=1, row=0, padx=10)

tkinter.Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Baskervville", 16, "bold"),
               fg="white", bg="#FF0000", bd=0).grid(column=2, row=0, padx=10)

tkinter.Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Baskervville", 16, "bold"),
               fg="black", bg="#FFFF00", bd=0).grid(column=3, row=0, padx=10)

# Table Frame

# Database frame

tree_frame = tkinter.Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1368, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Times New Roman', 18), rowheight=50)
# Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 18))

# Modify the font of the headings

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), style="mystyle.Treeview", selectmode ='browse')
tv.heading("1", text="ID")
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.heading("4", text="D.O.B")
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.heading("7", text="Contact")
tv.heading("8", text="Company")
tv.heading("9", text="Job")
tv.heading("10", text="CGPA")
tv.heading("11", text="Country")
tv.heading("12", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)

tv.pack(fill=tkinter.X)

displayAll()
root.mainloop()

