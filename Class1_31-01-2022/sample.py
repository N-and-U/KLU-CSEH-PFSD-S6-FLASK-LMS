from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>welcome to kl lms</h1>'
@app.route('/login')
def login():
    return '<h1>login page </h1>'
@app.route('/courses')
def courses():
    return '<h1>courses page </h1>'
@app.route('/submissions')
def submissions():
    return '<h1>submissions page </h1>'
@app.route('/grades')
def grades():
    return '<h1>grades page </h1>'
@app.route('/logout')
def logout():
    return '<h1>logout page </h1>'
@app.route('/contact')
def contact():
    return '<h1>contact page </h1>'

if __name__ == '__main__':
    app.run(debug=True)
