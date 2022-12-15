from selenium.webdriver.common.by import By
from conftest import *

Xpath_Object = read_jsonfile("./Configfiles/Locators.json")
Input_Object = read_jsonfile("./Configfiles/details.json")



class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def get_url(self):
        self.driver.get(Input_Object["url"])

    def enter_username(self):
        self.driver.find_element(By.XPATH, Xpath_Object["xpath_for_username"]).send_keys(Input_Object["username"])

    def enter_password(self):
        self.driver.find_element(By.XPATH, Xpath_Object["xpath_for_password"]).send_keys(Input_Object["password"])

    def click_login(self):
        self.driver.find_element(By.XPATH, Xpath_Object["xpath_for_submit"]).click()