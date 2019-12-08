# Fourteenth Day Exercise
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return 'This is the Index page'

@app.route('/hello')
def helloWorld():
	return 'Hello World!'

@app.route('/members')
def members():
	return 'Members Page!'
#==============================================================================
@app.route('/marks')
@app.route('/marks/')
@app.route('/marks/<mark>')
def mark(mark = 0):
	mark = int(mark)
	if mark >= 90:
		score = 'got A'
	elif mark >= 80 and mark < 90:
		score = 'got B'
	elif mark >= 70 and mark < 80:
		score = 'got C'
	elif mark >= 60 and mark < 70:
		score = 'got D'
	else:
		score = 'failed'
	return render_template('marks.html', title='Marks', score = score)
#==============================================================================
@app.route('/academy')
def academy():
	return render_template('academy.html')
	
if __name__ == '__main__':
	app.run()