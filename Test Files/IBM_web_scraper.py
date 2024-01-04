from bs4 import BeautifulSoup
import requests
import json

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
    update_dictionary()
    # data = get_text_snia("https://www.snia.org/education/online-dictionary/a/s/d/all")