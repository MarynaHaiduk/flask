from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

@app.route('/<name>')
def render_text(name):
    return 'Hello %s' % name

@app.route('/')
def home():
    return render_template('home.html')

# Render list articles
@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

# Render article
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

# About
@app.route('/about')
def about():
    return render_template("about.html")
# app.add_url_rule('about/')

if __name__ == '__main__':
    app.run(debug = True)
