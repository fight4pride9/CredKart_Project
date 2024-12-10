import pytest

from PageObjects.Login_Page import Login_Page_Class
from Utilities.Logger import log_generator_class
from Utilities.ReadConfig import ReadConfigClass
from testCases.conftest import driver_setup
from Utilities import XLutilities



@pytest.mark.usefixtures("driver_setup")
class Test_User_Login_Excel_DDT_class_002:
    login_url = ReadConfigClass.get_login_url()

    #initilizing the logger called logger method from log generator class in utilities folder
    log = log_generator_class.loggen_method()

    #initilizing the driver
    driver = None

    Excel_file_path = ".\\TestData\\Test_Data.xlsx"
    #Excel_file_path = r"D:\Pytest_CredKart_Project_Shubham\TestData\Test_Data.xlsx"

    @pytest.mark.regression
    @pytest.mark.group1
    @pytest.mark.flaky(reruns = 0,reruns_delay =2)
    def test_CredKart_User_Login_Excel_DDT_004(self):
        self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is started")
        """test verify user_login method with valid credentials"""
        self.log.info("opening Browser")
        self.lp = Login_Page_Class(self.driver)
        self.driver.get(self.login_url)
        self.log.info(f"Going to CredKart Url-->{self.login_url}")

        #Read Data from excel

        self.log.info("Reading data from excel")
        self.log.info("Reading the number rows from excel")
        excel_row_count = XLutilities.RowCount(self.Excel_file_path,"CredKart_login_Data")
        print (f"Number of row in excel is {excel_row_count}")
        self.log.info(f"Number of row in excel is {excel_row_count}")
        Result_List = []

        for i in range(2,excel_row_count+1):
            self.log.info(f"Reading the data from row number:{i} in excel")
            self.email = XLutilities.ReadData(self.Excel_file_path,"CredKart_login_Data",i,1)
            self.password = XLutilities.ReadData(self.Excel_file_path,"CredKart_login_Data",i,2)
            self.expected_result = XLutilities.ReadData(self.Excel_file_path,"CredKart_login_Data",i,3)

            self.log.info(f"Entering Email:{self.email}")
            self.lp.Enter_Email(self.email)
            self.log.info(f"Entering Password:{self.password}")
            self.lp.Enter_Password(self.password)
            self.log.info("Clicking login Button")
            self.lp.Click_submit_Button()
            self.log.info("Verify the user is log in or not")

            if self.lp.verify_user_login_or_registration() == "pass":
                actual_result = "login_pass"
                self.log.info(f"user {self.email} is logged in and actual result is {actual_result}")
                self.log.info("Taking Screenshot of for pass")
                self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_User_Login_Excel_DDT_004_{self.email}_pass.png")
            else:
                actual_result = "login_fail"
                self.log.info(f"user {self.email} is logged in and actual result is {actual_result}")
                self.log.info("Taking Screenshot of for fail")
                self.driver.save_screenshot(f".\\Screenshots\\test_CredKart_User_Login_Excel_DDT_004_{self.email}_fail.png")

            if self.expected_result == actual_result:
                test_case_status = "Pass"
            else:
                test_case_status = "Fail"

            XLutilities.WriteData(self.Excel_file_path,"CredKart_login_Data",i,4,actual_result)
            XLutilities.WriteData(self.Excel_file_path,"CredKart_login_Data",i,5,test_case_status)
            Result_List.append(test_case_status)
            self.driver.get(self.login_url)

        if "Fail" in Result_List:
            self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is failed")
            self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is complete")
            assert False
        else:
            self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is Pass")
            self.log.info("Testcase test_CredKart_User_Login_Excel_DDT_004 is complete\n")


