#! C:\Users\aiman\AppData\Local\Programs\Python\Python310-32\python.exe
print("Content-Type: text/html\r\n\r\n")
import cgi
#!/usr/bin/python

print("Content-Type: text/html\n")

import cgi
import mysql.connector

# Step 1: Get form data
f = cgi.FieldStorage()
print("<html><body>")
for i in range(1, 5):
    print(f"t{i} = {f.getvalue(f't{i}')}<br>")
print("</body></html>")








pid = f.getvalue('t1')
regno= f.getvalue('t2')
course = f.getvalue('t3')
sem = f.getvalue('t4')

# Step 2: Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",                      # your MySQL username
        password="#mysql@2027",                      # your MySQL password
        database="stud_prog"              # correct DB name (as seen in your image)
    )
    cursor = conn.cursor()

    # Step 3: Insert query
    query = """INSERT INTO stud_enrollment 
    (pid, regno, course, sem) 
    VALUES (%s, %s, %s, %s)"""
    
    values = (pid, regno, course, sem)

    cursor.execute(query, values)
    conn.commit()

    print("<html><body><h2>Data Inserted Successfully into stud_enrollment!</h2></body></html>")

except Exception as e:
    print(f"<html><body><h2>Error: {e}</h2></body></html>")

finally:
    cursor.close()
    conn.close()