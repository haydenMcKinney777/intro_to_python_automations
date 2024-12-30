"""
Creating a very simple "make sentences" GUI app with pyQT which will take
in a simple sentence, and make sure that it starts with a capital
and ends with a period.
"""

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit)

def make_sentence():
    input_text = textbox.text()                                     #we store the text that the user provided in the textbox to a variable called input_text
    output_label.setText(input_text.capitalize() + '.')                   #this line ensures that we change the final output sentence to have a capitalized first letter and ends in a period as all proper sentences do.

app = QApplication([])                                              #creating an instance of the application which takes an argument. we pass an empty list here as the argument which just means 'no argument'
window = QWidget()                                                  #creating a window instance to hold all the elements of our application
window.setWindowTitle('Sentence Maker')

#we add widgets (elements that are visible in the window) to something called a layout. here we are creating a textbox. Note that we have to manually attach the layout to the window - creating just a layout and adding widgets to it will not show up
layout = QVBoxLayout()                                              #note 'QV' as in vertical. So if we add anymore widgets to this layout, they will be stacked vertically. could use QHLayout instead for horizontal

textbox = QLineEdit()                                               
layout.addWidget(textbox)

btn = QPushButton('Make Sentence')
layout.addWidget(btn)

btn.clicked.connect(make_sentence)                                 #PyQT is made of widgetsm signals, and slots. the button is our widget, 'clicked' is our signal, and slot is the 'make_sentence' function. so when our button is clicked, make_sentence function gets connected (or called)

output_label = QLabel('')                                          #when the application first runs, we do not want anything to appear in the label so we just give it an empty string
layout.addWidget(output_label)

window.setLayout(layout)


window.show()                                                       #without this we cannot see the window when the app runs
app.exec()                                                          #execute (run) the app