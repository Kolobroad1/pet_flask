from flask import Flask, render_template
#import flask.views
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_moment import Moment 
from flask_bootstrap import Bootstrap
from datetime import datetime
#
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import ContactForm


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
	return render_template('hello.html', name=name, num_list=num_list, current_time=datetime.utcnow())

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
	return render_template('/bootstrap/base.html', current_time=datetime.utcnow())

app.add_url_rule('/test', 'test') # there is how to work with parameters
app.view_functions['test'] = test
#=========================================================
@app.errorhandler(404)
def page_not_found(e):
	return render_template('errors/404.html', e=e, current_time=datetime.utcnow()), 404

#=====================================
@app.route('/login', methods=['GET', 'POST'])
def login():
	username, password = '', ''
	message = ''
	if request.method == 'POST':
		username = request.form.get('usern')
		password = request.form.get('passw')

	if username == "pepe" and password == "pepe":
		message = "Correct username and password"
		return redirect(f'/about/{username}')
	else:
		message = f"Wrong username - {username} or password{password}"

	return render_template('login.html', message=message, current_time=datetime.utcnow())
#===============================================
@app.route('/login_wtf', methods=['GET', 'POST'])
def login_wtf():
	form = ContactForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		message = form.message.data
		print(name)
		print(email)
		print(message)
		if name == 'sasuke' and email == 'pepe@pe':
			print("\nData received. Now redirecting ...")
			return redirect('/')
	return render_template('login_wtf.html', form=form)

@app.route('/responser/')
def responser():
	response = make_response('<h1>RESPONSE<h1>', 200)
	response.headers['Content-Type'] = 'text/plain'
	response.headers['Server'] = 'SasukeUchiha'

	response.set_cookie("favorite-font", "sans-serif", 60*60)
	return response

@app.route('/render')
def render():
	name, age = "sasuke", 10
	current_time = datetime.utcnow()
	ctx_render = dict(name=name, age=age, current_time=current_time)
	return render_template("render.html", **ctx_render)
#---app.add_url_rule('/', 'index', index) =>
# == app.view_functions['index'] = index | if without third =>
# => arg  add_url_rule(rule, endpoint)
