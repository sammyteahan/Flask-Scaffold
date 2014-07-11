from flask import Flask 
from flask import render_template
from flask import request, url_for, redirect


### Our apps name:
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
	return render_template('login.html')



if __name__ == "__main__":
	app.run(debug=True)