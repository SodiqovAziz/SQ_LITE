import sqlite3

conn = sqlite3.connect('MILLIY_TAOMLAR.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ovqat (
        id INTEGER PRIMARY KEY,
        taom_nomi TEXT NOT NULL,
        taom_masaliqlari TEXT NOT NULL
    )
''')

taomlar = [
    (1, 'Osh', 'Guruch, go`sht, sabzi, piyoz'),
    (2, 'Somsa', 'Un, go`sht, piyoz, yog`'),
    (3, 'Manti', 'Un, go`sht, kartoshka'),
    (4, 'Lagman', 'Un, go`sht, sabzavotlar'),
    (5, 'Shashlik', 'Go`sht, tuz, ziravorlar'),
    (6, 'Norin', 'Guruch, go`sht, piyoz, yogurt'),
    (7, 'Chuchvara', 'Un, go`sht, piyoz'),
    (8, 'Qovurma', 'go`sht, yog`, piyoz'),
    (9, 'Halisa', 'Bug`doy, go`sht, yog`'),
    (10, 'Mastava', 'Guruch, go`sht, sabzi, pomidor')
]

cursor.executemany('''
    INSERT OR IGNORE INTO ovqat (id, taom_nomi, taom_masaliqlari)
    VALUES (?, ?, ?)
''', taomlar)

conn.commit()

cursor.execute('''
    SELECT * FROM ovqat
    WHERE taom_nomi LIKE '%a'
''')

natijalar = cursor.fetchall()

print("ID | Taom nomi | Masalliqlar")
print("-" * 40)
for taom in natijalar:
    print(f"{taom[0]:<3} | {taom[1]:<10} | {taom[2]}")

conn.close()
