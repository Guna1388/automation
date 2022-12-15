import time
from Pages.Loginpage import LoginPage, Input_Object
from Pages.Homepage import *
from Utilities import screenshots
import moment
from conftest import *

@pytest.mark.usefixtures("browser_setup")
class Test_GreytHR:
    def test_portal_login(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.get_url()
        loginpage.enter_username()
        loginpage.enter_password()
        loginpage.click_login()
        time.sleep(3)
        screenshot_name = f'home_{moment.now().strftime("%y-%m-%d_%H-%M-%S")}.png'
        screenshots.ScreenShotExtensions.take_standard_screenshot(driver,
                                                                  Input_Object["Screenshot_path"] % screenshot_name)
        time.sleep(3)

    def test_Username(self):
        driver = self.driver
        homepage = home_page(driver)
        homepage.My_INFO()
        print("User has successfully logged in")
        # path = Xpath_Object["xpath_for_name_assertion"]%(Input_Object['Name'])
        # print(path)
        # name = homepage.name_assertion()
        # assert name == Input_Object["Name"]
        #print("The User name is "  + name)
        #screenshots.ScreenShotExtensions.take_standard_screenshot(driver, "E:/User2/e2e/Screenshots/user.png")

    # def test_password_change():
    #         driver.find_element(By.XPATH, "(//a[@class='icon-link text-secondary text-regular ng-star-inserted'])[1]").click()
    #         driver.find_element(By.XPATH, "//span[@class='text-4' and text() ='Change Password']").click()
    #         driver.find_element(By.XPATH , "// input[@name ='currentPassword']").send_keys(Input_Object["password"])
    #         driver.find_element(By.XPATH, "//input[@name='newPassword']").send_keys(Input_Object["new_password"])
    #         driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys(Input_Object["new_password"])
    #         driver.find_element(By.XPATH , "//button[@type='submit']").click()
# #
# def test_ID():
#         wait = WebDriverWait(driver,10)
#         wait.until(expected_conditions.presence_of_element_located((By.XPATH,"(//span[@class='info ng-star-inserted'])[2]")))
#         ID = driver.find_element(By.XPATH, "(//span[@class='info ng-star-inserted'])[2]").text
#         assert ID == Input_Object["username"]
#         print("The employee ID is " + ID)
#         screenshots.ScreenShotExtensions.take_standard_screenshot(driver, "E:/User2/e2e/Screenshots/ID.png")
#
#
# def test_loop():
#         Details = driver.find_elements(By.XPATH, "//span[@class='info ng-star-inserted']")
#
#         for detail in Details:
#                 print(detail.text)
#                 if detail.text == Input_Object["marital_status"]:
#                         assert detail.text != "Commited"
#                         print("Details matches the data base")
#         screenshots.ScreenShotExtensions.take_standard_screenshot(driver, "E:/User2/e2e/Screenshots/details.png")
# #
# def test_drop_down():
#         try:
#                 driver.find_element(By.XPATH, "//button[@class='btn dropdown-toggle']").click()
#                 driver.find_element(By.XPATH, "//a[@title='presentaddress']").click()
#                 Address = driver.find_element(By.XPATH, "//*[contains(text(),'Gents PG')]").text
#                 print(Address)
#                 assert  Address == Input_Object["address"]
#         except Exception as e:
#                 print(e)
#         screenshots.ScreenShotExtensions.take_standard_screenshot(driver, "E:/User2/e2e/Screenshots/drop.png")
#
# def test_logout():
#         driver.find_element(By.XPATH, "//div[@class='image-gt-icon-logout w-2x h-2x']").click()
#         print("User has successfully logged out")
#         time.sleep(3)
#         screenshots.ScreenShotExtensions.take_standard_screenshot(driver, "E:/User2/e2e/Screenshots/logout.png")
#         File_object = open(r"./log.text", "a")
#         File_object.write("\n User has succesfully logged out  - " +  now.strftime("%m/%d/%Y, %H:%M:%S"))
#         driver.close()
