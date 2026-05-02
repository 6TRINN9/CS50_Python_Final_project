from PySide6 import QtWidgets

from ui.ui_generator import Ui_Password_generator



class W_generator(QtWidgets.QDialog):
    def __init__(self):       
        super(W_generator, self).__init__() 
        self.ui = Ui_Password_generator()
        self.ui.setupUi(self)
        self.show()

        
        


    
    