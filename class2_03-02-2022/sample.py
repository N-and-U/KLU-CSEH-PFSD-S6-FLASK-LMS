from flask import Flask, render_template

app = Flask(__name__)

course = [
    {
        'id':'20TS1234',
        'name':'TS-PFSD',
        'LTPS':'0-0-8-0',
        'Credits': 4
    },
    {
        'id':'20CS1234',
        'name':'CNS',
        'LTPS':'4-0-4-0',
        'Credits': 4
    },
    {
        'id':'20AI1234',
        'name':'AIDS',
        'LTPS':'2-0-4-2',
        'Credits': 6
    }
]

@app.route('/')
def home():
    return render_template("home.html", title='home')
@app.route('/login')
def login():
    return render_template("login.html", title='Login')
@app.route('/courses')
def courses():
    return render_template("courses.html", title='courses')
@app.route('/submissions')
def submissions():
    return render_template("submissions.html", title='submissions')
@app.route('/grades')
def grades():
    return render_template("grades.html", title='grades')
@app.route('/logout')
def logout():
    return render_template("logout.html", title='logout')
@app.route('/subjects')
def subjects():
    return render_template("subjects.html", title='subjects', cours=course)
@app.route('/contact')
def contact():
    return render_template("contact.html", title='contact')

if __name__ == '__main__':
    app.run(debug=True)
