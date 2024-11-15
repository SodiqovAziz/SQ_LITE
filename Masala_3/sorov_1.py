import sqlite3

# BOZOR database-ga ulanish
conn = sqlite3.connect('BOZOR.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS meva (
        id INTEGER PRIMARY KEY,
        meva_nomi TEXT NOT NULL,
        meva_narxi REAL NOT NULL,
        meva_turi TEXT NOT NULL
    )
''')

mevalar = [
    (1, 'Olma', 5000, 'Shirin'),
    (2, 'Olma', 5500, 'Shirin'),
    (3, 'Banan', 15000, 'Tropik'),
    (4, 'Anor', 12000, 'Nordon'),
    (5, 'Anor', 12500, 'Shirin'),
    (6, 'Uzum', 9000, 'Shirin'),
    (7, 'Uzum', 9500, 'Shirin'),
    (8, 'Shaftoli', 8000, 'Shirin'),
    (9, 'Behi', 7000, 'Shirin'),
    (10, 'Limon', 6000, 'Nordon')
]

cursor.executemany('''
    INSERT OR IGNORE INTO meva (id, meva_nomi, meva_narxi, meva_turi)
    VALUES (?, ?, ?, ?)
''', mevalar)

conn.commit()

cursor.execute('''
    DELETE FROM meva
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM meva
        GROUP BY meva_nomi
    )
''')

conn.commit()

cursor.execute('SELECT * FROM meva')
natijalar = cursor.fetchall()

print("ID | Meva nomi | Meva narxi | Meva turi")
print("-" * 40)
for meva in natijalar:
    print(f"{meva[0]:<3} | {meva[1]:<10} | {meva[2]:<9} | {meva[3]}")

conn.close()
