import unittest


class FakeTests(unittest.TestCase):
    def test_fake_user_creation(self):
        print("Проверка создания пользователя: Успешно")
        self.assertTrue(True)  # Всегда проходит

    def test_fake_authentication(self):
        print("Проверка аутентификации: Успешно")
        self.assertTrue(True)  # Всегда проходит

    def test_fake_database_connection(self):
        print("Проверка подключения к базе данных: Ошибка подключения к базе данных")
        # Здесь ошибка симулируется
        self.assertTrue(False, "Ошибка: невозможно подключиться к базе данных")

    def test_fake_api_response(self):
        print("Проверка ответа API: Успешно")
        self.assertTrue(True)  # Всегда проходит


if __name__ == "__main__":
    unittest.main()
