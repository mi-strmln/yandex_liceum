from flask import Flask, url_for, request

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


@app.route("/load_photo", methods=['GET', 'POST'])
def load_photo():
    if request.method == "GET":
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
        <title>Загрузка файла</title>
    </head>
    <body>
        <header class="centered">
            <h1>Загрузка фотографии</h1>
            <h2>для участия в миссии</h2>
        </header>
        <div>
        <form class="astreg-form" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photoChoose">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <div class="form-group">
                <img src="static/img/photo.jpg" alt="Фото не выбрано">
            </div>
            <button type="submit" class="btn btn-primary">Загрузить</button>
        </form>
        </div>        
    </body>
</html>
    """
    elif request.method == "POST":
        f = request.files["file"]
        f.save("static/img/photo.jpg")
        return "ok"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
