from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def get_definition(word):
    # Get data from supabase database
    data = supabase.table("IBM_terms").select("*").eq("term", word.lower()).execute()

    if len(data.data) != 0:
        deff_list = data.data[0]['definition'].split('|')
        full_deff = ''
        count = 1
        for def_val in deff_list:
            full_deff = full_deff + f"Definition {count}:  " + def_val + "\n \n"
            count +=1
    else: full_deff = "Word not found..."

    return (full_deff)

# Returns list of 5 other possible word matches
def other_definitions(word):
    # Get data from supabase database with .like()
    data = supabase.table("IBM_terms").select("*").like("term", f"{word.lower()}%").execute()
    other_words = []
    iteration = 0
    
    # First check if there are any other definitions for 'word'
    if len(data.data) <= 1:
        other_words = ["No word sugestions..."]
        return other_words
    else:
        while len(other_words) != len(data.data) and len(other_words) < 5 and iteration:
            # Skip exact match
            if data.data[iteration]['term'] == word.lower():
                iteration += 1
                continue
            else:
                other_words.append(data.data[iteration]['term'].capitalize())
                iteration += 1

        return (other_words)  


def add_definition(word, definition):
    data = supabase.table("IBM_terms").select("*").execute()
    word_exists = supabase.table("IBM_terms").select("*").eq("term", word.lower()).execute()

    # If not repeat, add new definition
    if len(word_exists.data) == 0:
        data = supabase.table("IBM_terms").insert([{"term":word.lower(), "definition":definition}]).execute()
        return True
    else:
        print("Definition already exists")
        return False
        

if __name__ == "__main__":
    print(get_definition("hot"))
    # print(add_definition("DS8000","A really cool product"))
    print(other_definitions("bible"))