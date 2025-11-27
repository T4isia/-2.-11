import unittest


from reg_exe import coincidence
from url_work import ddmmyyyy_from_my_url


class TestFromMyUrl(unittest.TestCase):
    # Проверяет, что функция возвращает строку (если URL доступен)

    def test_real_url(self):
        url = (
    "https://gist.githubusercontent.com/T4isia/"
    "4c9540e947791a1c2a6755097b77ea4c/raw/"
    "6a8b9b2fb89e8fbd34bc07cb35d8e2d96d1b3c5c/gistfile1.txt"
        )
        result = ddmmyyyy_from_my_url(url)
        self.assertTrue(isinstance(result, (str, type(None))))

    # Проверяет обработку несуществующего URL
    def test_invalid_url(self):
        url = "https://nope-nope-nope-404-404-404.com/"
        result = ddmmyyyy_from_my_url(url)
        self.assertIsNone(result) # это метод unittest, который проверяет None


# Coincidence
class TestFindDates(unittest.TestCase):

    # 1. Проверка валидатных дат
    def test_valid_dates(self):
        data = "22.12.2022 11.11.2011 19.07.1978"
        results = [m for m in coincidence(data)]
        self.assertIn("22.12.2022", results)
        self.assertIn("11.11.2011", results)
        self.assertIn("19.07.1978", results)

    # 2. Проверка невалидных дат неправильные: день, месяц, год, 29 февраля в високосном году
    def test_invalid_dates(self):
        data = "33.12.2012 10.22.2020 09.04.2200 29.02.2025"
        results = [m for m in coincidence(data)]
        self.assertEqual(results, [])

    # 3. Проверка високосного года
    def test_leap_year(self):
        data = "29.02.2024"
        results = [m for m in coincidence(data)]
        self.assertIn("29.02.2024", results)


# Тест с консольным вводом
class TestConsoleInput(unittest.TestCase):

    def test_console_input(self):
        data = "10.05.2007"
        results = [m for m in coincidence(data)]
        self.assertEqual(results, ["10.05.2007"])


if __name__ == "__main__":
    unittest.main()
