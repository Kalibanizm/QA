import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element(By.CLASS_NAME, 'btn').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    
    input = browser.find_element(By.CSS_SELECTOR, '#input_value').text
         
    answer = str(math.log(abs(12*math.sin(int(input)))))

    button = browser.find_element(By.ID, 'answer')
    button.send_keys(answer)
   
    time.sleep(1)

    click_button = browser.find_element(By.CLASS_NAME, "btn")
    click_button.click()

    


finally:
    time.sleep(15)
    browser.quit()
