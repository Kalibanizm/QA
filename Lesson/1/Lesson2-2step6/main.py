import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("window.scrollBy(0, 100);", button)
    
    answer = str(math.log(abs(12*math.sin(int(input)))))

    button = browser.find_element(By.ID, 'answer')
    button.send_keys(answer)

    check_robot = browser.find_element(By.ID, 'robotCheckbox')
    check_robot.click()

    

    robot_rule = browser.find_element(By.ID, 'robotsRule')
    robot_rule.click()
        
    
    time.sleep(1)

    click_button = browser.find_element(By.CLASS_NAME, "btn")
    click_button.click()

    


finally:
    time.sleep(15)
    browser.quit()
