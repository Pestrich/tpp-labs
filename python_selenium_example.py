from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service("C:\\PyWork\\geckodriver.exe")
driver = webdriver.Firefox(service=s)
driver.maximize_window()
driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.close()