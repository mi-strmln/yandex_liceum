from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")

@app.route("/distribution")
def distribution():
    members = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин"
    ]
    return render_template("distribution.html", members=members)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
