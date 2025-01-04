"""
Creating a GUI that will allow us to permanently delete certain files

docs: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html

"""

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QHBoxLayout,
                               QVBoxLayout, QWidget, QLineEdit, QComboBox, QFileDialog)
from PySide6.QtCore import Qt

def open_files():
    filenames, _ = QFileDialog.getOpenFileName(window, "Select Files to be Deleted")        #QFileDialog is what enables a user to traverse the file system in order to select files in a directory
    print(filenames)


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
layout.addWidget(destroy_button)

# #if file deletion successful, message = "Success." Else message = "Fail" 
# result_message = QLabel(message)

window.setLayout(layout)
window.show()                                                       #without this we cannot see the window when the app runs
app.exec()                                                          