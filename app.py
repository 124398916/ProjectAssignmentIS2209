from flask import Flask
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()

# accessing and printing value
print(os.getenv("MY_KEY"))

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello there!!'


if __name__ == '__main__':
    app.run()