from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip as pc


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button1 = browser.find_element(By.CLASS_NAME, "btn")
    button1.click()

    current_window = browser.window_handles[1]
    browser.switch_to.window(current_window)


    x_element = browser.find_element(By.ID, "input_value").text
    x = x_element
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    word = browser.switch_to.alert.text
    print(word)
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])
    current_window = browser.current_window_handle

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # link1 = "https://stepik.org/lesson/184253/step/6?unit=158843"
    # browser = webdriver.Chrome()
    # browser.get(link1)
    #
    # input2 = browser.find_element(By.ID, "ember305")
    # input2.send_keys(word)
    #
    # button1 = browser.find_element(By.CSS_SELECTOR, "[class='submit-submission']")
    # button1.click()
    #
    # time.sleep(10)
    # browser.quit()

