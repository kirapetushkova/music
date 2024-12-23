class TestIntegration(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_and_query_user(self):
        # Регистрация и получение пользователя из базы
        self.app.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.app.get('/user/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', response.get_data(as_text=True))
