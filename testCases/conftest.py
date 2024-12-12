import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser",default="firefox")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print ("Launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print ("Launching Edge Browser")
        driver = webdriver.Edge()
    elif browser == "--headless":
        print ("Firefox browser in headless mode")
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        print("Firefox browser started")
        driver = webdriver.Firefox()
    driver.maximize_window()

    #attaching driver to class
    request.cls.driver = driver
    yield driver
    driver.quit()
    print("Browser Closed")

    # yield driver #driver is return to test case or method
    # driver.quit()
    # print("Browser Closed")


def pytest_metadata(metadata):
    metadata["class"] = "Credence_Test#20"
    metadata["Description"] ="Test to varify the credence homepage and search functionality "
    metadata["Test Type"] = "Functional"
    metadata["Author"] = "Shubham-Test Automation Team"
    metadata["URL"] = "https://automation.credence.in/" #to add url key in report
    metadata.pop("Platform",None)


@pytest.fixture(params=[
    ("Credencetest@test.com","Crdence@123","login_pass"),
    ("Credencetest@test.com1","Crdence@123","login_fail"),
    ("Credencetest@test.com","Crdence@1231","login_fail"),
    ("Credencetest@test.com1","Crdence@123","login_fail"),
    ])
def get_data_CredKart_login(request):
    return request.param





















