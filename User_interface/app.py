from flask import Flask, render_template, request, redirect, url_for
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    phone_number = request.form['phone_number']
    password = request.form['password']

    # Call the automation script with input values
    process = Popen(['python3', 'final_sporty_2nd.py', phone_number, password], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        return redirect(url_for('success'))
    else:
        return 'Login failed!'  # Handle failure case
    

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
