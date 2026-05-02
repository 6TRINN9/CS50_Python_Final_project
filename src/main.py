import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets

from W_new_note import W_new_note

class Password_manager(QMainWindow):
    def __init__(self):
        super(Password_manager, self).__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.open_new_note_window()
       

    def open_new_note_window(self):
        self.w_new_note = W_new_note()
    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Password_manager()
    window.show()

    sys.exit(app.exec())
