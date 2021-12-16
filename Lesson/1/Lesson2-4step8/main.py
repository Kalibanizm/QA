import time, math

from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = " http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    click_button = browser.find_element(By.CLASS_NAME, "btn")
    click_button.click()

    input = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = str(math.log(abs(12*math.sin(int(input)))))

    button = browser.find_element(By.ID, 'answer')
    button.send_keys(answer)


    submit_button = browser.find_element(By.ID, 'solve').click()

    


finally:
    time.sleep(15)
    browser.quit()
    