import time
from selenium import webdriver
# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome()

# Пауза в выполнении программы
time.sleep(5)

# Открытие веб-страницы
driver.get("http://bga.by/contacts")
time.sleep(5)

# Ввод текста в текстовое поле
textarea = driver.find_element_by_tag_name("textarea")
textarea.send_keys("Мой первый тест через Selenium")

# Ввод текста в поле для имени пользователя
username = driver.find_element_by_id("124158159")
username.send_keys("Здесь введите мое имя")

time.sleep(5)

submit_button = driver.find_element_by_css_selector("#submitFormContacts")
submit_button.click()
time.sleep(5)
driver.quit()