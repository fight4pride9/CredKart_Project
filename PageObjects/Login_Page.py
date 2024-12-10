from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Page_Class:
    text_email_id = "email"
    text_password_id = "password"
    button_submit_class = "btn"
    button_menubutton_class = "dropdown-toggle"
    button_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

#driver is define in conftest
#driver value is used in testcase
#driver method are used in page object
#we have define

    def Enter_Email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def Click_submit_Button(self):
        self.driver.find_element(By.CLASS_NAME,self.button_submit_class).click()

    def Click_Menu_Button(self):
        menubutton = self.driver.find_element(By.CLASS_NAME,self.button_menubutton_class)
        menubutton.click()

    def Click_Logout_Button(self):
        logoutbutton = self.driver.find_element(By.XPATH,self.button_logout_xpath)
        logoutbutton.click()

    def verify_user_login_or_registration(self):
        try:
            MenuButton = self.driver.find_element(By.CLASS_NAME,self.button_menubutton_class)
            MenuButton.click()
            logoutbutton = self.driver.find_element(By.XPATH,self.button_logout_xpath)
            logoutbutton.click()
            return "pass"
        except:
            return "fail"

