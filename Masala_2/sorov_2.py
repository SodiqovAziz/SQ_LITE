import sqlite3

conn = sqlite3.connect('MILLIY_TAOMLAR.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT * FROM ovqat
    WHERE taom_masaliqlari LIKE '%guruch%'
''')

natijalar = cursor.fetchall()

print("ID | Taom nomi | Masalliqlar")
print("-" * 40)
for taom in natijalar:
    print(f"{taom[0]:<3} | {taom[1]:<10} | {taom[2]}")

conn.close()
