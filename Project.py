import pyttsx3
from pyttsx3 import Engine

from pywhatkit import sendwhatmsg_instantly, system, sendwhatmsg

# initialising the whatsapp system
system()

speaker: Engine = pyttsx3.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.say("Hello Jordan")
speaker.runAndWait()


# Functions

def display_contact_list(contacts, contact_numbers):
    desired_contacts = []
    print("Choose the name of your contact here: ")

    speaker.say(" Choose the name of your contact here ")
    speaker.runAndWait()
    print("========================================")

    contact_list = contacts.keys()
    for contact_index, contact_name in enumerate(contact_list):
        print("{} - {}".format((contact_index + 1), contact_name))

    contact_choices = input("Contact Choice : ").split()

    for contact_index in contact_choices:
        print(contact_index)
        if contact_index.isdigit():

            contact_index = int(contact_index)
            if 1 <= contact_index <= len(contacts):
                phone_number = contact_numbers.get(contact_index)
                desired_contacts.append(phone_number)

            else:
                print("Invalid Option")
                continue
        else:
            raise Exception("Incorrect Input")
    return desired_contacts


def display_message_type():
    print("Please select the message type you want : \n")

    speaker.say("Please select the message type you want ")
    speaker.runAndWait()
    print("1 - Instantaneous Message  \n")
    print("2 - Planned Message\n")
    choice = input("Message type : ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 2:
            return choice
        else:
            print("Invalid Option")
            exit()
    else:
        raise Exception("Incorrect Input")


def getMessage():
    speaker.say("Please enter your message")
    speaker.runAndWait()
    message = input("Type your message: ")

    speaker.say("The message entered is: " + message)
    speaker.runAndWait()
    return message


def sendProgrammedDetails():
    try:
        hours = int(input("Please provide the hours: "))
        minutes = int(input("Please provide the minutes: "))
        program_details = {
            "hours": hours,
            "minutes": minutes
        }
        return program_details
    except:
        raise Exception(" Wrong Input")


phone_dict = {"Jordan": "+22962747600", "Mjd": "+2348140257660", "Zita": "+918360222648", "Johnstone": "+263777128928",
              "Donald Idohou": "+22961876476", "Papa": "+22997984266", "Vishnu": "+919591590281",
              "Saphir": "+23793195666", "Rufin": "+22990166164", "Vikanshi": "+919012677280", "Casimir": "+918968793478"
    , "Tonton Rufin": "+22967601588", "Romualdine": "+22951864306", "Mr François": "+22997444472"}

phone_dict2 = {1: "+22962747600", 2: "+2348140257660", 3: "+918360222648", 4: "+263777128928", 5: "+22961876476",
               6: "+22997984266", 7: "+919591590281", 8: "+23793195666", 9: "+22990166164", 10: "+919012677280",
               11: "+918968793478", 12: "+22967601588", 13: "+22951864306", 14: "+22997444472"}

desired_number_list = display_contact_list(phone_dict, phone_dict2)
message_type = display_message_type()
desired_message = getMessage()

print(desired_number_list)
print(desired_message)
print(message_type)

match message_type:
    case 1:
        try:
            for desired_number in desired_number_list:
                sendwhatmsg_instantly(desired_number, desired_message, 15, True, 7)
                print("Successfully Sent!")
        except:
            print("Error while sending ")
    case 2:
        try:
            planned_details = sendProgrammedDetails()
            for desired_number in desired_number_list:
                sendwhatmsg(desired_number, desired_message, planned_details.get("hours"),
                            planned_details.get("minutes"), 15, True, 10)
                print("Successfully Sent !")

                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say("Message Successfully Sent!")
                engine.runAndWait()
        except:
            print("Error while sending message")

            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say("Error while sending message")
            engine.runAndWait()

speaker.stop()
"""Bonjour Tonton! Comment allez-vous?"""
