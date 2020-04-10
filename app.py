from flask import Flask, render_template, url_for, flash, redirect
from blog_data import Articles
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
data = Articles()
app.config['SECRET_KEY'] = 'X\x18#L\xeb\xda\xe6nc\x19\xfdU_?\x02\xd4\xbf\xda\xd9\x8b0\x1e?\x8d'

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


if __name__ == '__main__':
    app.run(debug=True)
