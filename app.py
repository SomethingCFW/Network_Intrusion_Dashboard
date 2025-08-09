from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


def get_logs():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 50")
    data = cursor.fetchall()
    conn.close()
    return data


@app.route("/")
def index():
    logs = get_logs()
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
