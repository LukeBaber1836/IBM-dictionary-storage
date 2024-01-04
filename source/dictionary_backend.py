import json

def word_definition(word):
    # Opening JSON file
    file = open('dictionary1.json')
    data = json.load(file)
    try:
        definition = data[word.lower()]
        full_deff = ''
        count = 1
        for x in definition:
            full_deff = full_deff + f"Definition {count}:  " + x + "\n \n"
            count +=1
        return full_deff
    except Exception:
        return("Word not found...")

def add_definition(word, definition):
    # Opening JSON file
    with open('dictionary1.json', 'r+') as file:
        definition = definition.split(', ') # Check for multiple definitions
        data = json.load(file)
        data.update({word.lower(): definition}) # Add new word to dictionary
        file.seek(0)
        json.dump(data, file, indent = 4) # convert back to json
    

if __name__ == "__main__":
    add_definition("Ds8000", "Mainframe storage for IBM, Really cool product dude")
    print(word_definition("DS8000"))