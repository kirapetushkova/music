# app.py
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from models import db, User, Musician, Album
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))



# Инициализация приложения
app = Flask(__name__)
app.config.from_object('config.Config')  # Подключаем конфигурацию

# Инициализация базы данных
db.init_app(app)
migrate = Migrate(app, db)

# Инициализация менеджера сессий
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Загрузка пользователя по ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Главная страница (выбор режима работы)
@app.route('/')
def home():
    return render_template('index.html')

# Страница авторизации (для сотрудников)
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

# Страница для авторизованных пользователей (сотрудников)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Страница для покупателей (просмотр исполнителей и альбомов)
@app.route('/catalog')
def catalog():
    musicians = Musician.query.all()
    return render_template('catalog.html', musicians=musicians)

# Выход из системы (для сотрудников)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
