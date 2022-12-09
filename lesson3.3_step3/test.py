
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By

def Test(url):
    browser = webdriver.Chrome()
    browser.get(url)
    elements = [".first_block .first", ".first_block .second", ".first_block .third"]
    values = ["Ivan", "Petrov", "ya@mail.ru"]
    for i in range(len(elements)):
        input2 = browser.find_element(By.CSS_SELECTOR, elements[i]).send_keys(values[i])

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    browser.quit()
    return welcome_text

class TestMy(unittest.TestCase):
    def test_1(self):
        text = Test("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", text)

    def test_2(self):
        text = Test("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", text)

if __name__ == '__main__':
    unittest.main()