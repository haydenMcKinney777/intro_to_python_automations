"""
Creating a GUI that will allow us to permanently delete certain files

docs: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html

"""

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QHBoxLayout,
                               QVBoxLayout, QWidget, QLineEdit, QComboBox, QFileDialog)
from PySide6.QtCore import Qt
from pathlib import Path

def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files to be Deleted")        #QFileDialog is what enables a user to traverse the file system in order to select files in a directory. Once a user selects some files to be deleted, their absolute paths will be stored as a list held in our variable called 'filenames'
    result_message.setText('\n'.join(filenames))                                             #the message will be the paths separated by a newline. This is what will display after the user destroys the files


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')                                                                 #overwrite the file
        path.unlink()                                                                       #.unlink() will delete the path
    result_message.setText('Destruction Successful!')

app = QApplication([])                                              
window = QWidget()                                                  
window.setWindowTitle('File Destroyer')

layout = QVBoxLayout()                                              

instruction_text = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted.')
layout.addWidget(instruction_text)

open_button = QPushButton('Open Files')
layout.addWidget(open_button, alignment=Qt.AlignmentFlag.AlignCenter)
open_button.clicked.connect(open_files)

destroy_button = QPushButton('Destroy Files')
layout.addWidget(destroy_button, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_button.clicked.connect(destroy_files)

result_message = QLabel('')
layout.addWidget(result_message)

window.setLayout(layout)
window.show()                                                       #without this we cannot see the window when the app runs
app.exec()                                                          