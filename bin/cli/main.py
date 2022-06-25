from bottle import route, run

@route('/')
def index():
	return f'<b>Hello GFG</b>!'

run(host='0.0.0.0', port=8000,debug=True)
