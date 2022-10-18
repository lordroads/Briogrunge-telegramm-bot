import sqlite3

connect = sqlite3.connect('briodata.db')
cursore = connect.cursor()

cursore.execute("CREATE TABLE IF NOT EXISTS questions( id INTEGER, question TEXT, answer TEXT, PRIMARY KEY (id) )")
connect.commit()


def add_question(question: str, answer: str):
    question = [question, answer]
    cursore.execute("INSERT INTO questions VALUES (NULL, ?, ?)", question)
    connect.commit()


def get_all() -> {}:
    cursore.execute("SELECT * FROM questions")
    all_questions = dict((y, z) for x, y, z in cursore.fetchall())
    return all_questions


def get_answer_by_question(question: str) -> str:
    cursore.execute("SELECT * FROM questions WHERE question = :find_question", {"find_question": question})
    return cursore.fetchone()[2]


def get_answer_by_id(question_id: int) -> tuple:
    cursore.execute("SELECT * FROM questions WHERE id = :find_question", {"find_question": question_id})
    find_entity = cursore.fetchone()
    return find_entity[2]


def get_question_by_id(question_id: int) -> tuple:
    cursore.execute("SELECT * FROM questions WHERE id = :find_question", {"find_question": question_id})
    return cursore.fetchone()


def update_question(question: str, answer: str, question_id: int):
    data = (question, answer, question_id)
    cursore.execute("UPDATE questions SET question = ?, answer = ? WHERE id = ?", data)
    connect.commit()


def delete_question(question_id: int):
    cursore.execute("DELETE FROM questions WHERE id=:target_id;", {"target_id": question_id})
    connect.commit()
