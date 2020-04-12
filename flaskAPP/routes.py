from flask import render_template, url_for, flash, redirect
from flaskAPP import app
from flaskAPP.models import User, Post
from flaskAPP.blog_data import Articles
from flaskAPP.forms import RegistrationForm, LoginForm

data = Articles()

@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html', data=data)

@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('auth/register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@admin.com" and form.password.data == "password":
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Please check username and password", 'danger')
    return render_template('auth/login.html', title='Login', form=form)