import time

# import pywp
import pywhatkit
from pywhatkit import sendwhatmsg_instantly, sendwhatmsg, system

import pyttsx3
from pyttsx3 import Engine

# import webbrowser as web
# import pyautogui


# pywhatkit.start_server()
# Functions

#
def systems() -> str:
    """
    systems() gets the operating system on which app is working
    :return: system name
    """
    sys = system()
    print(sys)
    return sys


def website():
    """
    updates the whatsapp website by opening and closing the website
    :return: none
    """
    web.open(f"https://web.whatsapp.com/")
    time.sleep(240)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(20)
    pyautogui.hotkey('alt', 'f4')


def talk(text: str):
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


def display_contact_list(contacts, contact_numbers):
    desired_contacts = []
    print("Choose the name of your contact here: ")
    print("========================================")

    contact_list = contacts.keys()
    for contact_index, contact_name in enumerate(contact_list):
        print("{} - {}".format((contact_index + 1), contact_name))
    talk(" Choose the name of your contact here ")
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
    print("1 - Instantaneous Message\n")
    print("2 - Planned Message\n")
    print("3 - Diffusion List\n")
    talk("Please select the message type you want ")
    choice = input("Message type : ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 3:
            return choice
        else:
            print("Invalid Option")
            exit()
    else:
        raise Exception("Incorrect Input")


def getMessage():
    # talk("Please enter your message")
    # message = input("Type your message: ")
    message = ("\n"
               "    Monsieur/Madame!\n"
               "Nos Salutations les plus distinguées !\n"
               "\n"
               "Nous vous écrivons de Lovely Professional University en Inde, afin de vous assister dans votre processus d'admission dans notre "
               "université.\n"
               "Selon cet intérêt que vous avez manifesté, l'université vous offre une bourse de 50%.\n"
               "\n"
               "Pour commencer le processus d'admission, nous aimerions que vous remplissiez le questionnaire ci-dessous:\n"
               "Nom et prénom :\n"
               "Pays d'origine :\n"
               "Numéro WhatsApp(contact) :\n"
               "Date de naissance :\n"
               "Email :\n"
               "Nom du Père :\n"
               "Nom de la Mère :\n"
               "Sexe(Genre) :\n"
               "Programme d'étude/filière :\n"
               "\n"
               "Pour plus d'information et d'assistance, vous pouvez nous contacter sur ce même numéro: +918360238249\n")
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
    """
    name() function gets the name of the selected phone number
    :param phone: Any
    :return: names
    """
    dict2_list = list(phone_dict2.values())
    index = dict2_list.index(phone_number)
    dict_list = list(phone_dict.keys())
    names = dict_list[index]
    print(names)
    return names


# phone_dict = {"Jordan": "+22962747600", "Mjd": "+2348140257660", "Zita": "+918360222648", "Papa": "+22997984266",
#               "Saphir": "+23793195666", "Johnstone": "+263777128928", "Idohou": "+22961876476",
#               "Vishnu": "+919591590281", "Rufin": "+22990166164", "Vikanshi": "+919012677280", "Dinah": "+22951864306",
#               "Casimir": "+918968793478", "Tonton Rufin": "+22967601588", "Mr François": "+22997444472"}

# phone_dict2 = {1: "+22962747600", 2: "+2348140257660", 3: "+918360222648", 4: "+22997984266", 5: "+23793195666",
#                6: "+263777128928", 7: "+22961876476", 8: "+919591590281", 9: "+22990166164", 10: "+919012677280",
#                11: "+22951864306", 12: "+918968793478", 13: "+22967601588", 14: "+22997444472"}

phone_dict = {"CAKPO": "+22994461326", "RAYMOND": "+22951216388", "MARC": "+22997612385", "FRANCIS": "+22955438887", "ISAAC": "+22953988863",
              "JUSTIN": "+22959720780", "OSSAH": "+22954075558", "SESSOU": "+22954141856", "FLORIAN": "+22996951584", "FREDI": "+22945588209",
              "MOUFID": "+22967616758", "LUCIEN": "+22952665437", "DONALD": "+22996874500", "EDMOND": "+22991468165", "BALLO": "+22951800715",
              "DJENGUE":"+22966063311", "PISSIA": "+22952185228", "ALEXIS": "+22952037009", "ANICET": "+22952678460", "MAROUANE": "+22995736446",
              "AKPOTCHEME": "+22950957151", "HOUNYE": "+22998491563", "JOSEPH": "+22952694434", "IRIASSAU": "+22957222739", "JUNIOR": "+22967645951",
              "AMOS": "+22994801205", "ALAZA": "+22969604061", "TCHANDO": "+22998955001", "ABDOU": "+22994696935", "ACHIRAF": "+22952926937",
              "RICHARD": "+22962312815", "ELITE": "+22961477271", "DJERI": "+22996757457", "ANAGO": "+22996968867", "JANVIER": "+22967146900",
              "JESUS": "+22997731630", "OUZZA": "+22953863156", "IBRAHIM": "+22991480090","FREJUSTE": "+22952576400", "PROSPER": "+22990756452",
              "DIANEAU": "+22958370983", "EDITH": "+22968007482", "CORNELIX": "+22946344179", "FRESNELLE": "+22957309102", "FAITH": "+22997387234",
              "BRICE": "+22997338916", "PHILIPPE": "+22945277730", "RENEAKADJA": "+22946498361", "SYLAS": "+22942422432", "ETIENNE": "+22967473700",
              "HOUNKPE": "+22958391216","AMOUSSOU": "+22965397328", "GAGO": "+22959238081", "ISSIFOU": "+22966989784", "CYRANO": "+22990122417",
              "ABRAHAM": "+22965614287", "ELVIS": "+22966110243", "MARIO": "+22997299934", "SEKPO": "+22952150929", "ERIC": "+22999226406",
              "AUREL": "+22957833391", "AGBO": "+22960302810", "JUDES": "+22969997152", "BORIS": "+22968998139", "TOFFA": "+22946569372",
              "SYLVESTRE": "+22953561198", "FANICK": "+22956138399", "DAVID": "+22995900770", "HADIROU": "+22961654350", "BIO": "+22962709511",
              "JEAN": "+22997674393", "AWAL": "+22952912717", "ANGE": "+22961816804", "JOSPIN": "+22991153860", "ZOUNGBAN": "+22969595687",
              "TOGBE": "+22962767426", "CHRISTMEL": "+22997970922", "ESSE": "+22968695965", "TONI": "+22954999529", "MURIELLE": "+22956394876",
              "ELIOSSE": "+22990615737", "REGIS": "+22961238715", "AZIZE": "+22959457606", "PRIVATE": "+22996412850", "MOUSTAPHA": "+22962882071",
              "ULRICH": "+22959252210", "FRESHNELLE": "+22959003634", "DONA": "+22956252327", "JENNIFER": "+22962536559", "ABIOLA": "+22969949854"}


phone_dict2 = {1: "+22994461326", 2: "+22951216388", 3: "+22997612385", 4: "+22955438887", 5: "+22953988863", 6: "+22959720780",
               7: "+22954075558",  8: "+22954141856", 9: "+22996951584", 10: "+22945588209", 11: "+22967616758", 12: "+22952665437",
               13: "+22996874500", 14: "+22991468165", 15: "+22951800715", 16: "+22966063311", 17: "+22952185228", 18: "+22952037009",
               19: "+22952678460", 20: "+22995736446", 21: "+22950957151", 22: "+22998491563", 23: "+22952694434", 24: "+22957222739",
               25: "+22967645951", 26: "+22994801205", 27: "+22969604061",28: "+22998955001", 29: "+22994696935", 30: "+22952926937",
               31: "+22962312815", 32: "+22961477271", 33: "+22996757457", 34: "+22996968867", 35: "+22967146900", 36: "+22997731630",
               37: "+22953863156", 38: "+22991480090", 39: "+22952576400", 40: "+22990756452", 41: "+22958370983", 42: "+22968007482",
               43: "+22946344179", 44: "+22957309102", 45: "+22997387234", 46: "+22997338916", 47: "+22945277730", 48: "+22946498361",
               49: "+22942422432", 50: "+22967473700", 51: "+22958391216", 52: "+22965397328", 53: "+22959238081", 54: "+22966989784",
               55: "+22990122417", 56: "+22965614287", 57: "+22966110243", 58: "+22997299934", 59: "+22952150929", 60: "+22999226406",
               61: "+22957833391", 62: "+22960302810", 63: "+22969997152", 64: "+22968998139", 65: "+22946569372", 66: "+22953561198",
               67: "+22956138399", 68: "+22995900770", 69: "+22961654350", 70: "+22962709511", 71: "+22997674393", 72: "+22952912717",
               73: "+22961816804", 74: "+22991153860", 75: "+22969595687", 76: "+22962767426", 77: "+22997970922", 78: "+22968695965",
               79: "+22954999529", 80: "+22956394876", 81: "+22990615737", 82: "+22961238715", 83: "+22959457606", 84: "+22996412850",
               85: "+22962882071",86: "+22959252210", 87: "+22959003634", 88: "+22956252327", 89: "+22962536559", 90: "+22969949854"}

message_type: int = display_message_type()
# print(message_type)

# desired_name = ""
# desired_number_list = display_contact_list(phone_dict, phone_dict2)
# desired_message = getMessage()
# print(desired_number_list)
# print(desired_message)


match message_type:
    case 1:
        try:
            systems()
            # website()
            desired_number_list = display_contact_list(phone_dict, phone_dict2)
            instant_sends = []
            for desired_number in desired_number_list:
                desired_name = get_name(desired_number)
                talk('Provide message for' + desired_name)
                desired_message = getMessage()
                instant_sends.append([desired_name, desired_number, desired_message])

            for instant_send in instant_sends:
                # print(instant_send)
                pywhatkit.sendwhatmsg_instantly(instant_send[1], instant_send[2], 30, True, 15)
                print("Successfully Sent!")
                talk("Message Successfully Sent to" + instant_send[0])


        except:
            print("Error while sending")
            talk("Error while sending")

    case 2:
        try:
            systems()
            # website()
            desired_number_list = display_contact_list(phone_dict, phone_dict2)
            plans = []
            for desired_number in desired_number_list:
                planned_details = sendProgrammedDetails()
                desired_name = get_name(desired_number)
                desired_message = getMessage()
                plans.append([desired_name, desired_number, list(planned_details.values()), desired_message])

            for plan in plans:
                # print(plan)
                sendwhatmsg(plan[1], plan[3], plan[2][0], plan[2][1], 30, True, 15)
                print("Successfully Sent !")
                talk("Message Successfully Sent to!" + plan[0])

        except:
            print("Error while sending message")
            talk("Error while sending message")

    case 3:
        try:
            systems()
            # website()
            diffList = display_contact_list(phone_dict, phone_dict2)
            desired_message = getMessage()
            for desired_number in diffList:
                sendwhatmsg_instantly(desired_number, desired_message, 30, True, 15)
                print("Successfully Sent!")
            talk("Message Successfully Sent to the diffusion list")
        except:
            print("Error while sending diffusion message")
