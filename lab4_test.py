import time
import unittest
import http.client
from urllib.parse import urlsplit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Lab4Test(unittest.TestCase):
    def setUp(self):
        # Создание новой Firefox сессии
        s = Service("C:\\PyWork\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # Перейти на домашнюю страницу приложения
        self.base_url = "https://veratales.com/"
        self.driver.get(self.base_url)
        # Проверка заголовка домашней страницы
        self.assertTitle("Veratales")

    def assertTitle(self, title):
        self.assertEqual(self.driver.title.find(title), 0, "Ошибка при проверке заголовка сайта")

    def goToNextPage(self):
        # Получаем кнопку для перехода на следующую страницу и кликаем
        next_button = self.driver.find_element(By.CSS_SELECTOR, ".pagination .page-item a[href]")
        next_button.click()

    def test_blog(self):
        # Получаем список постов с главной страницы
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".updates-card-header a[href]")
        links = []

        # Проходимся по элементам и формируем массив с ссылками
        for item in elements:
            links.append(item.get_attribute('href'))

        # Проверка на количество ссылок
        assert len(links) == 10, len(links)

        # Проверка что все посты открываются, т.е. код 200
        for href in links:
            host = urlsplit(href)
            conn = http.client.HTTPSConnection(host.netloc, timeout = 8)
            conn.request("HEAD", host.path)
            res = conn.getresponse()

            assert res.status == 200, "Как минимум один из постов не открывается"

        self.goToNextPage()
        assert self.driver.current_url == "https://veratales.com/?page=2", "Ошибка пагинации"

        self.goToNextPage()
        assert self.driver.current_url == "https://veratales.com/?page=3", "Ошибка пагинации"

    def tearDown(self):
        time.sleep(3)
        # Закрываем окно браузера
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings = "ignore")