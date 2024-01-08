from bs4 import BeautifulSoup
import requests
import json

# Link where data is pulled from: "https://www.ibm.com/docs/en/ds8900/9.4.0?topic=glossary"
def get_text_ibm(url):
    page_data = requests.get(url).text
    soup = BeautifulSoup(page_data, 'html.parser')
    data = {}
    num = 2
    while True:
        try:
            term = soup.find_all(class_="dlterm")[num].next
            defin = soup.find_all(class_="dlentry")[num].text
            data.update({str(term): str(defin)})
            num+=1
            print(num, end="\r")
        except Exception:
            break
    return data

# Link where data is pulled from: "https://www.snia.org/education/online-dictionary/a/s/d/all"
def get_text_snia(url):
    page_data = requests.get(url).text
    soup = BeautifulSoup(page_data, 'html.parser')
    data = {}
    num = 0
    while True:
        try:
            term = soup.find_all(class_="field-content")[num].text
            term = term.replace('[Permalink]','').rstrip() # Clean up term
            defin = soup.find_all(class_="field-content")[num + 1].text
            data.update({str(term): str(defin)})
            num+=2
            print(f"{num} / {len(soup.find_all(class_='field-content'))}", end="\r")
        except Exception:
            break
    return data

def json_to_csv(file_path):
    file_1 = open(file_path)
    data_1 = json.load(file_1)
    num = 0
    with open("Test Files/dictionary_ibm.csv", "a+") as file:
        while True:
            if num == len(data_1):
                break

            file.write('"' + list(data_1.keys())[num] + '"' + ' ')
            # Check for multiple definitions
            for val in list(data_1.values())[num]:
                if val != list(data_1.values())[num][(len(list(data_1.values())[num]))-1]:
                    file.write(',' + '"' + val + '"')
                else:
                    file.write(',' + '"' + val + '"' + "\n")
            num +=1

def update_dictionary():
    url = "https://www.ibm.com/docs/en/ds8900/9.4.0?topic=glossary"
    dictionary = get_text_ibm(url)
    for index in range(len(dictionary)):
        add_definition(list(dictionary.keys())[index], list(dictionary.values())[index])


def add_definition(word, definition):
    # Opening JSON file
    with open('dictionary_ibm.json', 'r+') as file:
        definition = definition.split('| ') # Check for multiple definitions
        data = json.load(file)
        data.update({word.lower(): definition}) # Add new word to dictionary
        file.seek(0)
        json.dump(data, file, indent = 4) # convert back to json

if __name__ == "__main__":
    json_to_csv('dictionary_files/dictionary_snia.json')