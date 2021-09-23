from flask import Flask
import flask.views


app = Flask(__name__)

#@app.route('/')
def index():
	return '<h1>HELLO WORLD<h1>'

app.add_url_rule('/', 'index')
app.view_functions['index'] = index

def hello(name):
	return f'<h1>HELLO {name}<h1>'

app.add_url_rule('/about/<name>', 'hello') # there is how to work with parameters
app.view_functions['hello'] = hello


#app.add_url_rule('/', view_func=MyView.as_view('myview', param1, param2))



#---app.add_url_rule('/', 'index', index) =>
# == app.view_functions['index'] = index | if without third =>
# => arg  add_url_rule(rule, endpoint)
