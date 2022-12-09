from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value").text
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button1 = browser.find_element(By.ID, "solve")
    button1.click()

    word = browser.switch_to.alert.text
    print(word)
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])
    current_window = browser.current_window_handle

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()