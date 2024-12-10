from selenium import webdriver
from selenium.webdriver.common.by import By
import faker
import pytest
from PageObjects.Login_Page import Login_Page_Class
from PageObjects.Registration_Page import Registration_Page_Class
from Utilities.ReadConfig import ReadConfigClass
from Utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class_001:
    #Reading data from config file
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_login_url()
    homepage_url = ReadConfigClass.get_homepage_url()
    registration_url = ReadConfigClass.get_register_url()

    #key1 = ReadConfigClass.section1_data()

    #Intilizing the logger called loggen method from loggenerator data class in utilities folder
    log = log_generator_class.loggen_method()

    #Initilizing the driver
    driver = None
    """Test cases fro user profile class"""

    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns=0,reruns_delay=2)
    def test_verify_CredKart_Url_001(self):
        """Test varify_credkart_url method with valid URL"""
        # driver = driver_setup
        # self.log.debug("This is debug")
        # self.log.info("This is info")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")
        self.log.info("Testcase test_verify_CredKart_Url_001 is started")
        self.driver.get(self.homepage_url)
        self.log.info("Opening Browser")
        self.log.info(f"Going to CredKart URL--> {self.homepage_url}")
        self.log.info("Checking the page title")
        if self.driver.title == "CredKart":
            self.log.info(f"Page Title:{self.driver.title} is match with expected title")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_pass.png")
            self.log.info("TestCase test_verify_CredKart_Url_001 is passed")
            self.log.info("Testcase test_verify_CredKart_Url_001 is completed\n")
            assert True
        else:
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_fail.png")
            self.log.info("TestCase test_verify_CredKart_Url_001 is failed")
            self.log.info("Testcase test_verify_CredKart_Url_001 is completed\n")
            assert False

###########################################################################################
    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns = 1,reruns_delay =2)
    def test_CredKart_User_Login_002(self):
        """test varify_user_login method with valid credentials"""
        #self.driver = driver_setup
        self.log.info("Testcase test_CredKart_User_Login_002 is started")
        self.log.info("Opening Browser")
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.log.info(f"Going to CredKart URL-->{self.login_url}")
        self.log.info(f"Entering email-->{self.email}")
        self.lp.Enter_Email(self.email)
        self.log.info(f"Entering password-->{self.password}")
        self.lp.Enter_Password(self.password)
        self.log.info("Clicking on login button")
        self.lp.Click_submit_Button()
        self.log.info("Verify user login or not")

        if self.lp.verify_user_login_or_registration() == "pass":
            print("User is logged in")
            self.log.info("Taking Screenshot for Pass")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
            self.log.info("Testcase test_CredKart_User_Login_002 is Pass")
            self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
            assert True
        else:
            self.log.info("Taking Screenshot for Fail")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_fail.png")
            print("User is not logged in")
            self.log.info("Testcase test_CredKart_User_Login_002 is Fail")
            self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
            assert False





####################################################################################

    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns = 1,reruns_delay = 2)
    def test_CredKart_User_Registration_003(self,faker):
        self.log.info("Testcase test_CredKart_User_Login_003 is started")
        self.log.info("Opening Browser")
        self.rp = Registration_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.registration_url)
        self.log.info(f"Going to CredKart URL-->{self.registration_url}")
        random_name = faker.name()
        random_email = faker.email()
        random_password =faker.password()

        self.log.info(f"Entering name:{random_name}")
        self.rp.Enter_Name(random_name)
        self.log.info(f"Entering email--{random_email}")
        self.rp.Enter_Email(random_email)
        self.log.info(f"Entering password--{random_password}")
        self.rp.Enter_Password(random_password)
        self.log.info(f"Entering confirm password--{random_password}")
        self.rp.Enter_Password(random_password)
        self.log.info("Clicking on register button")
        self.rp.Click_submit_Button()
        self.log.info("Verify user register or not")
        # if self.rp.verify_user_login_or_registration() == "CredKart":
        #     print("User is Registered")
        #     self.log.info("Taking Screenshot for Pass")
        #     self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
        #     self.log.info("Testcase test_CredKart_User_Login_002 is Pass")
        #     self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
        #     assert True
        # else:
        #     self.log.info("Taking Screenshot for Fail")
        #     self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_fail.png")
        #     print("User is not Registered")
        #     self.log.info("Testcase test_CredKart_User_Login_002 is Fail")
        #     self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
        #     assert False

        try:
            MenuButton = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
            assert MenuButton.is_displayed(), "User is not register in"
            print("User registered successfully")
            self.log.info("Taking Screenshot for Pass")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
            self.log.info("Testcase test_CredKart_User_Login_002 is Pass")
            self.log.info("Testcase test_CredKart_User_Login_002 is Completed\n")
        except:
            print("User not registered successfully")
        finally:
            self.driver.quit()








