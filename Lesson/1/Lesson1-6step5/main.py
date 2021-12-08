from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input0 = browser.find_elements(By.TAG_NAME, "input")
    for element in input0:
        element.send_keys("Hello!")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
