import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    input = browser.find_element(By.TAG_NAME, 'img')
    x = input.get_attribute('valuex')
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()

    button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button.click()

    time.sleep(1)

    click_button = browser.find_element(By.CLASS_NAME, "btn")
    click_button.click()

    


finally:
    time.sleep(15)
    browser.quit()
