import json

def get_definition(word):
    # Opening JSON file
    file = open('dictionary.json')
    data = json.load(file)
    word = word.lower()
    full_deff = ''
    
    if data.__contains__(word):
        definition = data[word]
        count = 1
        for x in definition:
            full_deff = full_deff + f"Definition {count}:  " + x + "\n \n"
            count +=1
    else: full_deff = "Word not found..."

    return (full_deff)   

def other_definitions(word):
    # Opening JSON file
    file = open('dictionary.json')
    data = json.load(file)
    word = word.lower()
    other_words = ''
    
    # Find other possible words
    other_words_dict = {key: val for key, val in data.items()
       if key.startswith(word)}
    
    for val in list(other_words_dict.keys())[0:5]: 
        other_words = other_words + val.capitalize()
        if val != list(other_words_dict.keys())[4]:
            other_words = other_words + ', '

    return (other_words)  

def add_definition(word, definition):
    # Opening JSON file
    with open('dictionary.json', 'r+') as file:
        definition = definition.split(', ') # Check for multiple definitions
        data = json.load(file)
        data.update({word.lower(): definition}) # Add new word to dictionary
        file.seek(0)
        json.dump(data, file, indent = 4) # convert back to json
    

if __name__ == "__main__":
    # add_definition("Ds8000", "Mainframe storage for IBM, Really cool product dude")
    print(get_definition("DS8000"))