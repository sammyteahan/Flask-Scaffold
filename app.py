from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect, session


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
@login_required
def home():
	return render_template('index.html', name=session.get('username'))

@app.route('/login', methods=["GET", "POST"])
def login():
	error = ''

	if request.method = 'POST':
		if request.form['user'] == 'admin'
			session['username'] = request.form['user']
			session['logged_in'] = True
			return redirect(url_for('home'))
		else:
			error = 'Invalid credentials'

	return render_template('login.html')

# For session based authentication
@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('logged_in', None)
	return redirect(url_for('login'))



if __name__ == "__main__":
	app.run(debug=True)