from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("Student_Registration.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
