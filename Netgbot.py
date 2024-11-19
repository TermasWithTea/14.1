import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGET, 
    balance INTEGER NOT NULL)
''')
users = []
for i in range(1, 11):
    username = f'User{i}'
    email = f'ecample{i}@gmail.com'
    age = i*10
    balance = 1000
    users.append((username, email, age, balance))

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)', users)
cursor.execute('''UPDATE Users
SET balance == 500
WHERE id IN(SELECT id FROM Users WHERE(id+1)% 2 = 0) 
''')

cursor.execute('''
DELETE FROM Users
WHERE id IN(SELECT id FROM Users WHERE(id+2)%3 = 0)
''')
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age !=60')
row = cursor.fetchall()

for rows in row:
    print(f'Имя: {row[0]}| Почта:{row[1]}| Возраст:{row[2]}| Баланс:{row[3]}')

connection.commit()
connection.close()