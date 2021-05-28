from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Users():

    def __init__(self, driver):
        self.driver = driver
        self.USERNAME = "tester"
        self.PASSWORD = "testingpass"

    def login_registered_user(self):
        self.driver.get("http://localhost:8000/") 
        login_link = self.driver.find_element_by_link_text("LOGIN")
        login_link.click()
        self.driver.implicitly_wait(1)
        username_input = self.driver.find_element_by_id("id_username")
        username_input.send_keys(self.USERNAME)
        password_input = self.driver.find_element_by_id("id_password")
        password_input.send_keys(self.PASSWORD)
        password_input = self.driver.find_element_by_id("id_password")
        password_input.send_keys(Keys.RETURN)

    def log_out_logged_in_user(self):
        login_link = self.driver.find_element_by_link_text("Logout")
        login_link.click()


