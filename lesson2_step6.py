from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card-body #price"),"$100"))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)

    x1_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = str(x1_element.text)
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    button2 = browser.find_element(By.ID, "solve").click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()