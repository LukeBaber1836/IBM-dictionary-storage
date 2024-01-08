from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# Read data
# data = supabase.table("IBM_terms_duplicate").select("id, term, definition").eq("term", "dog").execute()
# assert len(data.data) > 0

# Insert data
# data = supabase.table("IBM_terms_duplicate").insert([{"term":"ds8000", "definition":"Really cool product"}]).execute()

def get_definition(word):
    # Get data from supabase database
    data = supabase.table("IBM_terms").select("id, term, definition").eq("term", f"{word.lower()}").execute()

    if len(data.data) != 0:
        deff_list = data.data[0]['definition'].split('|')
        full_deff = ''
        count = 1
        for def_val in deff_list:
            full_deff = full_deff + f"Definition {count}:  " + def_val + "\n \n"
            count +=1
    else: full_deff = "Word not found..."

    return (full_deff)

def add_definition(word, definition):
    # Opening JSON file
    with open('dictionary.json', 'r+') as file:
        definition = definition.split(', ') # Check for multiple definitions
        

if __name__ == "__main__":
    print(get_definition("dog"))