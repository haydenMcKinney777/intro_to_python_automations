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
    resulting_def = data[user_word]

app = QApplication([])                                              
window = QWidget()                                                  
window.setWindowTitle('Dictionary')
layout = QHBoxLayout()                                              

file_json = open("./data.json")
data = json.load(file_json)

instruction_text = QLabel("Enter a word for its definition:")
layout.addWidget(instruction_text)

textbox = QLineEdit()
layout.addWidget(textbox)

resulting_def = QLabel('')

search_button = QPushButton("Search")
layout.addWidget(search_button)
search_button.clicked.connect(search_word_def)

window.setLayout(layout)
window.show()                                                       
app.exec()                                                          