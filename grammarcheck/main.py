"""
Grammar check API: Using post requests and Language tool API, send some text to the grammar checker API's server, where
                   it will correct our text and send it back to us.

Documentation found at: https://languagetool.org/http-api/

The base URL is api.languagetoolplus.com/v2. what you insert at the end of the url is found in the docs.

note we are using POST here since we are sending data
"""

import requests

url = 'https://api.languagetool.org/v2/check'
data = {
    'text' : 'tihs is grammatikaly rong.',
    'language' : 'en-US'
}
response = requests.post(url, data=data).json()              #we are sending our url, the language (required) and the text to check. the api sends a string back, and we turn it into a dictionary with .json()

print(response)