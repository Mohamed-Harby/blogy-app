from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from mysql.connector import connect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e09baada403749a37849125116b7ac4e0d47b706'


# secret key is used for protections against cross sites requests and modifying cookies.


def db(sqlquery):
    con = connect(host='localhost',
                  database='blogy',
                  user='root',
                  password='root')
    cur = con.cursor()
    cur.execute(sqlquery)
    records = cur.fetchall()
    con.commit()
    con.close()
    return records


def create_user(user_name, email, password):
    return db(f"insert into user values(0, '{user_name}', '{email}', '{password}', null)")


def update_profile_photo(photo, user_id):
    return db(f"update user set photo='{photo}' where user_id={user_id}")


def create_post(user_id, title, content, visibility):
    return db(f"insert into post values(0, {user_id}, '{title}', '{content}', 0, 0, 0, '{visibility}', now())")


def react(user_id, post_id, emotion):
    if emotion == 'idea':
        db(f"update post set idea_emotion = idea_emotion + 1 where id={post_id}")
    elif emotion == 'like':
        db(f"update post set like_emotion = like_emotion + 1 where id={post_id}")
    elif emotion == 'dislike':
        db(f"update post set dislike_emotion = dislike_emotion + 1 where id={post_id}")

    return db(f"insert into emotion values({user_id}, {post_id}, '{emotion}')")


def get_all_posts():
    return db(f"select * from post")


def get_user_posts(user_id):
    return db(f"select * from post where user_id={user_id}")


def add_friend(user_id, friend_id):
    return db(f"insert into friendship values({user_id}, {friend_id})"), db(
        f"insert into friendship values({friend_id}, {user_id})")


def get_friends(user_id):
    db(f"select second_friend_id from friendship where first_friend_id={user_id}")


def get_friends_posts(friend_id):
    return db(f"select * from post where user_id={friend_id}")


def get_posts_by_trending():
    return db(f"select * from post where visibility='public' order by idea_emotion + like_emotion + dislike_emotion desc")


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
    # create_user('moharby', 'mo@2.com', '123')
    # create_post(1, 'life', 'life is a game', 'public')
    app.run(debug=True)

