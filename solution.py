from flask import Flask, render_template
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")


@app.route("/table/<gender>/<int:age>")
def table(gender, age: int):
    if gender == "female" and age > 21:
        color = "#fd6767"
    elif gender == "female" and age < 21:
        color = "#fd67ee"
    elif gender == "male" and age > 21:
        color = "#1f53fd"
    else:
        color = "#50ecf7"
    is_adult = age > 21
    return render_template("table.html", wall_color=color, is_adult=is_adult)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
