import sqlite3

conn = sqlite3.connect('UNIVERSITET.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS talaba (
        id INTEGER PRIMARY KEY,
        talaba_ismi TEXT NOT NULL,
        talaba_kursi INTEGER,
        talaba_stipendiyasi REAL
    )
''')

talabalar = [
    (1, 'Ali', 1, 500000),
    (2, 'Vali', 2, 550000),
    (3, 'Olim', 3, 600000),
    (4, 'Nodir', 4, 650000),
    (5, 'Zarina', 1, 520000),
    (6, 'Laylo', 2, 570000),
    (7, 'Dilshod', 3, 610000),
    (8, 'Kamol', 4, 660000),
    (9, 'Aziz', 1, 530000),
    (10, 'Madina', 2, 580000)
]

cursor.executemany('''
    INSERT OR IGNORE INTO talaba (id, talaba_ismi, talaba_kursi, talaba_stipendiyasi)
    VALUES (?, ?, ?, ?)
''', talabalar)

conn.commit()

cursor.execute('''
    UPDATE talaba
    SET talaba_kursi = talaba_kursi + 1
''')

cursor.execute('''
    DELETE FROM talaba
    WHERE talaba_kursi >= 4
''')

conn.commit()

cursor.execute('SELECT * FROM talaba')
talabalar = cursor.fetchall()

print("\nYangilangan jadval:")
print("ID | Talaba ismi | Talaba kursi | Talaba stipendiyasi")
print("-" * 40)
for talaba in talabalar:
    print(f"{talaba[0]:<3} | {talaba[1]:<11} | {talaba[2]:<12} | {talaba[3]:<8} so'm")

conn.close()
