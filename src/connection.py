from datetime import date
from PySide6 import QtSql
from PySide6.QtWidgets import QMessageBox

class Data:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self):
        # Check if the instance has already been initialized
        if not hasattr(self, 'db'):
            self.db = None
            self.create_connection()

    def create_connection(self):
        """
        Creates a connection to the database and initializes the table.
        """
        try:
            self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('manager_db.db')

            if not self.db.open():
                raise ConnectionError(f"Cannot open database: {self.db.lastError().text()}")

            query = QtSql.QSqlQuery()
            success = query.exec(
                "CREATE TABLE IF NOT EXISTS m_pass (" 
                "ID integer primary key AUTOINCREMENT, " 
                "Title VARCHAR(50), " 
                "Login VARCHAR(50), " 
                "Password VARCHAR(100), " 
                "Url VARCHAR(200), " 
                "Created VARCHAR(20) NOT NULL" 
                ")"
            )
            if not success:
                raise RuntimeError(f"Table creation failed: {query.lastError().text()}")
            
            self.create_index()
            return True
        except Exception as ex:
            QMessageBox.critical(self, "Critical error", f"Error create connection: {ex}")

    def create_index(self):
        """
        Creates the necessary indexes to optimize queries.
        """
        query = QtSql.QSqlQuery()
        index_name, table_name, column_name = "idx_title", "m_pass", "Title"
        success = query.exec(f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_name})")
        
        if not success:
            raise RuntimeError(f"Failed to create index {index_name}: {query.lastError().text()}")
        return True

    
    def execute_query_with_params(self, sql_query, query_values=None):
        """
        Executes a SQL query with parameters. Returns the query object or None on error.
        """
        try:
            query = QtSql.QSqlQuery()

            if not query.prepare(sql_query):
                raise ValueError(f"Query preparation failed: {query.lastError().text()}")
                

            if query_values is not None:
                for query_val in query_values:
                    query.addBindValue(query_val)

            if not query.exec():
                raise ValueError(f"Query execution failed: {query.lastError().text()}")
            
            return query
        except Exception as ex:
            QMessageBox.critical(self, "Critical error", f"Error execute: {ex}")
    
    
    def add_new_note_query(self, title, login, password, url):
        """
        Adds a new note to the database.
        """
        sql_query = (
            "INSERT INTO m_pass (Title, Login, Password, Url, Created) " \
            "VALUES (?, ?, ?, ?, ?)"
        )

        # Creted date
        today = date.today().isoformat()
    
        return self.execute_query_with_params(sql_query, [ title, login, password, url, today])
    
    def update_note_query(self, title, login, password, url, note_id):
        """
        Updates an existing transaction by ID.
        """
        sql_query = (
            "UPDATE m_pass "\
            "SET Title=?, Login=?, Password=?, Url=?, Created=? " \
            "Where ID=?"
        )
        # Modified date
        today = date.today().isoformat()
        return self.execute_query_with_params(sql_query, [ title, login, password, url, today, note_id])
    
    def delete_note_query(self, note_id):
        """
        Deletes a transaction by ID.
        """
        sql_query = "DELETE FROM m_pass WHERE ID=?"
        return self.execute_query_with_params(sql_query, [note_id])
    
    
    
    def close_connection(self):
        """
        Closes the connection to the database.
        """
        if self.db and self.db.isOpen():
            self.db.close()