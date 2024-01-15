from dotenv import load_dotenv
from gotrue import errors
import os
from supabase import create_client, Client

load_dotenv()  # for environment variabls

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

user_email: str = "luke.baber1@gmail.com"
user_password: str = "abc123"

# Signs user up
# user = supabase.auth.sign_up({"email": user_email, "password": user_password})
session = None

try:
    # Sign in
    session = supabase.auth.sign_in_with_password({"email": user_email, "password": user_password})
    print(session)

except errors.AuthApiError:
    print("Login failed")


supabase.auth.sign_out()

# if __name__ == "__main__":
#     print ("x")