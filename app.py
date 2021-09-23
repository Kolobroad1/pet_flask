from flask import Flask, render_template
#import flask.views
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_moment import Moment 
from flask_bootstrap import Bootstrap
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sasuke'
bootstrap = Bootstrap(app)
moment = Moment(app)

#@app.route('/')
def index():
	#user_agent = request.headers.get('User_Agent')
	#response = make_response(f'<h1> Hello {user_agent}, I will send u \
		                     #a  coockie<h1>')
	#response.set_cookie('answ', '42')
	return render_template('index.html', current_time=datetime.utcnow())   # return response == <h1>Somths</h1>, 400 etc..

app.add_url_rule('/', 'index')
app.view_functions['index'] = index
#------------------------------------------------
def hello(name):
	num_list = [1,2,3,4,5,6,7]
	return render_template('hello.html', name=name, num_list=num_list)

app.add_url_rule('/about/<name>', 'hello') # there is how to work with parameters
app.view_functions['hello'] = hello

def aborter():
	abort(404)
	return f'<h1>HELLO {name}<h1>'

app.add_url_rule('/aborter', 'aborter') # there is how to work with parameters
app.view_functions['aborter'] = aborter
#========================================================
def test():
	user = False
	nar = "NARUTO"
	return render_template('/bootstrap/base.html')

app.add_url_rule('/test', 'test') # there is how to work with parameters
app.view_functions['test'] = test
#=========================================================
@app.errorhandler(404)
def page_not_found(e):
	return render_template('errors/404.html', e=e), 404


#---app.add_url_rule('/', 'index', index) =>
# == app.view_functions['index'] = index | if without third =>
# => arg  add_url_rule(rule, endpoint)
