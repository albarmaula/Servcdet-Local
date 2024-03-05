from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def user(username):
    return f'{username}\'s profile'

@app.route('/admin')
def admin():
    return redirect(url_for("user", username="Admin!"))

# Create a WSGI application callable
def create_wsgi_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
