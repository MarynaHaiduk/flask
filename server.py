from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from data_articles import Articles
from forms import RegistrationForm
import os # to generate some random sekret key

app = Flask(__name__)

# to generate some random sekret key
my_sekret_key = os.urandom(24)
app.config['SECRET_KEY'] = 'X\x18#L\xeb\xda\xe6nc\x19\xfdU_?\x02\xd4\xbf\xda\xd9\x8b0\x1e?\x8d'

Articles = Articles()

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

if __name__ == '__main__':
    app.run(debug = True)
