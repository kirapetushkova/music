import unittest
from app import app

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_register_user(self):
        # Тестируем регистрацию пользователя
        response = self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)  # Успешная регистрация
        self.assertIn('User registered', response.get_data(as_text=True))

    def test_login_user(self):
        # Тестируем логин пользователя
        self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.app.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)  # Успешный логин
        self.assertIn('access_token', response.get_data(as_text=True))
