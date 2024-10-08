import time
import pywhatkit
from pywhatkit import sendwhatmsg_instantly, sendwhatmsg, system

import pyttsx3
from pyttsx3 import Engine

import webbrowser as web
import pyautogui


def systems() -> str:
    """
    system() gets the operating system on which app is working
    :return: system name
    """
    sys = system()
    print(sys)
    return sys


def talk(text: str) -> object:
    """
    talk() read the value of the parameter that is parsed into the function
    :param text: str
    :return: speaker.say(param)
    """
    speaker: Engine = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
    return speaker.say(text)


def show_contact_list(contacts, contact_numbers):
    desired_contacts = []
    print("Choose the name of your contact here: ")
    print("========================================")

    contact_list = contacts.keys()
    for contact_index, contact_name in enumerate(contact_list):
        # print("{} - {}".format((contact_index + 1), contact_name))
        print(f"{contact_index + 1} - {contact_name}")
    contact_choices = input("Contact Choice : ").split()

    for contact_index in contact_choices:
        print(contact_index)
        if contact_index.isdigit():
            contact_index = int(contact_index)
            if 1 <= contact_index <= len(contacts):
                phone_number = contact_numbers.get(contact_index)
                desired_contacts.append(phone_number)
                print(desired_contacts)

            else:
                print("Invalid Option")
                continue
        else:
            raise Exception("Incorrect Input")

    return desired_contacts


def show_message_type():
    print("Please select the message type you want : \n")
    print("1 - Instantaneous Message \n")
    print("2 - Planned Message\n")
    print("3 - Diffusion List\n")
    talk("Please select the message type you want ")
    choice = int(input("Message type : "))
    if 1 <= choice <= 3:
        return choice
    else:
        print("Invalid Option")
        raise Exception("Incorrect Input")


def getMessage():
    message = input("Type your message: ")
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

def get_name(phone_number):
    dict2_list = list(phone_dict2.values())
    index = dict2_list.index(phone_number)
    dict_list = list(phone_dict.keys())
    names = dict_list[index]
    print(names)
    return names


phone_dict = {"Jordan": "+22962747600", "Mjd": "+2348140257660", "Zita": "+918360222648", "Papa": "+22997984266",
              "Saphir": "+23793195666", "Johnstone": "+263777128928", "Idohou": "+22961876476",
              "Vishnu": "+919591590281", "Rufin": "+22990166164", "Vikanshi": "+919012677280", "Dinah": "+22951864306",
              "Casimir": "+916284748460", "Tonton Rufin": "+22967601588", "Mr François": "+22997444472"}

phone_dict2 = {1: "+22962747600", 2: "+2348140257660", 3: "+918360222648", 4: "+22997984266", 5: "+23793195666",
               6: "+263777128928", 7: "+22961876476", 8: "+919591590281", 9: "+22990166164", 10: "+919012677280",
               11: "+22951864306", 12: "+916284748460", 13: "+22967601588", 14: "+22997444472"}
message_type = show_message_type()
# print(message_type)
match message_type:
    case 1:

        try:
            systems()
            desired_number_list = show_contact_list(phone_dict, phone_dict2)
            instant_sends = []
            for desired_number in desired_number_list:
                desired_name = get_name(desired_number)
                desired_message = getMessage()
                instant_sends.append([desired_name, desired_number, desired_message])
            for instant_send in instant_sends:
                pywhatkit.sendwhatmsg_instantly(instant_send[1], instant_send[2], 20, True, 15)
                print("Successfully Sent!")
                talk("Message successfully sent!")
        except:
            print("Error while sending")
            talk("Error while sending")

    case 2:
        try:
            systems()
            desired_number_list = show_contact_list(phone_dict, phone_dict2)
            plans = []
            for desired_number in desired_number_list:
                planned_details = sendProgrammedDetails()
                desired_name = get_name(desired_number)
                desired_message = getMessage()
                plans.append([desired_name, desired_number, list(planned_details.values()), desired_message])
            for plan in plans:
                pywhatkit.sendwhatmsg(plan[1], plan[3], plan[2][0], plan[2][1], 20, True, 10)
                print("Successfully Sent !")
                talk("Message Successfully Sent to!" + plan[0])
        except:
            print("Error while sending message")
            talk("Error while sending message")

    case 3:
        try:
            system()
            # website()
            diffList = show_contact_list(phone_dict, phone_dict2)
            desired_message = getMessage()
            for desired_number in diffList:
                sendwhatmsg_instantly(desired_number, desired_message, 20, True, 7)
                print("Successfully Sent!")
                talk("Message Successfully Sent to the diffusion list")
        except:
            print("Error while sending diffusion message")