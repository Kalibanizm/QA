from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRegistry(unittest.TestCase):
    #link1 = "http://suninjuly.github.io/registration1.html"
    #link2 = "http://suninjuly.github.io/registration2.html"
    def test_registry_link1(self):
        link = "http://suninjuly.github.io/registration1.html"

        

        browser = webdriver.Chrome()
        browser.implicitly_wait(5) #add pause 5 sec every find_element
        browser.get(link)


        input1 = browser.find_element(By.CLASS_NAME, "first:required")
        input1.send_keys("Ivan")


        input2 = browser.find_element(By.CLASS_NAME, "second:required")
        input2.send_keys("Petrov")


        input3 = browser.find_element(By.CLASS_NAME, "third:required")
        input3.send_keys("Smolensk")


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be equal!")
        browser.quit()

    def test_registry_link2(self):
        link = "http://suninjuly.github.io/registration2.html"

        

        browser = webdriver.Chrome()
        browser.implicitly_wait(5) #add pause 5 sec every find_element
        browser.get(link)


        input1 = browser.find_element(By.CLASS_NAME, "first:required")
        input1.send_keys("Ivan")


        input2 = browser.find_element(By.CLASS_NAME, "second:required")
        input2.send_keys("Petrov")


        input3 = browser.find_element(By.CLASS_NAME, "third:required")
        input3.send_keys("Smolensk")


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be equal!")
        browser.quit()

if __name__ == "__main__":
    unittest.main()