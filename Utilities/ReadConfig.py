import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
#config.read(r"D:\Pytest_CredKart_Project_Shubham\Configurations\config.ini")

class ReadConfigClass:
    @staticmethod
    def get_data_for_email():
        email = config.get("login data","email")
        return email

    @staticmethod
    def get_data_for_password():
        password = config.get("login data","password")
        return password

    # @staticmethod
    # def section1_data():
    #     section2_data = config.get("section1","key1")
    #     return section2_data

    @staticmethod
    def get_login_url():
        loginurl = config.get("Application url","login_page")
        return loginurl

    @staticmethod
    def get_homepage_url():
        homepageurl = config.get('Application url', 'homepage')
        return homepageurl


    @staticmethod
    def get_register_url():
        registerurl = config.get('Application url', 'register_page')
        return registerurl