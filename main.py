import mysql
from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="localhost", user="root", password="", database="project")

cursor = conn.cursor()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    # cursor.execute("""SELECT * FROM 'users' WHERE 'email' LIKE {} AND 'password' LIKE {}""").format(email,password)
    # users=cursor.fetchall()
    # cursor.execute( """SELECT * FROM 'details' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}'""".format(email,password))
    # users=cursor.fetchall()
    cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
    users = cursor.fetchall()
    if len(users) > 0:
        return render_template('home.html')
    else:
        return render_template('login.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cursor.execute("""INSERT INTO users(name,email,password) VALUES ('{}','{}','{}')""".format(name, email,password))

    # cursor.execute("INSERT INTO users (name,email,password) VALUES ({},{},{})",
    # (name, email, password))

    # cursor.execute("INSERT INTO users ('name','email','password') VALUES ({},{},{})".format(name, email, password))
    # cursor.execute("INSERT INTO users ('name','email','password') VALUES ({},{},{})".format(name, email, password))
    # cursor.execute('INSERT INTO users VALUES (%s,%s,%s)')

    conn.commit()

    return "user registered"


if __name__ == '__main__':
    app.run(debug=True)
