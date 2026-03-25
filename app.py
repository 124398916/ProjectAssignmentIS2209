import requests
from flask import Flask
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CAT_FACTS_API_KEY = os.getenv("CAT_FACTS_API_KEY")
CAT_FACTS_URL = 'https://meowfacts.herokuapp.com/'

app = Flask(__name__)

##
@app.route('/')
def hello_world():
    response = requests.get(CAT_FACTS_URL)
    data = response.json()

    # Extract the cat fact
    fact = data.get("data", ["No fact found"])[0]

    return f"Interesting Cat Fact: {fact}"

if __name__ == '__main__':
    app.run()