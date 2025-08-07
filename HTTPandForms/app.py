from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # Optional home page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect(url_for('welcome', username=username))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username', 'Guest')
    return render_template('welcome.html', username=username)
if __name__ == '__main__':
    app.run(debug=True)