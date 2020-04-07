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

##### MySQL
```
sudo apt get install mysl-server libmysqlclient-dev or
pip install flask-mysqldb
```

##### Forms
```
pip install Flask-WTF
```

##### Flask Bootstrap
```
pip install flask-bootstrap
```

### Useful Links
* [https://flask.palletsprojects.com/en/1.1.x](https://flask.palletsprojects.com/en/1.1.x/) - Flask documentation
* [https://github.com/pallets/flask](https://github.com/pallets/flask) - Open source
* [https://www.tutorialspoint.com/flask](https://www.tutorialspoint.com/flask/index.htm) - Flask tutorial
* [edureka](https://www.youtube.com/watch?v=lj4I_CvBnt0) - Python Flask tutorial for beginners
* [https://pythonhosted.org/Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/) - Flask Bootstrap
* https://github.com/pallets/flask/tree/1.1.2/examples/tutorial
