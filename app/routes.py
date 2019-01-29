from flask import render_template
from app import app, mongo

@app.route('/')
@app.route('/index')
def index():
    posts = list(mongo.db.posts.find())
    print(type(posts))
    return render_template('index.html', title='Home', posts=posts)

@app.route('/post')
def post():
    return render_template('post.html', title='Posts')
