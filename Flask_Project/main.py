from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/menu.html')
def menu():
    return render_template('menu.html')


@app.route('/signIn.html')
def signIn():
    return render_template('signIn.html')


if __name__ == '__main__':
    app.run(debug=True)
