import sqlite3
def connect_to_db():
    connection = sqlite3.connect("notepad.db")
    return connection
def create_notes_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255) NOT NULL,
            text TEXT NOT NULL,
            created_at DATETIME NOT NULL
        );
    """)
    connection.commit()
def add_note(connection, title, text):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO notes (title, text, created_at)
        VALUES (?, ?, ?);
    """, (title, text, datetime.now()))
    connection.commit()
def get_all_notes(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    return notes
def get_note_by_id(connection, id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (id,))
    note = cursor.fetchone()
    return note
def update_note(connection, id, title, text):
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE notes
        SET title = ?,
            text = ?,
            created_at = ?
        WHERE id = ?;
    """, (title, text, datetime.now(), id))
    connection.commit()
def delete_note(connection, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
    connection.commit()
def main():
    connection = connect_to_db()

    # Створення таблиці
    #create_notes_table(connection)

    # Додавання нотатки
    #add_note(connection, "Перша нотатка", "Це моя перша но
