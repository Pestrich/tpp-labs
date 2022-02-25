import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Lab2Test(unittest.TestCase):
    def setUp(self):
        # Создание новой Firefox сессии
        s = Service("C:\\PyWork\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # Перейти на домашнюю страницу приложения
        self.base_url = "https://www.artlebedev.ru/case/"
        self.driver.get(self.base_url)
        # Проверка заголовка домашней страницы
        self.assertTitle("Конвертер регистров")

    def assertTitle(self, title):
        self.assertEqual(self.driver.title, title)

    def changeMethodTab(self, tab_id):
        # Получаем таб метода по id и кликаем по нему
        method_tab = self.driver.find_element(By.CSS_SELECTOR, "[data-val^='" + str(tab_id) + "']")
        self.driver.execute_script("arguments[0].click();", method_tab)

    def getTargetValue(self):
        # Получаем текстовое поле результата и его значение
        target = self.driver.find_element(By.ID, "target")

        return target.get_attribute('value')

    def writeInSource(self):
        # Получаем текстовое поле источника и записываем строку
        source = self.driver.find_element(By.ID, "source")
        source.send_keys("ТеСтОвАя СтРоКа.")

    def test_converter_upper_case(self):
        self.changeMethodTab(0)
        self.writeInSource()

        target_value = self.getTargetValue()

        # Проверка значения
        assert target_value == "ТЕСТОВАЯ СТРОКА.", "Верхний регистр - не пройдено"

    def test_converter_lower_case(self):
        self.changeMethodTab(1)
        self.writeInSource()

        target_value = self.getTargetValue()

        # Проверка значения
        assert target_value == "тестовая строка.", "Нижний регистр - не пройдено"

    def test_converter_capital_letters(self):
        self.changeMethodTab(2)
        self.writeInSource()

        target_value = self.getTargetValue()

        # Проверка значения
        assert target_value == "Тестовая Строка.", "Заглавные буквы - не пройдено"

    def test_converter_case_inversion(self):
        self.changeMethodTab(3)
        self.writeInSource()

        target_value = self.getTargetValue()

        # Проверка значения
        assert target_value == "тЕсТоВаЯ сТрОкА.", "Инверсия регистра - не пройдено"

    def test_converter_on_proposals(self):
        self.changeMethodTab(4)
        self.writeInSource()

        target_value = self.getTargetValue()

        # Проверка значения
        assert target_value == "Тестовая строка.", "По предложениям - не пройдено"

    def tearDown(self):
        # Закрываем окно браузера
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()