from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect


### Our apps name:
app = Flask(__name__)

# login_required decorator to ensure a user is logged in
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			return redirect (url_for('login'))
	return wrap

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
	return render_template('login.html')



if __name__ == "__main__":
	app.run(debug=True)