"""
Creating a GUI that will provide the user with a definition of a word provided by the user
"""

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QHBoxLayout,
                               QVBoxLayout, QWidget, QLineEdit, QComboBox, QFileDialog)
from PySide6.QtCore import Qt
from pathlib import Path
import json

def search_word_def():
    user_word = textbox.text()
    if user_word in data:
        matching_defs = data[user_word]                                                                                #matching_defs will be a list of strings containing the definitions
        formatted_defs = "\n".join([f"{i + 1}. {definition}" for i, definition in enumerate(matching_defs)])           #join each of the definition strings with a newline and a number
        resulting_def.setText(formatted_defs)                                                                          #display the definitions in the resulting_def output box at bottom of the GUI
    else:
        resulting_def.setText("Word definition not found.")

app = QApplication([])                                              
window = QWidget()                                                  
window.setWindowTitle('Dictionary')
layout = QVBoxLayout()                                              

file_json = open("./data.json")
data = json.load(file_json)

layout_top = QHBoxLayout()
layout.addLayout(layout_top)

instruction_text = QLabel("Enter a word for its definition:")
layout_top.addWidget(instruction_text)

textbox = QLineEdit()
layout_top.addWidget(textbox)

layout_bottom = QHBoxLayout()
layout.addLayout(layout_bottom)

resulting_def = QLabel('')
layout_bottom.addWidget(resulting_def)

search_button = QPushButton("Search")
layout.addWidget(search_button)
search_button.clicked.connect(search_word_def)

window.setLayout(layout)
window.show()                                                       
app.exec()                                                          