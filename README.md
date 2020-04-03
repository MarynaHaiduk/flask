# Flask

Flask is a micro web framework written in Python. 
It aims to keep the core of an application simple yet extensible.
Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
Flask supports the extensions to add such functionality to the application.

##### WSGI
Web Server Gateway Interface has been adopted as a standard for Python web application development. 
WSGI is a specification for a universal interface between the web server and the web applications.

##### Werkzeug
It is a WSGI toolkit, which implements requests, response objects, and other utility functions. 
This enables building a web framework on top of it. 

##### Jinja2
Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.


## Installing

##### Install virtual Python environment:
```
pip install virtualenv or
sudo apt-get install virtualenv
```

Once installed, new virtual environment is created in a folder.
```
mkdir newproj
cd newproj
virtualenv venv
```
To activate corresponding environment 
```
venv/bin/activate (Linux/OS X) or 
venv\scripts\activate (On Windows)
```

##### Install Flask and update using pip:
```
pip install Flask
```
Running on [http://127.0.0.1:5000](http://127.0.0.1:5000/) (Press CTRL+C to quit) 

##### Install MySQL:
```
sudo apt get install mysl-server libmysqlclient-dev or
pip install flask-mysqldb
```

##### Forms:
```
pip install Flask-WTF
```

##### Flask Bootstrap:
```
pip install flask-bootstrap
```

### Useful Links
* [https://flask.palletsprojects.com/en/1.1.x](https://flask.palletsprojects.com/en/1.1.x/) - Flask documentation
* [https://github.com/pallets/flask](https://github.com/pallets/flask) - Open source
* [https://palletsprojects.com/p/flask](https://palletsprojects.com/p/flask/) - Flask website
* [https://www.tutorialspoint.com/flask](https://www.tutorialspoint.com/flask/index.htm) - Flask tutorial
* [edureka](https://www.youtube.com/watch?v=lj4I_CvBnt0) - Python Flask tutorial for beginners
* [https://stackoverflow.com/questions](https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502) - Generate secret key
https://www.tutorialspoint.com/flask/flask_routing.htm
* [https://pythonhosted.org/Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/) - Flask Bootstrap