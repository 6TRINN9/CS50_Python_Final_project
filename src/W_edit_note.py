
from PySide6 import QtWidgets
from W_generator import W_generator
from ui.ui_new_note import Ui_New_Note

class W_edit_note(QtWidgets.QDialog):
    def __init__(self, w_main, id_row):       
        super(W_edit_note, self).__init__() 

        self.title = ""
        self.login = ""
        self.password = ""
        self.url = ""
        self.note_id = ""

        self.w_main = w_main
        self.connection = w_main.connection
        self.id_row = id_row

        self.ui = Ui_New_Note()
        self.ui.setupUi(self)
        self.setup_ui()
        self.update_info()
        self.show()


        

    def setup_ui(self):
        self.ui.btn_create_password.clicked.connect(self.open_generator_window)
        self.ui.btn_create_note.clicked.connect(self.edit_note)
        self.ui.btn_create_note.setText("Edit")
        self.setWindowTitle("Edit note")
        self.ui.label_note.setText("Edit note")

    def open_generator_window(self):
        self.w_generator = W_generator(self)

    def edit_note(self):
        title = self.ui.le_Title.text()
        login = self.ui.le_login.text()
        password = self.ui.le_password.text()
        url = self.ui.le_url.text()

        self.connection.update_note_query(title, login, password, url, self.note_id)
        self.close()

    def update_info(self):
        model = self.w_main.ui.tableView.model()
        row_data = []
        for col in range(model.columnCount()):
            cell_index = model.index(self.id_row, col)
            row_data.append(model.data(cell_index))

        self.title = row_data[1]
        self.login = row_data[2]
        self.password = row_data[3]
        self.url = row_data[4]
        self.note_id = str(row_data[0])


        self.ui.le_Title.setText(self.title)
        self.ui.le_login.setText(self.login)
        self.ui.le_password.setText(self.password)
        self.ui.le_url.setText(self.url)

    def set_password(self, password):
        self.password = password
        self.ui.le_password.setText(self.password)

    def close(self):
        self.w_main.update_model()
        return super().close()
