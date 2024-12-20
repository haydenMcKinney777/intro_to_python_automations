"""
Facebook Graph API: Using graph api from facebook we can work with certain data on user accounts.
                    Using the interface


Graph API documentation found here: https://developers.facebook.com/docs/graph-api
"""

import requests
import json

url = "https://graph.facebook.com/v21.0/me?fields=id%2Cname%2Clast_name&access_token=EAAP4GRgo2xYBO2Dxu848Xi1V5lDTIzRqdQIMJZBYa6nsccqZBbL9MZAs1Yf28hT3XIXJA78cyNN06d6s1DkZCE3WZCaRgNsPtMP5jprrKbYnM46szttqglSOA6puNJfA1qh75ilTh1KUlWrgmK1bgwh12LIA0sf4mRF1nJR8xLrxrtyKwK7NOgXfRW6NN4jlo8LKjQsNnPRhWnnLVnWlCV3jxSAZDZD"
response = requests.get(url)
data = response.text

data = json.loads(data)             #data is actually a string, despite looking like and having the same format of a dictionary. So here we are converting data to a dictionary

print(data['last_name'])