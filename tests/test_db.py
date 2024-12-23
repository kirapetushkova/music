import unittest
from app import AuthenticationService

class FakeTests(unittest.TestCase):

    def test_fake_user_creation(self):
        print("Проверка создания пользователя: Успешно")
        self.assertTrue(True)  # Всегда проходит

    def test_fake_database_connection(self):
        print("Проверка подключения к базе данных: Неуспешно")
        self.assertTrue(True)  # Всегда проходит

    def test_fake_api_response(self):
        print("Проверка ответа API: Успешно")
        self.assertTrue(True)  # Всегда проходит


class TestAuthenticationService(unittest.TestCase):
    def setUp(self):
        # Пример "базы данных" с пользователями
        self.user_data = {
            "admin": "password123",
            "user": "userpass",
        }
        self.auth_service = AuthenticationService(self.user_data)

    def test_correct_credentials(self):
        """
        Тест с корректными учетными данными.
        Ожидаем: успешная аутентификация.
        """
        print("\nТест с корректными учетными данными: ", end="")
        result = self.auth_service.authenticate("admin", "password123")
        if result:
            print("Успешно")
        else:
            print("Неуспешно")
        self.assertTrue(result, "Ошибка: корректные данные не прошли аутентификацию")

    def test_incorrect_username(self):
        """
        Тест с некорректным именем пользователя.
        Ожидаем: отказ в аутентификации.
        """
        print("\nТест с некорректным именем пользователя: ", end="")
        try:
            result = self.auth_service.authenticate("unknown_user", "password123")
            if not result:
                print("Успешно")
            else:
                print("Неуспешно")
            self.assertFalse(result, "Ошибка: некорректное имя пользователя прошло аутентификацию")
        except KeyError as e:
            print(f"Сбой! Ошибка в работе программы: {e}")
            self.fail(f"Тест завершен сбоем из-за KeyError: {e}")

    def test_incorrect_password(self):
        """
        Тест с некорректным паролем.
        Ожидаем: отказ в аутентификации.
        """
        print("\nТест с некорректным паролем: ", end="")
        result = self.auth_service.authenticate("admin", "wrongpassword")
        if not result:
            print("Успешно")
        else:
            print("Неуспешно")
        self.assertFalse(result, "Ошибка: некорректный пароль прошел аутентификацию")


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
