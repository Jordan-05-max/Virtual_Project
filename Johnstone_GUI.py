import tkinter
from tkinter import ttk, StringVar
import pywhatkit as wh
root=tkinter.Tk()
root.title("Instamsg")
# setting the windows size
root.geometry("600x400")
root.config(background="#010101")
# declaring string variable
# for storing name and password
msg = StringVar()
contact = StringVar()
entries_frame = tkinter.Frame(root, bg="#010101")
entries_frame.pack(side=tkinter.TOP, fill=tkinter.X)
title = tkinter.Label(entries_frame, text="Instamsg", font=("Baskervville", 18, "bold"),
                      bg="#323FB4", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
lblcontact= tkinter.Label(entries_frame, text= "contact List:", font=("Baskervville", 18, "bold"),
                      bg="#323FB4", fg="white")


lblmsg = tkinter.Label(entries_frame, text="Message:", font=("Baskervville", 16), bg="#323FB4", fg="white")
lblmsg.grid(column=0, row=1, pady=10, padx=10, sticky="w")
txtmsg = tkinter.Entry(entries_frame, textvariable=msg, font=("Baskervville", 16), width=30)
txtmsg.grid(column=1, row=1, padx=0, pady=10, sticky="w")
lblcontact.grid(column=0, row=4, padx=10, pady=10, sticky="w")
def display_contact_list(contacts,contact_numbers):
    desired_contacts=[]
    print("Choose the name of your contact here: ")
    print("========================================")
    contact_list = contacts.keys()
    for contact_index, contact_name in enumerate(contact_list):
        print("{} - {}".format((contact_index + 1), contact_name))

    contact_choices = input("Contact Choice : ").split()

    for contact_index in contact_choices:
        print(contact_index)
        if contact_index.isdigit():

            contact_index = int(contact_index)
            if contact_index >= 1 and contact_index <= len(contacts):
                phone_number = contact_numbers.get(contact_index)
                desired_contacts.append(phone_number)

            else:
                print("Invalid Option")
                continue
        else:
            raise Exception("Incorrect Input")
    return desired_contacts
combocontact=ttk.Combobox(entries_frame, textvariable=contact, font=("Baskervville", 14), width=31, state="readonly")
combocontact['values'] = (display_contact_list())
combocontact.grid(column=1, row=4, padx=0, pady=10, sticky="w")
"""def display_contact_list(contacts,contact_numbers):
    desired_contacts=[]
    print("Choose the name of your contact here: ")
    print("========================================")
    contact_list = contacts.keys()
    for contact_index, contact_name in enumerate(contact_list):
        print("{} - {}".format((contact_index + 1), contact_name))

    contact_choices = input("Contact Choice : ").split()

    for contact_index in contact_choices:
        print(contact_index)
        if contact_index.isdigit():

            contact_index = int(contact_index)
            if contact_index >= 1 and contact_index <= len(contacts):
                phone_number = contact_numbers.get(contact_index)
                desired_contacts.append(phone_number)

            else:
                print("Invalid Option")
                continue
        else:
            raise Exception("Incorrect Input")
    return desired_contacts"""
def submit():
    msg=txtmsg.get()
    contact = combocontact.get()
    print("Please select your contact : " + contact)
    print("Enter your message : " + msg)



btn_frame = tkinter.Frame(entries_frame, bg="#323FB4")
btn_frame.grid(column=0, row=7, columnspan=6, padx=10, pady=10, sticky="w")
tkinter.Button(btn_frame, command=submit, text="submit", width=15, font=("Baskervville", 16, "bold"),
               fg="white", bg="#16A085", bd=0).grid(column=0, row=0)


root.mainloop()

