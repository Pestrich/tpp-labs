import time
import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Lab3Test(unittest.TestCase):
    def setUp(self):
        # Создание новой Firefox сессии
        s = Service("C:\\PyWork\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # Перейти на домашнюю страницу приложения
        self.base_url = "https://yandex.ru/"
        self.driver.get(self.base_url)
        # Проверка заголовка домашней страницы
        self.assertTitle("Яндекс")

    def assertTitle(self, title):
        self.assertEqual(self.driver.title, title)

    def writeInSearchField(self, value):
        # Получаем поле поиска и записываем строку
        search_field = self.driver.find_element(By.NAME, "text")
        search_field.send_keys(value)
        search_field.submit()

    def test_search_system(self):
        self.writeInSearchField("Hello")
        time.sleep(3)
        self.writeInSearchField("World")
        time.sleep(2)

        # Получаем список элементов, которые отображаются после поиска
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".serp-item.desktop-card h2")

        count = 0

        # Проходимся по элементам
        for item in elements:
            if item.text.find("HelloWorld") >= 0:
                count += 1

        # Проверка на наличие сайтов со словосочетанием HelloWorld
        assert count > 0, "Отсутствуют сайты со словосочетанием HelloWorld"

    def tearDown(self):
        # Закрываем окно сайта через 5-6 секунд
        time.sleep(random.randint(5,6))
        # Закрываем окно браузера
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()