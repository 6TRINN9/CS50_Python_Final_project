from PySide6 import QtWidgets
from W_generator import W_generator
from ui.ui_new_note import Ui_New_Note



class W_new_note(QtWidgets.QDialog):
    def __init__(self, w_main):       
        super(W_new_note, self).__init__() 

        self.w_main = w_main
        self.connection = w_main.connection

        self.title = ""
        self.login = ""
        self.password = ""
        self.url = ""

        self.ui = Ui_New_Note()
        self.ui.setupUi(self)
        self.show()

        

        self.ui.btn_create_password.clicked.connect(self.open_generator_window)
        self.ui.btn_create_note.clicked.connect(self.add_new_note)

        

    def open_generator_window(self):
        self.w_generator = W_generator(self)

    def add_new_note(self):
        title = self.ui.le_Title.text()
        login = self.ui.le_login.text()
        password = self.ui.le_password.text()
        url = self.ui.le_url.text()

        self.connection.add_new_note_query(title, login, password, url)

        self.close()        

    def set_password(self, password):
        self.password = password
        self.ui.le_password.setText(self.password)

    def close(self):
        self.w_main.update_model()
        return super().close()