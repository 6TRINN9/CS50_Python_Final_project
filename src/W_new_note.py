from PySide6 import QtWidgets

from W_generator import W_generator
from ui.ui_new_note import Ui_New_Note



class W_new_note(QtWidgets.QDialog):

    password = ""

    def __init__(self):       
        super(W_new_note, self).__init__() 
        self.ui = Ui_New_Note()
        self.ui.setupUi(self)
        self.show()

        self.ui.btn_create_password.clicked.connect(self.open_generator_window)
        

    def open_generator_window(self):
        self.w_generator = W_generator(self)

    def update_info(self):
        pass
        

    def set_password(self, password):
        self.password = password
        self.ui.le_password.setText(self.password)