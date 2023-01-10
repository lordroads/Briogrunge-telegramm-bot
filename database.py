import sqlite3
import database.questions as questions

connect = sqlite3.connect('briodata.db')
cursore = connect.cursor()

cursore.execute("DROP TABLE questions")
connect.commit()

cursore.execute("CREATE TABLE IF NOT EXISTS questions( id INTEGER, question TEXT, answer TEXT, PRIMARY KEY (id) )")
connect.commit()

questions.add_question('question1', 'answer1')
# entity_1 = ['question1', 'answer1']
# cursore.execute("INSERT INTO questions VALUES (NULL,?,?);", entity_1)
# connect.commit()
#
questions.add_question('question2', 'answer2')
questions.update_question('test2', 'answer_test2', 2)
questions.delete_question(2)
# entity_2 = ['question2', 'answer2']
# cursore.execute("INSERT INTO questions VALUES (NULL,?,?);", entity_2)
# connect.commit()
print(questions.get_answer_by_question('question1'))
# cursore.execute("SELECT * FROM questions")
#
# all_test = cursore.fetchall()
all_test = questions.get_all()
print(all_test)

# for q in all_test:
#     print(f'{q[0]} , {q[1]} , {q[2]}')
#
# new_all_test = dict((y, z) for x, y, z in all_test)
# print(new_all_test)

