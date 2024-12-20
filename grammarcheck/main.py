"""
Grammar check API: Using post requests and Language tool API, send some text to the grammar checker API's server, where
                   it will correct our text and send it back to us.

Documentation found at: https://languagetool.org/http-api/

The base URL is api.languagetoolplus.com/v2. what you insert at the end of the url is found in the docs.

note we are using POST here since we are sending data

this is a very lightweight and simply grammar checker. do not expect anything crazy

TO-DO: have users enter text in dynamically and assign it to the 'data' dictionary instead of it being hardcoded.
"""

import requests

url = 'https://api.languagetool.org/v2/check'
data = {
    'text' : 'tihs is grammatikaly rong.',
    'language' : 'en-US'
}
response = requests.post(url, data=data).json()              #we are sending our url, the language (required) and the text to check. the api sends a string back, and we turn it into a dictionary with .json()

typos = response['matches']
print(f"\nTotal number of typos found: {len(typos)}")

for typo in typos:
    message = typo['message']
    replacements = [r['value'] for r in typo['replacements']]       #list comprehension
    context = typo['context']['text']
    offset = typo['offset']

    print(f"\nError: {message}\n In: '{context}' starting at position offset {offset} - did you mean {replacements}?")

print("\nGrammar check complete!\n")


#Below is an example of the JSON format that the API would return: (I got this from running print(response)
# {
#
#   'software': {
#       'name': 'LanguageTool', 
#       'version': '6.6-SNAPSHOT', 
#       'buildDate': '2024-12-17 18:50:29 +0100', 
#       'apiVersion': 1, 
#       'premium': True, 
#       'premiumHint': 'You might be missing errors only the Premium version can find. Contact us at support<at>languagetoolplus.com.', 
#       'status': ''}, 
#       'warnings': {
#           'incompleteResults': False
#       },

#  'language': {
#       'name': 'English (US)', 
#       'code': 'en-US', 
#       'detectedLanguage': {
#           'name': 'English (US)', 
#           'code': 'en-US', 
#           'confidence': 0.0, 
#           'source': None}}, 

#  'matches': [
#   {
#       'message': 'This sentence does not start with an uppercase letter.', 
#       'shortMessage': '', 
#       'replacements': [
#           {
#               'value': 'Tihs'
#           }
#       ], 
#       'offset': 0, 
#       'length': 4, 
#       'context': {
#           'text': 'tihs is grammatikaly rong.', 
#           'offset': 0, 'length': 4}, 
#           'sentence': 'tihs is grammatikaly rong.', 
#           'type': {'typeName': 'Other'}, 
#           'rule': {'id': 'UPPERCASE_SENTENCE_START', 
#           'description': 'Checks that a sentence starts with an uppercase letter', 
#           'issueType': 'typographical', 
#           'urls': [{'value': 'https://languagetool.org/insights/post/spelling-capital-letters/'}], 'category': {'id': 'CASING', 'name': 'Capitalization'}, 'isPremium': False, 'confidence': 0.6}, 'ignoreForIncompleteSentence': True, 'contextForSureMatch': -1}, 
#       ...
#       ...
#       ...