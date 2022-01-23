from flask import Flask, render_template, url_for
app = Flask(__name__)


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
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Blogy', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About Page')

# export FLASK_APP=blog-app.py
# export FLASK_DEBUG=on

if __name__ == '__main__':
    app.run(debug=True)
