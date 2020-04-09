from flask import Flask, render_template
from blog_data import Articles


app = Flask(__name__)
data = Articles()

@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html', data=data)

@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
