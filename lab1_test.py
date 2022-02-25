import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Lab1Test(unittest.TestCase):
    def setUp(self):
        # Создание новой Firefox сессии
        s = Service("C:\\PyWork\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # Перейти на домашнюю страницу приложения
        self.base_url = "http://www.siaxx.com/"
        self.driver.get(self.base_url)
        # Проверка заголовка домашней страницы
        self.assertTitle("nAble, by Siaxx Corporation")

    def assertTitle(self, title):
        self.assertEqual(self.driver.title, title)

    def test_follow_links(self):
        # Получаем все ссылки из меню
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".menulinks a[href]")
        links = []

        # Проходимся по элементам и формируем массив с названиями и ссылками
        for item in elements:
            href = item.get_attribute('href')
            links.append((item.text.lower(), href))

        # Проверка на количество ссылок
        assert len(links) == 3, len(links)

        # Сортировка в алфавитном порядке
        sort_links = sorted(links, key = lambda x: x[0])

        num_of_tabs = 0

        # Открываем вкладки
        for text, href in sort_links:
            num_of_tabs += 1
            self.driver.execute_script('window.open(\"' + href + '\");')
            self.driver.switch_to.window(self.driver.window_handles[num_of_tabs])
            time.sleep(1)

        # Закрываем вкладки начиная с исходного
        for x in range(0, len(links) + 1):
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            time.sleep(1)

    def tearDown(self):
        time.sleep(5)
        # Закрываем окно браузера
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()