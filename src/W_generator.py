
from PySide6 import QtWidgets

from ui.ui_generator import Ui_Password_generator

from utils import generate_password, evaluate_password_strength, calculate_password_entropy



class W_generator(QtWidgets.QDialog):
    password = ""
    length = 8
    use_lowercase = True
    use_uppercase = True
    use_digits = True
    use_specials = True

    entropy = 0
    strength = "Strength: none"

    def __init__(self, _W_new_note):       
        super(W_generator, self).__init__() 
        self._W_new_note = _W_new_note
        self.ui = Ui_Password_generator()
        self.ui.setupUi(self)
        self.update_info()
        self.change_type_chars()
        self.init_btns()
        self.show()

    def init_btns(self):
        self.ui.bnt_repeat.clicked.connect(self.generate)

        self.ui.cb_lowercase.clicked.connect(self.change_type_chars)
        self.ui.cb_uppercase.clicked.connect(self.change_type_chars)
        self.ui.cb_digits.clicked.connect(self.change_type_chars)
        self.ui.cb_specials.clicked.connect(self.change_type_chars)

        self.ui.slider_pass_length.valueChanged.connect(self.change_length)
        self.ui.slider_pass_length.setValue(self.length)

        self.ui.btm_ok.clicked.connect(self.close)
        

    def generate(self):
        self.password = generate_password(self.length, self.use_lowercase, self.use_uppercase, self.use_digits, self.use_specials)
        self.entropy = calculate_password_entropy(self.password)
        self.strength = evaluate_password_strength(self.entropy)
        self.update_info()

    def update_info(self):
        self.ui.le_view_password.setText(self.password)
        self.ui.lb_entropy.setText(f"Entropy: {self.entropy} bit")
        self.ui.lb_strength.setText(self.strength)

    def change_type_chars(self):
        self.use_lowercase = self.ui.cb_lowercase.isChecked()
        self.use_uppercase = self.ui.cb_uppercase.isChecked()
        self.use_digits = self.ui.cb_digits.isChecked()
        self.use_specials = self.ui.cb_specials.isChecked()
    
    def change_length(self):
        len_pass = self.ui.slider_pass_length.value()
        self.ui.le_pass_length.setText(f"{len_pass}")
        self.length = len_pass
    
    def close(self):
        self._W_new_note.set_password(self.password)
        return super().close()

        
        


    
    