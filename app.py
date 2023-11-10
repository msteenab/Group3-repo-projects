from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

import sqlite3


app = Flask(__name__)
app.secret_key = "mahsjdshdssdkdd_ncjdjkl"


# Database initialization function
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


init_db()


# Route for the signin page
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? OR email = ?',
                       (username_or_email, username_or_email))
        user = cursor.fetchone()
        conn.close()

        if user and user['password'] == password:
            flash('signin successful', 'success')  # Display a success message
            return redirect(url_for('index'))
        else:
            # Display an error message
            flash('Invalid username or password', 'error')
    return render_template('signin.html')

# Route for the forgot password page
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        username_or_email = request.form['username or email']
        new_password = request.form['new password']
        confirm_new_password = request.form['confirm new password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? OR email = ?',
                       (username_or_email, username_or_email))
        user = cursor.fetchone()
        conn.close()

        if new_password == confirm_new_password:
            flash('New password set', 'success')  # Display a success message
            return redirect(url_for('signin'))
        else:
            # Display an error message
            flash('Invalid username or password', 'error')
    return render_template('forgot.html')

# Route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for('signin'))
        else:
            # Display an error message
            flash('Passwords do not match', 'error')
    return render_template('signup.html')


# Route for the index page
@app.route('/index')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


# Route for serving static files (CSS, JS, images, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


# Route for "about.html" page
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run(debug=True)
