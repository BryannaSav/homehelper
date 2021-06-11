from selenium import webdriver
from .TaskListPage import TaskLists
from .LoginPage import Users
import unittest

# FIXME: Django's LiveServerTestCase will help here
class TaskListTestCase(unittest.TestCase):

    def setUp(self):
        PATH = r"C:\Users\Bryanna\Documents\Projects\HomeHelper\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        self.driver = driver
        # FIXME: Nit: self.page
        self.TaskList = TaskLists(driver)
        # FIXME: No need for this if standalone login() and logout()
        self.User = Users(driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_tasklist(self):
        # FIXME: login() -- function by itself
        self.User.login_registered_user()
        # FIXME: Nit: self.page.open()
        self.TaskList.navigate_to_lists_page()
        # FIXME: Nit: page.new_list_name = "test list - 8675309"
        self.TaskList.populate_name_input("test list - 8675309")
        # FIXME: Nit: page.new_list_description = ...
        self.TaskList.populate_description_input("test description")

        # FIXME: Nit: page.submit_new_list() / .click_create_new_list_button()
        self.TaskList.submit_create_tasklist_form()
        # FIXME: self.page.get_tasklist(...)  # raises if does not exist
        self.assertTrue(self.TaskList.check_for_tasklist("test list - 8675309"))
        # FIXME: logout() -- function by itself
        self.User.log_out_logged_in_user()

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
