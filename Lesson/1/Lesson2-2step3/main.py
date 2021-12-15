import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input = browser.find_element(By.CSS_SELECTOR, 'h2 span:nth-child(2)')
    x = input.text
    input = browser.find_element(By.CSS_SELECTOR, 'h2 span:nth-child(4)')
    y = input.text
    
    answer = str(int(x) + int(y))
        
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)
    
    time.sleep(1)

    click_button = browser.find_element(By.CLASS_NAME, "btn")
    click_button.click()

    


finally:
    time.sleep(15)
    browser.quit()
