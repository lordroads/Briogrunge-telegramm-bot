import sqlite3


connect = sqlite3.connect('briodata.db')
cursore = connect.cursor()

cursore.execute("""CREATE TABLE IF NOT EXISTS 
users( 
    id INTEGER, 
    isBot INTEGER, 
    isAdmin INTEGER,
    firstName TEXT,
    lastName TEXT,
    username TEXT,
    languageCode TEXT,
    PRIMARY KEY (id) 
)""")
connect.commit()


def add_user(user_id: int,
             is_bot: bool,
             is_admin: bool,
             first_name: str,
             last_name: str,
             username: str,
             language_code: str):
    entity = (user_id, is_bot, is_admin, first_name, last_name, username, language_code)
    cursore.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", entity)
    connect.commit()


def get_all() -> []:
    cursore.execute("SELECT * FROM users")
    return cursore.fetchall()


def get_user_by_id(user_id: int) -> tuple:
    cursore.execute("SELECT * FROM users WHERE id = :find_user", {"find_user": user_id})
    return cursore.fetchone()


def update_user(user_id: int,
                is_bot: bool,
                is_admin: bool,
                first_name: str,
                last_name: str,
                username: str,
                language_code: str):
    entity = (is_bot, is_admin, first_name, last_name, username, language_code, user_id)
    cursore.execute("""UPDATE users SET 
    isBot = ?,
    isAdmin = ?,
    firstName = ?,
    lastName = ?,
    username = ?,
    languageCode = ? 
    WHERE id = ?""", entity)
    connect.commit()


def delete_user(user_id: int):
    cursore.execute("DELETE FROM questions WHERE id=:user_id;", {"user_id": user_id})
    connect.commit()
