import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlTableModel

from connection import Data
from ui.ui_main import Ui_MainWindow
from W_new_note import W_new_note
from W_edit_note import W_edit_note

class Password_manager(QMainWindow):
    def __init__(self):
        super(Password_manager, self).__init__()
        self.connection = Data()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()
        self.update_model()
        

    def setup_ui(self):
        """
        Initializing ui with error handling
        """    
        # connect action for buttons
        self.ui.btn_create.clicked.connect(self.create_new_note)
        self.ui.btn_delete.clicked.connect(self.delete_note)
        self.ui.btn_edit.clicked.connect(self.edit_note)
        self.ui.le_search_password.textEdited.connect(self.search_note)

        #settings for tableview
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

    def update_model(self):
        """
        Updating a table model with error handling
        """
        try:
            self.model = QSqlTableModel(self)
            self.model.setTable('m_pass')
            if not self.model.select():
                QMessageBox.critical(self, "DB Error", f"Error loading data: {self.model.lastError().text()}")
                return
            self.ui.tableView.setModel(self.model)
            self.ui.tableView.setColumnHidden(0, True)
            # Automatically adjust column widths
            self.ui.tableView.resizeColumnsToContents()
        except Exception as ex:
            QMessageBox.critical(self, "Critical error", f"Error updating model: {ex}")
       
    def create_new_note(self):
        """
        Creating a new note
        """
        try:
            self.w_new_note = W_new_note(self)            
            self.w_new_note.show()
        except Exception as ex:
            QMessageBox.critical(self, "Error", f"Failed to open compose window: {ex}")

    def get_selected_row_id(self):
        """
        Getting the selected row id
        """
        selected_row = self.ui.tableView.selectionModel().selectedRows()[0].row()
        if selected_row is None:
            QMessageBox.warning(
                self, "Attention", "Please select a record to edit/delete"
            )
        return selected_row

    
    def edit_note(self):
        """
        Editing the selected entry
        """
        try:
            id_row = self.get_selected_row_id()
            self.w_edit_note = W_edit_note(self, id_row)            
            self.w_edit_note.show()
        except Exception as ex:
            QMessageBox.critical(self, "Error", f"Can't open edit window: {ex}")
        

    def delete_note(self):
        """
        Delete the selected entry with confirmation
        """

        id_row = self.get_selected_row_id()

        # Get the ID from the first column (assuming the ID is in the first column)
        cell_index = self.ui.tableView.model().index(id_row, 0)

        if not cell_index.isValid():
            QMessageBox.critical(
                self, "Error", "Failed to get record ID"
            )
            return None

        note_id = str(self.ui.tableView.model().data(cell_index))

        if note_id is None:
            return    
        
        reply = QMessageBox.question(
                    self,
                    "Confirm Delete",
                    f"Are you sure you want to delete the note with ID {note_id}?",
                    QMessageBox.Yes | QMessageBox.No
                )

        if reply == QMessageBox.Yes:
            try:
                if self.connection.delete_note_query(note_id):
                    QMessageBox.information(self, "Success", "Record successfully deleted")
                    self.update_model()
                else:
                    QMessageBox.critical(self, "Error", "Failed to delete record")
            except Exception as ex:
                QMessageBox.critical(self, "Delete error", f"An error occurred: {ex}")
        

    def search_note(self):
        """
        Search records by filter
        """
        search_text = self.ui.le_search_password.text().strip()
        if not search_text:
            self.update_model()
            return
        
        try:
            filter_str = f"title LIKE '%{search_text}%'"
            self.model.setFilter(filter_str)
            if not self.model.select():
                QMessageBox.critical(
                self, 
                "Search Error", f"Search execution error: {self.model.lastError().text()}"
                )
        except Exception as ex:
            QMessageBox.critical(
                self,
                "Search Error", f"Search execution error: {ex}"
            )


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = Password_manager()
        window.show()
        sys.exit(app.exec())
    except Exception as ex:
        QMessageBox.critical(
                None, 
                f"Critical application error", f"The application cannot start: {ex}", 
                sys.exit(1)
        )
