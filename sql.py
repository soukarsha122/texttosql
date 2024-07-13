import sqlite3

## Connector
connection = sqlite3.connect("student.db")

# Cursor
cursor = connection.cursor()

# Table Creation
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (ROLL_NO VARCHAR(25),NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT, UNIQUE(ROLL_NO));
"""
cursor.execute(table_info)

# Records Insertion
insert_record = """
INSERT OR IGNORE INTO STUDENT (ROLL_NO, NAME, CLASS, SECTION, MARKS) VALUES (?,?,?,?,?)
"""
records_to_insert = [
    ("1", "Soukarsha", "AI", "A", "100"),
    ("2", "Rohan", "ECE", "A", "89"),
    ("3", "Anurag", "Civil", "A", "99"),
    ("4", "Chittadip", "CS", "B", "77"),
    ("5", "Debanshu", "CS", "B", "70"),
]
cursor.executemany(insert_record, records_to_insert)

# Display the records
display_records = """
SELECT * FROM STUDENT
"""
print("The inserted records are: ")

data = cursor.execute(display_records)

for row in data:
    print(row)

# Close connection
connection.commit()
connection.close()
