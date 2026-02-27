#! C:\Users\aiman\AppData\Local\Programs\Python\Python310-32\python.exe
print("Content-Type: text/html\r\n\r\n")
import cgi
#!/usr/bin/python

print("Content-Type: text/html\n")


import cgi
import mysql.connector

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Database connect
con = mysql.connector.connect(host="localhost", user="root", password="#mysql@2027", database="stud_prog")
cur = con.cursor()

# Check credentials
cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
row = cur.fetchone()

if row:
    print("success")  # JavaScript will redirect on this
else:
    print("fail")