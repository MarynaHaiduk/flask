from flask import render_template, redirect, url_for, request
from main import app

from main.data_articles import Articles
from main.forms import RegistrationForm

Articles = Articles()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def articles():
    return render_template('blog/articles.html', articles=Articles)

@app.route('/blog/<int:id>/')
def article(id):
    return render_template('blog/article.html', id=id, articles=Articles)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    return render_template('login/register.html', form=form)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.is_submitted():
        result=request.form
        return render_template('sucess.html', result=result)
    return render_template('login/signup.html', form=form)
