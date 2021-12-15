# -*- coding: utf-8 -*-
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CLASS_NAME, 'form-control:nth-child(2)')
    input1.send_keys('Igor')

    input2 = browser.find_element(By.CLASS_NAME, 'form-control:nth-child(4)')
    input2.send_keys('Igor')

    input3 = browser.find_element(By.CLASS_NAME, 'form-control:nth-child(6)')
    input3.send_keys('Igor')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    time.sleep(1)

    click_button = browser.find_element(By.CLASS_NAME, "btn")
    click_button.click()

    


finally:
    time.sleep(15)
    browser.quit()
