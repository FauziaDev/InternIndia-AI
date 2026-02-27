#! C:\Users\aiman\AppData\Local\Programs\Python\Python310-32\python.exe

print("Content-Type: text/html\r\n\r\n")

import cgi
import mysql.connector

f = cgi.FieldStorage()
print("<html><body>")
for i in range(1, 3):
    print(f"t{i} = {f.getvalue(f't{i}')}<br>")
print("</body></html>")

userid = f.getvalue("t1")
password = f.getvalue("t2")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",                      # your MySQL username
        password="#mysql@2027",                      # your MySQL password
        database="stud_prog"              # correct DB name (as seen in your image)
    )
    cursor = conn.cursor()

    # Step 3: Insert query
    query = """INSERT INTO login
    
    (userid, password) 
    
    VALUES (%s, %s)"""
    
    values = (userid, password)

    cursor.execute(query, values)
    conn.commit()

    print("<html><body><h2>Data Inserted Successfully into login!</h2></body></html>")

except Exception as e:
    print(f"<html><body><h2>Error: {e}</h2></body></html>")

finally:
    cursor.close()
    conn.close()