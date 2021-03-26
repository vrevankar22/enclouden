from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path="D:\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    #driver.quit()







