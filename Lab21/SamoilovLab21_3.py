import time
from selenium import webdriver
# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome()

# Пауза в выполнении программы
time.sleep(5)

# Открытие веб-страницы
driver.get("https://www.bsuir.by/ru/obratnaya-svyaz")
time.sleep(5)

# Ввод текста в текстовое поле
textarea = driver.find_element_by_name("newprop_14537_1")
textarea.send_keys("Александр")

# Ввод текста в поле для имени пользователя
textarea = driver.find_element_by_name("newprop_14538_1")
textarea.send_keys("Какой-то мой номер телефона")

textarea = driver.find_element_by_name("newprop_14539_1")
textarea.send_keys("Как отчислиться")

time.sleep(5)

submit_button = driver.find_element_by_css_selector("#fb_button")
submit_button.click()
time.sleep(5)
driver.quit()