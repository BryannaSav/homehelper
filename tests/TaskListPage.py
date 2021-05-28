from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TaskLists():

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_lists_page(self):
        try:
            #TO-DO: look into ways to simplify wait
            lists_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Lists"))
            )  
            lists_link.click()
        except:
            return False
    
    def populate_name_input(self, name):
        name_input = self.driver.find_element_by_id("input-9")
        name_input.send_keys(name)

    def populate_description_input(self, description):
        description_input = self.driver.find_element_by_id("input-12")
        description_input.send_keys(description)

    def submit_create_tasklist_form(self):
        submit_button = self.driver.find_element_by_id("create-form-submit")
        submit_button.send_keys(Keys.RETURN)

    def check_for_tasklist(self, name):
        #change to get a tasklist
        try:
            link_check = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, name))
            ) 
            return True
        except:
            return False 

