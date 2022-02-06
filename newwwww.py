from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства',
           'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.',
           'И начнем с Марса!',
           'Присоединяйся!']
    return '<br>'.join(lst)


@app.route('/image_mars')
def image():
    return f"""
    <!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src={url_for('static', filename='img/mars.png')} alt="должен был быть Марс">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                    rel="stylesheet" 
                    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class='text-danger'>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.png')} alt="должен был быть Марс">
                    <div class="alert-dark" role="alert">
                      <br><h3>Человечество вырастает из детства.</h3>
                    </div>
                    <div class="alert-success" role="alert">
                      <br><h3>Человечеству мала одна планета.</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h3>И начнем с Марса!</h3>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h3>Присоединяйся!</h3>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
