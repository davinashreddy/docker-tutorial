from flask import render_template, request
from app import app, mongo

@app.route('/')
@app.route('/index')
def index():
    posts = list(mongo.db.posts.find())
    print(type(posts))
    return render_template('index.html', title='Home', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        author = request.form['username']
        title = request.form['newtitle']
        subtitle = request.form['subtitle']
        content = request.form['content']
        mongo.db.posts.insert({'author': author, 'title': title, 'subtitle': subtitle, 'body': content})
        results = "Successfully published."
        return render_template('post.html', title='Posts', results=results)
    if request.method == 'GET':
        return render_template('post.html', title='Posts')
