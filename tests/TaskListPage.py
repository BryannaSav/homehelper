from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tasklist.models import TaskList

# FIXME: Nit: TaskListsPage
class TaskListsPage():

    def __init__(self, driver):
        self.driver = driver
        self.new_list_name = ""
        self.new_list_description = ""

    def open(self):
        try:
            #TO-DO: look into ways to simplify wait
            lists_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Lists"))
            )  
            lists_link.click()
        except:
            return False

    def click_create_new_list_button(self):
        name_input = self.driver.find_element_by_id("input-9")
        name_input.send_keys(self.new_list_name)
        description_input = self.driver.find_element_by_id("input-12")
        description_input.send_keys(self.new_list_description)
        submit_button = self.driver.find_element_by_id("create-form-submit")
        submit_button.send_keys(Keys.RETURN)

    def get_tasklist(self, name):
        try:
            tasklist = TaskList.objects.get(name="test list - 8675309")
            return self.driver.find_element_by_id("tasklist" + str(tasklist.id))
        except:
            raise ValueError("No such tasklist " + name)
            

