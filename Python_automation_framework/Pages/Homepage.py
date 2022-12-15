from selenium.webdriver.common.by import By

from Pages.Loginpage import Xpath_Object, Input_Object


class home_page():
    def __init__(self, driver):
        self.driver = driver

    def My_INFO(self):
        self.driver.find_element(By.XPATH, Xpath_Object["xpath_for_MyInfo"]).click()

    # def name_assertion(self):
    #     self.driver.find_element(By.XPATH, Xpath_Object["xpath_for_name_assertion"]%(Input_Object['Name'])).text
