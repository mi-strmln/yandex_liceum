from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    engineering = False
    if 'инженер' in prof or 'строитель' in prof:
        engineering = True
    return render_template('training.html', engineering=engineering)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof_list = ["инженер-исследователь",
                 "пилот",
                 "строитель",
                 "экзобиолог",
                 "врач",
                 "инженер по терраформированию",
                 "климатолог",
                 "специалист по радиационной защите",
                 "астрогеолог", "гляциолог",
                 "инженер жизнеобеспечения",
                 "метеоролог",
                 "оператор марсохода",
                 "киберинженер",
                 "штурман",
                 "пилот дронов"
                 ]
    return render_template('list_prof.html', l_type=list, prof_list=prof_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        "title": "И на Марсе будут яблони цвести!",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "мужской",
        "motivation": "Всегда мечтал застрять на Марсе",
        "ready": True
    }
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
