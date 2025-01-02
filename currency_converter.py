"""
Creating a currency converter GUI by scraping the currency exchange rate using beautifulsoup
and the gui with PyQT

In this branch, we are giving the GUI a dropdown menu for the user to pick which currencies they would like to convert between
"""

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit, QComboBox)

from bs4 import BeautifulSoup
import requests

def get_exchange_rates(input_currency='USD', output_currency='EUR'):
    url = f'https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").getText()
    rate = float(rate[:-4])

    return rate

def convert():
    input_text = textbox.text()                                     #we store the text that the user provided in the textbox to a variable called input_text
    input_currency = input_combo.currentText()                      #we set the input currency to whatever the user selected in the first dropdown
    target_currency = target_combo.currentText()
    rate = get_exchange_rates(input_currency, target_currency)
    output = round(float(input_text) * rate, 3)               
    message = f"{input_text} {input_currency} is equivalent to {output} {target_currency}."
    output_label.setText(str(message))                               #output must be converted to a string to display itself          

app = QApplication([])                                              #creating an instance of the application which takes an argument. we pass an empty list here as the argument which just means 'no argument'
window = QWidget()                                                  #creating a window instance to hold all the elements of our application
window.setWindowTitle('Currency Converter')

#we add widgets (elements that are visible in the window) to something called a layout. here we are creating a textbox. Note that we have to manually attach the layout to the window - creating just a layout and adding widgets to it will not show up
layout = QVBoxLayout()                                              #note 'QV' as in vertical. So if we add anymore widgets to this layout, they will be stacked vertically. could use QHLayout instead for horizontal

input_combo = QComboBox()                                           #instantiating a combo box (a dropdown)
currencies = ['USD', 'EUR', 'INR', 'JPY']
input_combo.addItems(currencies)                                  #adding the list of currencies to the combo box
layout.addWidget(input_combo)

target_combo = QComboBox()                                          
target_combo.addItems(currencies)                               
layout.addWidget(target_combo)


textbox = QLineEdit()                                               
layout.addWidget(textbox)

btn = QPushButton('Convert')
layout.addWidget(btn)

btn.clicked.connect(convert)                                        #PyQT is made of widgets, signals, and slots. the button is our widget, 'clicked' is our signal, and slot is the 'convert' function. so when our button is clicked, make_sentence function gets connected. notice we only mention the function within the parenthesis and do not actually call it

output_label = QLabel('')                                          #when the application first runs, we do not want anything to appear in the label so we just give it an empty string
layout.addWidget(output_label)

window.setLayout(layout)


window.show()                                                       #without this we cannot see the window when the app runs
app.exec()                                                          #execute (run) the app