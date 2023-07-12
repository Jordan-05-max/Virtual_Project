import pywhatkit
from pywhatkit import sendwhatmsg_instantly, sendwhatmsg
phone_dict = {"Jordan": "+22962747600", "Mjd": "+2348140257660", "Zita": "+918360222648", "Johnstone": "+263777128928",
              "Donald Idohou": "+22961876476", "Papa": "+22997984266", "Vishnu": "+919591590281",
              "Saphir": "+23793195666", "Rufin": "+22990166164", "Vikanshi": "+919012677280", "Casimir": "+918968793478"
    , "Tonton Rufin": "+22967601588", "Romualdine": "+22951864306", "Mr François": "+22997444472"}

phone_dict2 = {1: "+22962747600", 2: "+2348140257660", 3: "+918360222648", 4: "+263777128928", 5: "+22961876476",
               6: "+22997984266", 7: "+919591590281", 8: "+23793195666", 9: "+22990166164", 10: "+919012677280",
               11: "+918968793478", 12: "+22967601588", 13: "+22951864306", 14: "+22997444472"}



def name(phone):
    x = list(phone_dict2.values())
    y= x.index(phone)
    k = list(phone_dict.keys())
    ke = k[y]
    print(type(ke))
name("+22997444472")