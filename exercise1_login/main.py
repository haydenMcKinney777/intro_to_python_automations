"""
NEWSAPI: this file shows how we can simply use news API to gather information from news articles online.
         all we do is make a request to 'https://newsapi.org/v2/everything'. Everything added onto this URL
         is for us to tell it specifically what parameters we want the API to search for. For example, if we 
         wanted news articles with the words "exercise" or "stock prices" in the title, we would add a 
         qInTitle parameter to the end of the link. At the end of the URL we add our API key.
"""

import requests

r = requests.get("https://newsapi.org/v2/everything?qInTitle=Black%20Ops%206&apiKey=50ae6f8dd35c4e86bd73945f2b845548")      #GET requests return data in JSON format

print(r.headers['Content-Type'])                                                                                        #simply print statement to verify that our GET request returns data in JSON format

content = r.json()                                                                                                      #turns the json data given by our get request into a python dictionary full of the json data

articles = content['articles']                                                                                          #here we are accessing the dictionary that we created and we are grouping all of the articles into a variable. articles is a dictionary itself, which contains more lists and dictionaries. with this, we are able to access all of the information that we want to from the news stories that the API gathers, such as the titles of each articles, descriptions of them, etc. 

for article in articles:
    print("\nTITLE: ", article['title'], "\nDESCRIPTION:\n", article['description'], "\nPUBLISHED AT:\n", article['publishedAt'])

print(articles)