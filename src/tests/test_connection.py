import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from src.connection import Data

@pytest.fixture(scope='session')
def app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app

@pytest.fixture
def db_connection(app):
    original_create = Data.create_connection

    def patched_create(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(':memory:')
        if not self.db.open():
            raise ConnectionError("Cannot open in-memory database")
        query = QSqlQuery()
        query.exec(
            "CREATE TABLE IF NOT EXISTS m_pass ("
            "ID integer primary key AUTOINCREMENT, "
            "Title VARCHAR(50), " 
            "Login VARCHAR(50), " 
            "Password VARCHAR(100), "
            "Url VARCHAR(200), "
            "Created VARCHAR(20) NOT NULL)"
        )
        query.exec("CREATE INDEX IF NOT EXISTS idx_title ON m_pass (Title)")
        return True

    Data.close_connection = patched_create #TODO ()
    Data._instance = None
    data = Data()
    Data.create_connection = original_create
    yield data
    data.close_connection()


@pytest.fixture
def clean_db(db_connection):
    query = QSqlQuery()
    query.exec("DELETE FROM m_pass")
    return db_connection

def test_add_note(clean_db):
    data = clean_db
    query = data.add_new_note_query("Title1", "login1", "pass1", "url1")
    assert query is not None
    
    select = QSqlQuery("SELECT COUNT(*) FROM m_pass WHERE Title='Title1'")
    select.next()
    assert select.value(0) == 1

def test_update_note(clean_db):
    data = clean_db
    data.add_new_note_query("Old", "log", "oldpass", "oldurl")
    q = QSqlQuery("SELECT ID FROM m_pass WHERE Title='Old'")
    q.next()
    note_id = q.value(0)
    data.update_note_query("New", "newlog", "newpass", "newurl", note_id)

    q = QSqlQuery(f"SELECT Title, Login, Password, Url FROM m_pass WHERE ID={note_id}")
    q.next()
    assert q.value(0) == "New"
    assert q.value(1) == "newlog"
    assert q.value(2) == "newpass"
    assert q.value(3) == "newurl"

def test_delete_note(clean_db):
    data = clean_db
    data.add_new_note_query("Del", "x", "y", "z")
    q = QSqlQuery("SELECT ID FROM m_pass WHERE Title='Del'")
    q.next()
    note_id = q.value(0)
    data.delete_note_query(note_id)
    q = QSqlQuery(f"SELECT COUNT(*) FROM m_pass WHERE ID={note_id}")
    q.next()
    assert q.value(0) == 0
