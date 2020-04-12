# Flask

Flask is a micro web framework written in Python. 
Flask has three main dependencies. The routing, debugging, and Web Server
Gateway Interface (WSGI) subsystems come from Werkzeug; the template
support is provided by Jinja2; and the command-line integration comes from
Click.


### Install

Create a project folder:
```
mkdir myproject
cd myproject
```

Create an environment:
```
python3 -m venv venv (On Windows) or
sudo apt-get install python3-venv (Linux)
```

Activate the environment: 
```
venv\Scripts\activate (On Windows) or 
venv/bin/activate (Linux) 
```

Install Flask: 
```
pip install Flask
```
Running on [http://127.0.0.1:5000](http://127.0.0.1:5000/) (Press CTRL+C to quit) 

For MySQL:
```
sudo apt get install mysl-server libmysqlclient-dev or
pip install flask-mysqldb
```

For SQLAlchemy:
```
pip install flask-sqlalchemy

in Python Console: 
from app import db
db.create_all()
from app import User, Post
user_1 = User(username='test', email='test@test.com', password='password')
db.session.add(user_1)
db.session.commit()
User.query.all()
User.query.first()
User.query.filter_by(username='test').all()
User.query.filter_by(username='test').first()

user = User.query.filter_by(username='test').all()
user.id // 1
user = User.query.get(1)
user.posts // []

post_1 = Post(title='Article One', text='Lorem ipsum dolor sit amet...', user_id=user.id)
db.session.add(post_1)
db.session.commit()

// drop db table rows
db.drop_all()
db.create_all()
User.query.all() // []
Post.query.all() // []

# Не работает!!!
user.posts

for post in user.posts:
   print(post.title)

post = Post.query.first()

post.user_id
post.author
```

Install for Forms:
```
pip install Flask-WTF
```

Install Flask Bootstrap:
```
pip install flask-bootstrap
```
Install all the requirements:
```
$ pip install -r requirements.txt
```

Flask allows you to register environment variables that you want to be automatically 
imported when you run the flask command. To use this option you have to install the python-dotenv package:
```
(venv) $ pip install python-dotenv
```

Flask-CLI:
```
pip install flask-cli
```

Bcrypt (for generating strong hashing values in Python)
```
pip install flask-bcrypt

in Python Console: 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('')
```


### Useful Links
* [https://flask.palletsprojects.com/en/1.1.x](https://flask.palletsprojects.com/en/1.1.x/) - Flask documentation
* [https://github.com/pallets/flask](https://github.com/pallets/flask) - Open source
* [https://www.tutorialspoint.com/flask](https://www.tutorialspoint.com/flask/index.htm) - Flask tutorial
* [https://pythonhosted.org/Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/) - Flask Bootstrap
* https://github.com/pallets/flask/tree/1.1.2/examples/tutorial
