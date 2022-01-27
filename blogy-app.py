from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e09baada403749a37849125116b7ac4e0d47b706'
# secret key is used for protections against cross sites requests and modifying cookies.
posts = [
    {
        'author': 'Mohamed Harby',
        'title': 'importance of data structures',
        'content': 'In computer science, a data structure is a data organization, management, and storage format that '
                   'enables efficient access and modification.',
        'date_posted': 'March 28, 2018'
    },
    {
        'author': 'Salma Harby',
        'title': 'natural numbers',
        'content': 'In mathematics, the natural numbers are those numbers used for counting and ordering. In common '
                   'mathematical terminology, words colloquially used for counting are "cardinal numbers", '
                   'and words used for ordering are "ordinal numbers".',
        'date_posted': 'January 10, 2022'
    },
    {
        'author': 'Gad Fekry',
        'title': 'Agriculture',
        'content': 'Agriculture is the practice of cultivating plants and livestock.[1] Agriculture was the key '
                   'development in the rise of sedentary human civilization, whereby farming of domesticated species '
                   'created food surpluses that enabled people to live in cities. The history of agriculture began '
                   'thousands of years ago.',
        'date_posted': 'Novmber 26, 2020'
    },
    {
        'author': 'Ibrahim Mokhls',
        'title': 'Architecture',
        'content': 'architecture, the art and technique of designing and building, as distinguished from the skills '
                   'associated with construction. The practice of architecture is employed to fulfill both practical '
                   'and expressive requirements, and thus it serves both utilitarian and aesthetic ends.',
        'date_posted': 'Novmber 26, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Blogy', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account for {form.username.data} is created!', 'success')
        # add database verifications here
        return redirect(url_for('home'))
    return render_template('register.html', title='registration page', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # add database verifications here
        flash(f'Welcome {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='login Page', form=form)


# export FLASK_APP=blog-app.py
# export FLASK_DEBUG=on

if __name__ == '__main__':
    app.run(debug=True)
