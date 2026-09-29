import sqlite3
connection = sqlite3.connect("bank.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row)
for row in rows:
    print("ID:", row[0])
    print("Holder:", row[1])
    print("Number:", row[2])
    print("Type:", row[3])
    print("Balance:", row[4])
    print("----------------")
    
for row in rows:
    print("Account Holder:", row[0])
    
connection.close()