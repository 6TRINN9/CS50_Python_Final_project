# 🔐 Password Manager

An application for secure password storage and generation with a graphical interface on **PySide6**. 
All data is stored in a local **SQLite** database. All CRUD operations, header search, and a built-in cryptographic password generator with an assessment of their entropy and durability are supported.

[Video of the app's work]
(https://youtu.be/FvWbDHgureo)  

## 📋 Content

- [Features](#-features)
- [Technologies](#-technologies)
- [Project structure](#-project-structure)
- [Database](#-database)
- [Manual](#-manual)
  - [Main window](#-main-window)
  - [Creating an entry](#-creating-an-entry)
  - [Password Generator](#-password-generator)
  - [Editing and deleting](#-editing-and-deleting)
  - [Search](#-search)
- [Possible improvements](#-possible-improvements)

---

## ✨ Features

- ✅ **Full-fledged account management**  
  Title, login, password, URL, date of creation/modification.

- 🔄 **Password Generating**  
  - Length from 1 to 30+ characters (slider)  
  - Choice of character types: `a-z`, `A-Z`, `0-9`, punctuation characters
  - Cryptographic randomness (`secrets` + `shuffle`)

- 📊 **Password strength assessment**
- Calculation of entropy (bits) based on the actual character classes used  
  - Quality scale: `Pathetic' (<20 bits), `Weak` (20-50), `Good` (50-60) `Strong` (60-100), `Excellent' (>100)

- 🗄️ **Local storage**
SQLite with automatic table and index creation.

- 🔍 **Real-time title search**

- 🖱️ **User-friendly interface**  
  Table with row selection, confirmation of deletion.
  
---

## 🧰 Technologies

| Component          | Technology                     |
|-------------------|--------------------------------|
| GUI               | PySide6 (Qt6 для Python)       |
| The database       | SQLite through QtSql             |
| Generating numbers   | `secrets`,  `math.log2`        |
|                   | `random.SystemRandom`
| Date              | `datetime`                     |

---

## 📁 Project structure

- password-manager/
- src/
  - icons/                  # GUI icons
  - PySide_UI/              # raw UI files from PySide6 disigner
    - Main.ui
    - New_note.ui
    - Password_Generator.ui
  - ui/                     # compiled UI files
    - ui_main.py
    - Res_rc_rc.py
    - Res_rc.qrc
    - ui_new_note.py
    - ui_generator.py
  - tests/
    - test_connection.py
    - test_utils.py
  - connection.py           # the Data singleton class for working with databases
  - utils.py                # password generation, entropy, evaluation
  - W_new_note.py           # record creation dialog
  - W_edit_note.py          # editing dialog
- W_generator.py            # password generator dialog
- main.py                   # main window (QMainWindow)
  - manager_db.db           # SQLite file (created automatically)
- preview/                  # images example of an interview
- requirements.txt          # imports

---

## 🗄️ Database
The m_pass table has the following structure:
| Field    | Type        | Description                              |
|---------|------------|--------------------------------------------|
| ID      | INTEGER (PK) | Auto-increment primary key               |
| Title   | VARCHAR(50) | The title (for example, "Google.com")     |
| Login   | VARCHAR(50) | User name / email                         |
| Password| VARCHAR(100)| Password (stored in clear text)           |
| Url     | VARCHAR(200)| Website address                           |
| Created | VARCHAR(20) | Date in ISO format (YYYY-MM-DD)           |

---

## 🖥️ Manual

### Main window

After launching, a table opens with all saved records sorted by creation date (new ones first).  
The `ID` column is hidden, but is used for editing/deleting.

The Toolbar:

- **Create** – opens the dialog for adding an entry
- **Edit** – changes the selected line
- **Delete** – deletes the highlighted line (with confirmation prompt)
- **Search** – field for filtering by title (case-insensitive)

### Create an entry

1. Click **"Create"**.
2. Fill in the fields:
   - **Title** – required (recommended)
   - **Login** – login or email
   - **Password** – you can enter it manually or click on the "Generate" button
   - **Url** – web address
3. Click **"Create"**.  
   The `Created` date will be set automatically for the current day.

### Password Generator

When creating or editing an entry, click on the "Generate" button. A dialog opens:

![Generator window](https://docs/generator.png)

- **Length** – adjustable by slider, displayed by a number.
- **Character set** – select the desired types (at least one).
- **🔄** – generate a new password.
- **Password field** – displays the generated password.
- **Entropy** – for example, `Entropy: 78.45 bit'.
- **Rating** – `Strength: Strong'.

Click **"OK"** to insert the password into the main form.

> 💡 **The Council:** For maximum durability, use a length of at least 12 characters and all 4 types of characters.

### Edit and delete

- **Editing:** select the line → "Edit" → change the data → "Edit".  
  The `Created` date will be updated to the current one.
- **Removal:** select the line → "Delete" → confirm. The record will disappear.

### Search

Start typing in the **Search** field – the table is instantly filtered by the `Title` field.  
Clear the field to show all entries.

---

## 🚧 Possible improvements

List of ideas:

- 🔐 **Password encryption**.
- 📤 **Export/import with encryption**.
- 🏷️ **Categories / Tags**.
- 🛡️ **Password verification for compromise**.
- 🌙 **Custom interface themes**.
- 🧩 **Auto-completion of forms on the website**.
