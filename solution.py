from flask import Flask, render_template, request, redirect, flash
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")


@app.route('/carousel')
def carousel():
    image_folder = os.path.join('static/img')
    images = sorted([f"img/{f}" for f in os.listdir(image_folder)
                     if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    print(images)
    return render_template('carousel.html', images=images)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
