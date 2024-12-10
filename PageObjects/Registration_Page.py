from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    text_name_id = "name"
    text_confirm_password_id ="password-confirm"


    def Enter_Name(self,name):
        self.driver.find_element(By.ID,self.text_name_id).send_keys(name)

    def Enter_confirm_password(self,password):
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(password)

