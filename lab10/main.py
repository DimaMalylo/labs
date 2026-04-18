import unittest

# --- 1. MathTool ---
class MathTool:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return None
        return a / b

# --- 2. LibraryItem ---
class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def details(self):
        return f"{self.title} by {self.author}, {self.year}"

# --- 3. NotificationService і UserManager ---
class NotificationService:
    def send(self, user_id, message):
        # Реальна логіка тут не потрібна
        print(f"Send to {user_id}: {message}")

class UserManager:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notify_user(self, user_id, message):
        self.notification_service.send(user_id, message)

# --- 4. Функція check_even ---
def check_even(number):
    return number % 2 == 0

# --- 5. Тести ---
class TestMathTool(unittest.TestCase):
    def setUp(self):
        self.tool = MathTool()

    def test_add(self):
        self.assertEqual(self.tool.add(5,3), 8)

    def test_subtract(self):
        self.assertEqual(self.tool.subtract(10,4), 6)

    def test_multiply(self):
        self.assertEqual(self.tool.multiply(7,6), 42)

    def test_divide_normal(self):
        self.assertEqual(self.tool.divide(10,2), 5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.tool.divide(5,0))

class TestLibraryItem(unittest.TestCase):
    def test_details(self):
        item1 = LibraryItem("Python 101", "John Doe", 2020)
        item2 = LibraryItem("AI Basics", "Jane Smith", 2023)
        self.assertEqual(item1.details(), "Python 101 by John Doe, 2020")
        self.assertEqual(item2.details(), "AI Basics by Jane Smith, 2023")

class TestUserManager(unittest.TestCase):
    def test_notify_user_calls_send(self):
        class MockService:
            def __init__(self):
                self.called_with = None
            def send(self, user_id, message):
                self.called_with = (user_id, message)

        mock_service = MockService()
        manager = UserManager(mock_service)
        manager.notify_user("user123", "Hello!")
        self.assertEqual(mock_service.called_with, ("user123", "Hello!"))

class TestCheckEven(unittest.TestCase):
    def test_check_even_multiple_cases(self):
        test_cases = [
            (2, True),
            (3, False),
            (0, True),
            (-4, True),
            (-5, False)
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(check_even(number), expected)

# --- Запуск тестів ---
if __name__ == "__main__":
    unittest.main()