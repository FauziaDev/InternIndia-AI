 #!C:/Users/aiman/AppData/Local/Programs/Python/Python310-32/python.exe
import cgi, html, mysql.connector, sys, traceback

def fail(msg):
    """सभी एरर एक ही फ़ॉर्मेट में दिखाएँ"""
    print("Content-Type: text/html")
    print()                      # header ↔ body separator
    print(f"<h1>Server Error</h1><pre>{html.escape(msg)}</pre>")
    sys.exit(0)

try:
    form = cgi.FieldStorage()

    cid         = form.getfirst("t1", "").strip()
    cname       = form.getfirst("t2", "").strip()
    duration    = form.getfirst("t3", "").strip()
    description = form.getfirst("t4", "").strip()

    if not all([cid, cname, duration, description]):
        fail("Form fields missing – चारों t1..t4 अनिवार्य हैं")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#mysql@2027",
        database="stud_prog"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO student_registration (cid, cname, duration, description) "
        "VALUES (%s, %s, %s, %s)",
        (cid, cname, duration, description)
    )
    conn.commit()
    cur.close()
    conn.close()

    print("Content-Type: text/html")
    print()
    print("<h2>डेटा सफलतापूर्वक इन्सर्ट हुआ!</h2>")

except Exception:
    # पूरा traceback लॉग में, समरी यूज़र को
    traceback.print_exc()         # apache error.log के लिए
    fail("Unexpected exception – error.log देखें")
