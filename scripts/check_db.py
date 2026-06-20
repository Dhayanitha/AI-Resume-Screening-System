import sqlite3

conn = sqlite3.connect("resume_screening.db")

cursor = conn.cursor()

# show tables
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

print("\nTables:")
for table in tables:
    print(table[0])

# show rankings
print("\nRankings Data:\n")

cursor.execute("SELECT * FROM rankings")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()