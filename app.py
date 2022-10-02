from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quem-somos.html")

if __name__ == "__main__":
    app.run()
