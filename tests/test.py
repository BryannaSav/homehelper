from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .TaskListPage import TaskListsPage
import unittest
from tasklist.models import TaskList
from django.contrib.auth.models import User 
from selenium.webdriver.common.by import By

# FIXME: Django's LiveServerTestCase will help here
class TaskListTestCase(unittest.TestCase):

    def setUp(self):
        PATH = r"C:\Users\Bryanna\Documents\Projects\HomeHelper\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        self.driver = driver
        self.page = TaskListsPage(driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_tasklist(self):
        login(self.driver)
        self.page.open()
        self.page.new_list_name = "test list - 8675309"
        self.page.new_list_description = "test description"
        self.page.click_create_new_list_button()
        self.page.get_tasklist("test list - 8675309")
        created_tasklist = TaskList.objects.get(name="test list - 8675309")
        created_tasklist.delete()
        logout(self.driver)

    def test_delete_tasklist(self):
        create_test_tasklist()
        login(self.driver)
        self.page.open()
        tasklist_element = self.page.get_tasklist("test list - 8675309")
        delete_icon = tasklist_element.find_element_by_css_selector('a.mdi-trash-can')
        delete_icon.click()
        def tasklist_is_deleted():
            try:
                self.page.get_tasklist("test list - 8675309")
                return False
            except ValueError:
                return True
        tasklist_is_deleted()
            
def login(driver):
        driver.get("http://localhost:8000/") 
        login_link = driver.find_element_by_link_text("LOGIN")
        login_link.click()
        driver.implicitly_wait(1)
        username_input = driver.find_element_by_id("id_username")
        username_input.send_keys("tester")
        password_input = driver.find_element_by_id("id_password")
        password_input.send_keys("testingpass")
        password_input = driver.find_element_by_id("id_password")
        password_input.send_keys(Keys.RETURN)

def logout(driver):
    login_link = driver.find_element_by_link_text("Logout")
    login_link.click()

def create_test_tasklist():
    user = User.objects.get(id=8)
    task_list = TaskList(
            name="test list - 8675309", 
            description="test description", 
            user=user)
    task_list.save()

if __name__ == '__main__':
    unittest.main()


# Completed: 
#  - Moved driver logic to TaskLists and Users classes
#  - Set up Django's unittest to handle testing
#  - Added proper class/id naming to tasklists page for edit/delete functionality

# Upcoming:
#  - Make a database for testing only (Django can handle most of this)
#  - Have testing user register proir to login
#  - If this POC is on the right track, implement edit/delete tests
#  - Implement blank name test
