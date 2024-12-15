import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")
#cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", ("user", "ex@gmail.com", "20", "1000"))
#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", (f"user{i}", f"ex{i}@gmail.com", i*10, 1000))

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1000")
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
rows = cursor.fetchall()
for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

cursor.execute("SELECT id FROM Users WHERE id = 6")
if cursor.fetchone():
    cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(f"{total_users} - общее количество пользователей в базе данных")

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(f"{all_balances} - общая сумма баланса у пользователей")

if total_users > 0:
    average_balance = all_balances / total_users
    print(f"{average_balance} - средняя сумма по балансу у пользователей")
else:
    print("Нет пользователей в базе данных.")

connection.commit()
connection.close()