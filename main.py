import requests
from dotenv import load_dotenv
import os

# link morse code dictionary API
# load_dotenv(r"C:\Users\vikas\Google Drive\Avish\Udemy\PythonBootcamp\Projects\MorseCode\.env")
# morse_code_dict_api = os.getenv('API_Endpoint')
morse_code_dict_api = 'https://api.npoint.io/11d0b507c4a9a403ca01'
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

