# necessary imports
from dotenv import load_dotenv
import sqlite3

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

# configure genai api key and choo
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro")


def getResponse(question, prompt):
    response = model.generate_content([prompt, question])
    return response.text


def sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = f"""
### Instruction: Given a natural language description, generate the corresponding SQL query.
The table is STUDENT and not STUDENTS
It has columns ROLL_NO, NAME, CLASS, SECTION, MARKS AND ROLL_NO IS UNIQUE
You need to write the SQL QUERIES FOR THIS TABLE ONLY
donot start any query with sql keyword .. i mean no sql queries start with that
Here are a few examples for some other tables

### Example 1:
Description: Retrieve the names of employees who work in the Sales department.
SQL Query: SELECT name FROM employees WHERE department = 'Sales';

### Example 2:
Description: Insert a new student named Alice with a grade of A and an age of 14 into the students table.
SQL Query: INSERT INTO students (name, grade, age) VALUES ('Alice', 'A', 14);

### Example 3:
Description: Update the price of all products in the Electronics category by reducing it by 10%.
SQL Query: UPDATE products SET price = price * 0.9 WHERE category = 'Electronics';

### Example 4:
Description: Delete all orders from the orders table where the order date is before January 1, 2023.
SQL Query: DELETE FROM orders WHERE order_date < '2023-01-01';

### Example 5:
Description: Create a new table called customers with columns for id (which is the primary key), name, email (which must be unique), and the date the record was created.
SQL Query: CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, created_at DATE);

### Additional Examples:

### Example 6:
Description: Add a new column called salary of type INTEGER to the employees table.
SQL Query: ALTER TABLE employees ADD COLUMN salary INTEGER;

### Example 7:
Description: Calculate the average salary of employees who work in the Engineering department.
SQL Query: SELECT AVG(salary) FROM employees WHERE department = 'Engineering';

### Example 8:
Description: Create an index on the order_date column of the orders table to improve query performance.
SQL Query: CREATE INDEX idx_order_date ON orders(order_date);

### Example 9:
Description: Retrieve the name and age of students who have a grade of A.
SQL Query: SELECT name, age FROM students WHERE grade = 'A';

### Example 10:
Description: Delete a customer from the customers table where the id is 5.
SQL Query: DELETE FROM customers WHERE id = 5;
"""


st.set_page_config(page_title="Retreive SQL")
st.header("Gemini API to retreive SQL Data")
question = st.text_input("Input", key="input")
submit = st.button("Ask me the Question")

if submit:
    response = getResponse(question, prompt)
    print(response)
    data = sql_query(response, "student.db")
    st.subheader("The response is ")
    for row in data:
        print(row)
        st.header(row)
