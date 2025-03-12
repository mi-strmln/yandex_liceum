from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def root():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!<br>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась"
                    height=500 width=500>
                    <br>Вот она какая, красная планета.
                  </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for("static", filename="img/mars.jpg")}"
        alt="Фото Марса украл НЛО"
        height=250 width=250>
        <div class="alert alert-dark" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-dark" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-warning" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-danger" role="alert">       
            Присоединяйся!
        </div>
    </body>
</html>"""


@app.route("/choice/<planet_name>")
def choice(planet_name):
    reasons = {"меркурий": {"reason0": "На этой планете обнаружен лед",
                            "reason1": "Ее магнитное поле снижает радиацию",
                            "reason2": "На ней огромные запасы солнечной энергии",
                            "reason3": "Ее гравитация больше, чем у Луны",
                            "reason4": "Наконец, она просто красивая"},
               "венера": {"reason0": "Эта планета похoжа на Землю",
                          "reason1": "На ней есть атмосфера",
                          "reason2": "Она близка к Земле",
                          "reason3": "На ней можно житьв аэростатах",
                          "reason4": "Наконец, она просто красивая"},
               "марс":
                   {"reason0": "Эта планета близка к Земле",
                    "reason1": "На ней много необходимых ресурсов",
                    "reason2": "На ней есть вода и атмосфера",
                    "reason3": "На ней есть небольшое магнитное поле",
                    "reason4": "Наконец, она просто красивая"}
               }
    return f"""<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
        <title>Выбор планеты</title>
    </head>
    <body>
        <h1>Моё предложение: {planet_name.capitalize()}</h1>
        <h4>{reasons[planet_name.lower()]['reason0']};<h4>
        <div class="alert alert-success" role="alert">
            {reasons[planet_name.lower()]['reason1']};
        </div>
        <div class="alert alert-dark" role="alert">
            {reasons[planet_name.lower()]['reason2']};
        </div>
        <div class="alert alert-warning" role="alert">
            {reasons[planet_name.lower()]['reason3']};
        </div>
        <div class="alert alert-danger" role="alert">
            {reasons[planet_name.lower()]['reason4']}!
        </div>

    </body>
</html>
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
