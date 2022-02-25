import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class SearchText(unittest.TestCase):
    def setUp(self):
        # Создание новой Firefox сессии
        s = Service("C:\\PyWork\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # Перейти на домашнюю страницу приложения
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        # Получаем поле поиска
        self.search_field = self.driver.find_element(By.NAME, "q")

        # Вводим слова для поиска и отправляем запрос
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        # Получаем список элементов, которые отображаются после поиска
        lists = self.driver.find_elements(By.CLASS_NAME, "g")
        self.assertEqual(11, len(lists))

    def tearDown(self):
        # Закрываем окно браузера
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()