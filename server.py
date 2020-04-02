from flask import Flask, render_template, redirect, url_for, request
from data_articles import Articles
from forms import RegistrationForm

app = Flask(__name__)

Articles = Articles()
app.secret_key = 'development key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def articles():
    return render_template('blog/articles.html', articles=Articles)

@app.route('/blog/<int:id>/')
def article(id):
    return render_template('blog/article.html', id=id, articles=Articles)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    return render_template('login/register.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)
