from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Users\Bryanna\Documents\Projects\HomeHelper\chromedriver.exe"
driver = webdriver.Chrome(PATH)
USERNAME = "tester"
PASSWORD = "testingpass"

def run_tests():
    print("list create -", create_list())
    print("list edit -", edit_list())
    print("list delete -", delete_list())
    driver.quit()

def login_using_test_cred():
    driver.get("http://localhost:8000/") 
    login_link = driver.find_element_by_link_text("LOGIN")
    login_link.click()
    driver.implicitly_wait(1)

    username_input = driver.find_element_by_id("id_username")
    username_input.send_keys(USERNAME)
    password_input = driver.find_element_by_id("id_password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

def logout_of_test_cred():
    login_link = driver.find_element_by_link_text("Logout")
    login_link.click()

def create_list():   
    login_using_test_cred()
    try:
        lists_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Lists"))
        )  
        lists_link.click()
    except:
        return False
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "input-9"))
    )
    name_input = driver.find_element_by_id("input-9")
    name_input.send_keys("test list - 8675309")
    description_input = driver.find_element_by_id("input-12")
    description_input.send_keys("test description")
    name_input.send_keys(Keys.RETURN)
    try:
        link_check = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "test list - 8675309"))
        ) 
        # logout_of_test_cred()
        return True
    except:
        return False 

def edit_list():
    login_using_test_cred()
    try:
        lists_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Lists"))
        )  
        lists_link.click()
    except:
        return False
    # Edit buttons have no tasklist specific selectors. 
    # Finding the li that contains the tasklist and clicking that button
    all_li_tags = driver.find_elements_by_css_selector("li")
    for li in all_li_tags:
        li_html = li.get_attribute('outerHTML')
        if "test list - 8675309" in li_html:
            edit_button = li.find_element_by_class_name("mdi-lead-pencil")
            edit_button.click()
    name_input = driver.find_element_by_id("input-22")
    name_input.send_keys(" - UPDATED")
    desc_input = driver.find_element_by_id("input-25")
    desc_input.send_keys(" - UPDATED")
    desc_input.send_keys(Keys.RETURN)
    try:
        link_check = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "test list - 8675309 - UPDATED"))
        ) 
        logout_of_test_cred()
        return True
    except:
        return False 

def delete_list():
    login_using_test_cred()
    try:
        lists_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Lists"))
        )  
        lists_link.click()
    except:
        return False
    link_with_id = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "test list - 8675309"))
    )
    #Uses the list name to get an id, then finds a trash can icon with the id
    list_html = link_with_id.get_attribute('outerHTML')
    list_html_id = list_html[list_html.index("list/")+5:list_html.index("\">")]
    links = driver.find_elements_by_class_name("mdi-trash-can")
    for elem in links:
        html_elem = elem.get_attribute('outerHTML')
        if list_html_id in html_elem:
            elem.click()
            return True
    return False

run_tests()


#Add classes, ids to html to make selecting easier
#Make takslists into a class that I can call all the tasklist page functiuonality from


#Next time:
#Register tester account in tests
#Look into a test framework to run these tests (py.test or unit test)
#Add the blank name field test
#Other: django test suite, make db for testing