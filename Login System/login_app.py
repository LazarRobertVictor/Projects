from flask import Flask, render_template, request, session, redirect
from passlib.hash import pbkdf2_sha256 as hasher

app = Flask(__name__)
app.secret_key = 'your-secret-key'

users = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and hasher.verify(password, users[username]):
            session['username'] = username
            return redirect('/home')
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template('register.html', error='Username already exists')

        hashed_password = hasher.hash(password)
        users[username] = hashed_password

        return render_template('login.html', message='Registration successful. You can now log in.')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
