import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def get_time_fun():
    return math.log(int(time.time()))
# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link)

button = browser.find_element(By.ID, "ember32")
button.click()
input1 = browser.find_element(By.NAME, "login")
input1.send_keys("Your email")
input2 = browser.find_element(By.NAME, "password")
input2.send_keys("Your password")
button1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button1.click()
time.sleep(1)
anser_filed = browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')
anser_filed.send_keys(get_time_fun())
time.sleep(1)
submit_btn = browser.find_element(By.CLASS_NAME, "submit-submission")
submit_btn.click()


time.sleep(10)
browser.quit()

