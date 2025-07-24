import re
from flask import Flask, render_template, request, redirect, url_for

app = Flask(Flask)

# A simple mock database of users (replace with your real database)
users = {
    "admin": "Password123!",
    "user1": "MyPassword1@",
}

# Password validation function
def is_valid_password(password):
    # Regex to ensure the password is at least 8 characters long, has at least one uppercase letter, one symbol, and one number
    password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(password_regex, password):
        return True
    return False

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the password meets the criteria
    if not is_valid_password(password):
        error_message = "Password must be at least 8 characters long, contain one uppercase letter, one symbol, and one number."
        return render_template('login.html', error=error_message)

    # Check if the username and password are correct
    if username in users and users[username] == password:
        return redirect(url_for('dashboard'))
    else:
        # If login fails, show an error message
        error_message = "Invalid username or password"
        return render_template('login.html', error=error_message)

@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the Dashboard!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
