
from typing import Final
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://tuportal.temple.edu")
print("Application title is ", driver.title)
print("application url is ", driver.current_url)


#LOGIN PAGE
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("tui85832")
password = driver.find_element_by_id("password")
password.send_keys("3BigHouse$")
loginButton = driver.find_element_by_name("_eventId_proceed")
loginButton.send_keys(Keys.RETURN)

time.sleep(40)

#NEXT PAGE
driver.get("https://prd-xereg.temple.edu/StudentRegistrationSsb/ssb/classRegistration/classRegistration")

while(True):
    try:    
        subject = driver.find_element_by_id("s2id_autogen4")
        subject.send_keys("cis")
        time.sleep(5)
        subject.send_keys(Keys.RETURN)
        courseNumber = driver.find_element_by_id("txt_courseNumber")
        courseNumber.send_keys("3344")
        searchBtn = driver.find_element_by_id("search-go")
        searchBtn.click()
        time.sleep(2)
        addCourseButton = driver.find_element_by_id("addSection20213630072")
        addCourseButton.click()
        time.sleep(2)
        saveCourse = driver.find_element_by_id("saveButton")
        saveCourse.click()
        time.sleep(10)
        driver.refresh()
        time.sleep(5)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(5)
    except:
        break

driver.quit() 
        
        
        
   
    


# print(main.text)

# duoButton = driver.find_elements_by_class_name("auth-button positive")
# duoButton.send_keys(Keys.RETURN)


