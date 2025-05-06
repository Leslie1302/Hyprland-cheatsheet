from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cheat_sheet():
    return render_template("cheatsheet.html")

if __name__ == "__main__":
    app.run(debug=True)
