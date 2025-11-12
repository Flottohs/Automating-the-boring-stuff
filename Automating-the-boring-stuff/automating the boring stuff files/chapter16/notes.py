# ============================================================
# SQLite with Python Notes
# ============================================================

# Import the sqlite3 module
import sqlite3
import pprint  # For pretty-printing query results

# ------------------------------------------------------------
# 1. Connecting to a Database
# ------------------------------------------------------------
# Create a Connection object for a SQLite database stored in 'example.db'.
# If the file doesn't exist, SQLite will create it.
conn = sqlite3.connect('example.db', isolation_level=None)  # autocommit mode

# ------------------------------------------------------------
# 2. Creating Tables
# ------------------------------------------------------------
# Creating a table 'cats' with columns for name, birthdate, fur, and weight.
# NOT NULL ensures a value must be provided.
# STRICT enforces type checking for columns.
conn.execute('''
CREATE TABLE IF NOT EXISTS cats (
    name TEXT NOT NULL,
    birthdate TEXT,
    fur TEXT,
    weight_kg REAL
) STRICT
''')

# Data types in SQLite:
# - NULL
# - INTEGER
# - REAL
# - TEXT
# - BLOB (binary large object)

# ------------------------------------------------------------
# 3. Viewing Tables and Columns
# ------------------------------------------------------------
# List all tables
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
# View info about columns in 'cats' table
conn.execute('PRAGMA table_info(cats)').fetchall()

# ------------------------------------------------------------
# 4. CRUD Operations
# ------------------------------------------------------------
# CRUD = Create, Read, Update, Delete
# Insert new rows into the table
conn.execute("INSERT INTO cats VALUES ('Fluffy', '2010-06-01', 'long', 4.5)")
conn.execute("INSERT INTO cats VALUES ('Mittens', '2012-09-15', 'short', 3.2)")

# Read/query data
conn.execute('SELECT * FROM cats').fetchall()

# Loop through query results
for row in conn.execute('SELECT * FROM cats'):
    print('Row data:', row)
    print(f"{row[0]} is one of my favorite cats")

# Filtering
conn.execute('SELECT * FROM cats WHERE fur="short"').fetchall()

# Ordering results
conn.execute('SELECT * FROM cats ORDER BY fur').fetchall()
conn.execute('SELECT * FROM cats ORDER BY weight_kg DESC').fetchall()
conn.execute('SELECT * FROM cats ORDER BY fur ASC, birthdate DESC').fetchall()

# Limiting results
conn.execute('SELECT * FROM cats LIMIT 3').fetchall()
conn.execute('SELECT * FROM cats LIMIT 3 OFFSET 3').fetchall()  # Skip first 3 rows

# Update rows
conn.execute('UPDATE cats SET fur="gray tabby" WHERE name="Fluffy"')
conn.execute('UPDATE cats SET fur="orange and white" WHERE fur="white and orange"')

# Delete rows
conn.execute('DELETE FROM cats WHERE name="Fluffy"')

# ------------------------------------------------------------
# 5. Transactions
# ------------------------------------------------------------
# BEGIN starts a transaction
conn.execute('BEGIN')
conn.execute('INSERT INTO cats VALUES ("Socks", "2022-04-04", "white", 4.2)')
conn.execute('INSERT INTO cats VALUES ("Mittens", "2023-05-12", "black", 3.8)')
conn.rollback()  # Undo the transaction
# Commit transaction
conn.execute('INSERT INTO cats VALUES ("Fluffy", "2022-10-30", "gray", 4.5)')
conn.commit()

# ------------------------------------------------------------
# 6. SQL Injection Protection
# ------------------------------------------------------------
# Use ? placeholders to prevent SQL injection attacks
cat_name = 'Zophie'
cat_bday = '2021-01-24'
fur_color = 'black'
cat_weight = 5.6
conn.execute(
    'INSERT INTO cats VALUES (?, ?, ?, ?)',
    (cat_name, cat_bday, fur_color, cat_weight)
)

# ------------------------------------------------------------
# 7. Indexes
# ------------------------------------------------------------
# Create index to speed up queries
conn.execute('CREATE INDEX idx_name ON cats(name)')
conn.execute('CREATE INDEX idx_birthdate ON cats(birthdate)')
# Drop index
conn.execute('DROP INDEX idx_name')
conn.execute('DROP INDEX idx_birthdate')

# ------------------------------------------------------------
# 8. Foreign Keys and Multiple Tables
# ------------------------------------------------------------
conn.execute('PRAGMA foreign_keys = ON')
conn.execute('''
CREATE TABLE IF NOT EXISTS vaccinations (
    vaccine TEXT,
    date_administered TEXT,
    administered_by TEXT,
    cat_id INTEGER,
    FOREIGN KEY(cat_id) REFERENCES cats(rowid)
) STRICT
''')

# Join tables
conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id').fetchall()

# ------------------------------------------------------------
# 9. In-Memory Databases
# ------------------------------------------------------------
memory_db_conn = sqlite3.connect(':memory:', isolation_level=None)
memory_db_conn.execute('CREATE TABLE test (name TEXT, number REAL)')
memory_db_conn.execute('INSERT INTO test VALUES ("foo", 3.14)')

# Backup in-memory database to file
file_db_conn = sqlite3.connect('test.db', isolation_level=None)
memory_db_conn.backup(file_db_conn)

# ------------------------------------------------------------
# 10. Backups
# ------------------------------------------------------------
conn.backup('backup.db')

# ------------------------------------------------------------
# 11. Altering/Dropping Tables
# ------------------------------------------------------------
# Add new column
conn.execute('ALTER TABLE cats ADD COLUMN color TEXT')
# Drop table
conn.execute('DROP TABLE cats')

# ------------------------------------------------------------
# 12. Export Database
# ------------------------------------------------------------
# Export SQL statements to file
with open('sweigartcats-queries.txt', 'w', encoding='utf-8') as fileObj:
    for line in conn.iterdump():
        fileObj.write(line + '\n')

# ============================================================
# End of SQLite Notes
# ============================================================

# ------------------------------------------------------------
# Practice Questions:
# 1. How do you connect to a SQLite database in Python?
# 2. How do you create a table with TEXT columns?
# 3. How to insert data safely to prevent SQL injection?
# 4. What is a foreign key and how do you use it?
# 5. How to back up a database or copy to memory?
# 6. What does the STRICT keyword do?
# 7. How do you query/filter/order/limit data?
# 8. What does CRUD stand for?
# 9. What does ACID stand for?
# 10. How do you create and delete an index?