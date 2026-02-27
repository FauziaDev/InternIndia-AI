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
for i in range(1, 11):
    print(f"t{i} = {f.getvalue(f't{i}')}<br>")
print("</body></html>")


regno = f.getvalue('t1')
sname = f.getvalue('t2')
contno = f.getvalue('t3')
dob = f.getvalue('t4')
email = f.getvalue('t5')
gender = f.getvalue('t6')
address = f.getvalue('t7')
reg_date = f.getvalue('t8')
pic = f.getvalue('t9')
pid = f.getvalue('t10')

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
    query = """INSERT INTO student_registration 
    (regno, sname, contno, dob, email, gender, address, reg_date, pic, pid) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    values = (regno, sname, contno, dob, email, gender, address, reg_date, pic, pid)

    cursor.execute(query, values)
    conn.commit()

    print("<html><body><h2>Data Inserted Successfully into student_registration!</h2></body></html>")

except Exception as e:
    print(f"<html><body><h2>Error: {e}</h2></body></html>")

finally:
    cursor.close()
    conn.close()