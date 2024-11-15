import sqlite3

conn = sqlite3.connect('BOZOR.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT * FROM meva
    ORDER BY meva_narxi DESC
    LIMIT 5
''')

natijalar = cursor.fetchall()

print("ID | Meva nomi | Meva narxi | Meva turi")
print("-" * 40)
for meva in natijalar:
    print(f"{meva[0]:<3} | {meva[1]:<10} | {meva[2]:<9} | {meva[3]}")

conn.close()
