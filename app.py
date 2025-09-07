from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Nueva página de ejemplo: lanzamiento de moneda
@app.route("/moneda")
def moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return f"<h1>Salió: {resultado}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
