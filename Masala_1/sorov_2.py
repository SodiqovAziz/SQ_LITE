import sqlite3

conn = sqlite3.connect('UNIVERSITET.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT talaba_kursi, COUNT(*) as talaba_soni
    FROM talaba
    GROUP BY talaba_kursi
    ORDER BY talaba_kursi
''')

kurslar = cursor.fetchall()

print("Kurs | Talabalar soni")
print("-" * 20)
for kurs in kurslar:
    print(f"{kurs[0]:<4} | {kurs[1]:<4}")

conn.close()
