from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(driver: webdriver.Chrome, username, password):
    tries = 3;
    while tries > 0:
        driver.get("http://labkom.ilkom.unpak.ac.id/login.php")

        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(username)

        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(password)
        
        elem = driver.find_element_by_tag_name("button")
        elem.send_keys(Keys.RETURN)

        tries += 1
        if "login" not in driver.current_url:
            break