import unittest
from app.models import db, User  # Предполагаем, что есть объект базы данных и модель User
from app import app

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Настраиваем приложение для тестирования
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Используем in-memory базу
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        # Удаляем тестовую базу данных
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_database_connection(self):
        # Тестируем подключение к базе данных
        self.assertIsNotNone(db.engine)

    def test_user_creation(self):
        # Тестируем создание пользователя
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()
        queried_user = User.query.filter_by(username="testuser").first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, "test@example.com")
