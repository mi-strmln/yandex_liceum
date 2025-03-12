from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" href="static/css/style.css">
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <header class="centered">
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                            </header>
                            <div>
                                <form class="astreg-form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">                                  
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное (9 классов)</option>
                                          <option>Среднее (11 классов)</option>
                                          <option>СПО</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="professionSelect">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession1" id="professionCheck1" name="profession">
                                            <label for="professionCheck1">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession2" id="professionCheck2" name="profession">
                                            <label for="professionCheck2">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession3" id="professionCheck3" name="profession">
                                            <label for="professionCheck3">Врач</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession4" id="professionCheck4" name="profession">
                                            <label for="professionCheck4">Программист</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession5" id="professionCheck5" name="profession">
                                            <label for="professionCheck5">Биолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession6" id="professionCheck6" name="profession">
                                            <label for="professionCheck6">Метеоролог</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession7" id="professionCheck7" name="profession">
                                            <label for="professionCheck7">Оператор БПЛА</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" value="profession8" id="professionCheck8" name="profession">
                                            <label for="professionCheck8">Специалист по радиационной защите</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="motivation">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="motivation" rows="3" name="motivationt"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == "POST":
        return "Заявка отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
