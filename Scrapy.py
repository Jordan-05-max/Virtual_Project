import scrapy
import json
import random
def read_from_json(path,key):
    values = []
    #file = "C:/Users/jorda/PycharmProjects/virtualEnviroment/character.json"
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        clean_sentence = sentence.strip()
        cleaned.append(clean_sentence)
    return cleaned

def random_item(objectlist):
    rand_numb = random.randint(0, len(objectlist)-1)
    return objectlist[rand_numb]

def random_value(source_path, key):
    all_values = read_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return random_item(clean_values)

def random_quote():
    return random_value('quotes.json', 'quote')

def random_character():
    return random_value('character.json', 'character')

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ? '
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
            # This will stop the loop!

if __name__ == '__main__':
    main_loop()