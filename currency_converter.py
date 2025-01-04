"""
Creating a GUI that will provide the user with a definition of a word provided by the user
"""

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QHBoxLayout,
                               QVBoxLayout, QWidget, QLineEdit, QComboBox, QFileDialog)
from PySide6.QtCore import Qt
from pathlib import Path

def search_word():
    print("Hi")

app = QApplication([])                                              
window = QWidget()                                                  
window.setWindowTitle('Dictionary')
layout = QVBoxLayout()                                              

instruction_text = QLabel("Enter a word for its definition")
layout.addWidget(instruction_text)

textbox = QLineEdit()
layout.addWidget(textbox)

search_button = QPushButton("Search")
layout.addWidget(search_button)
search_button.clicked.connect(search_word)

window.setLayout(layout)
window.show()                                                       
app.exec()                                                          