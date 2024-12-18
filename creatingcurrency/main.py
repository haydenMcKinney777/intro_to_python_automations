"""
Creating Currency: this file creates a simply web app using flask
                   that will use the code we made in the beautiful soup branch to scrape a currency exchange
                   rate from x-rates.com using REST API. Once the web app has been launched, the user may supply different
                   currency codes within the URL such as USD-EUR or EUR-JPY etc to grab the exchange rate
                   between the two currencies. The output is displayed on the page in JSON format.

"""

from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(input_currency, output_currency):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text                                                                 #requests.get(url) will return the status of the GET request. but if we add .text at the end, we get the source code for the html page, since that is obviously what would be replied with in a GET request
    soup = BeautifulSoup(content, "html.parser")                                                     #we create an instance of BeautifulSoup called 'soup' which expects a page's markup (held in content) and we also tell it we want to use an html parser which will be used to parse through the markup code for the <span> element that holds the number for the exchange rate on the webpage.
    rate = soup.find("span", class_="ccOutputRslt").get_text()                                       #the element on the webpage that holds the exchange rate is a span with a class of 'ccOutputRslt'. If we do not include .get_text() at the end, beautiful soup will return the markup for the span in which the currency rate number lives inside, as well as all child elements of the span class. Adding .get_text() ensures we only grab the exchange rate number with its related tag (USD, AUD, etc). Note that this value will be a string
    currency = float(rate[0:8])                                                                      #this makes sure we only grab the number of the exchange rate, only grabbing the string between index 0 and 8. This value is still a string, so we convert it to a float in this same step as well.

    return currency

print(get_currency('INR', 'AUD'))

app = Flask(__name__)       #__name__ holds the string of the current module

@app.route('/')
def home():
    return f'<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<input_currency>-<output_currency>')
def api(input_currency, output_currency):
    rate = get_currency(input_currency, output_currency)
    result_dictionary = {'input_currency':input_currency, 'output_currency':output_currency, 'rate':rate}
    return jsonify(result_dictionary)

app.run()