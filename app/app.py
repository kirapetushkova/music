# app.py
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from models import db, User, Musician, Album
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object('config.Config')  # Load configuration settings

# Initialize the database
db.init_app(app)
migrate = Migrate(app, db)

# Initialize session manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # No changes here

# Load user by ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home page (selection of user mode)
@app.route('/')
def home():
    return render_template('index.html')

# Login page (for staff members)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

# Dashboard for authorized staff members
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Catalog page for customers (view musicians and albums)
@app.route('/catalog')
def catalog():
    musicians = Musician.query.all()
    return render_template('catalog.html', musicians=musicians)

# Logout for staff members
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
