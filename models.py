import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)''')
    c.execute('''INSERT INTO users (username) VALUES ('admin'), ('guest')''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database diinisialisasi.")