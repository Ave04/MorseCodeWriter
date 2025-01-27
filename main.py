import requests
from dotenv import load_dotenv
import os

# link morse code dictionary API
load_dotenv(r"C:\Users\vikas\Google Drive\Avish\Udemy\PythonBootcamp\Projects\MorseCode\MorseCode\.env")

morse_code_dict_api = os.getenv('API_Endpoint')
route = requests.get(url=morse_code_dict_api)
response = route.json()

# Check if proper dictionary is returned
print(response)

user_input = input('Please write any text: ')

# while loop condition
condition = True

while condition:
    # exit condition
    if user_input == 'Exit':
        condition = False
    else:
        for i in user_input.upper():

            print(response[i])
            condition = False

