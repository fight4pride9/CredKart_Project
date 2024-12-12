import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_Page import Login_Page_Class
from Utilities.Logger import log_generator_class
from Utilities.ReadConfig import ReadConfigClass


@pytest.mark.usefixtures("driver_setup")
class Test_User_Login_Params_Class_003:
    #reading data from config file
    login_url = ReadConfigClass.get_login_url()

    #initializing the logger called loggen method from loggenerator class in utilities folder
    log = log_generator_class.loggen_method()

#initiliazing the driver
    driver = None

    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns=0,reruns_delay=2)

    def test_Credkart_User_Login_params_DDT_005(self,get_data_CredKart_login):
        self.log.info("Testcase test_Credkart_User_Login_params_DDT_005 is started")
        self.log.info("Opening Browser")
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.log.info(f"Going to CreKart URl-->{self.login_url}")
        self.email =get_data_CredKart_login[0]
        self.password = get_data_CredKart_login[1]
        self.expected_result = get_data_CredKart_login[2]

        self.log.info(f"Entering email-->{self.email}")
        self.lp.Enter_Email(self.email)

        self.log.info(f"Entering Password-->{self.password}")
        self.lp.Enter_Password(self.password)

        self.log.info("Click on submit button")
        self.lp.Click_submit_Button()

        self.log.info("verify the user login or not")
        if self.lp.verify_user_login_or_registration() == "pass":
            print("User is logged in")
            self.log.info("Taking screenshot for pass")
            self.driver.save_screenshot(f".\\Screenshots\\pass.png")
            actual_result = "login_pass"
            assert True

        else:
            self.log.info("Taking screenshot for fail")
            self.driver.save_screenshot(f".\\Screenshots\\fail.png")
            print("User is not logged in")
            actual_result = "login_fail"



        if self.expected_result == actual_result:
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is Pass")
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is completed")
            assert True
        else:
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is Fail")
            self.log.info("Testcase test_CredKart_User_Login_params_DDT_005 is completed")

        # try:
        #     MenuButton = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        #     assert MenuButton.is_displayed(), "User is not register in"
        #     print("User registered successfully")
        #     self.log.info("Taking Screenshot for Pass")
        #     self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
        #     self.log.info("Testcase test_CredKart_User_Login_002 is Pass")
        #     self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
        # except:
        #     print("User not registered successfully")
        # finally:
        #     self.driver.quit()


