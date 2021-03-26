import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from utilities.BaseClass import BaseClass
from datetime import datetime
import datetime as DT
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class TestsalesPage(BaseClass):

    log = BaseClass.getLogger()


# py.test testcases/test_salesPage.py::TestsalesPage::test_verfysaleswithin7days

    def test_verfysaleswithin7days(self):
        d1 = DT.date.today()
        a = d1.strftime("%Y-%m-%d")

        d2 = d1 + DT.timedelta(days=6)
        b = d2.strftime("%Y-%m-%d")

        self.driver.get("https://sso.eservices.jud.ct.gov/foreclosures/Public/PendPostbyTownList.aspx")
        time.sleep(10)
        window_before = self.driver.window_handles[0]
        list = ['Milford', 'Trumbull', 'Norwalk', 'Stamford', 'Shelton', 'Fairfield']
        townname = sorted(list)
        getTownList = self.driver.find_elements(By.XPATH, "//table//tbody//tr//td//div[@id='ctl00_cphBody_Panel1']//a")
        time.sleep(10)
        for town in getTownList:
            if town.text in townname:
                time.sleep(10)
                ActionChains(self.driver).context_click(town).key_down(Keys.COMMAND).key_down(Keys.SHIFT).click(
                    town).key_down(Keys.COMMAND).key_down(Keys.SHIFT).perform()
                time.sleep(10)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                rows = len(self.driver.find_elements(By.XPATH, "//table[@id='ctl00_cphBody_GridView1']//tbody//tr"))
                columns = len(self.driver.find_elements(By.XPATH, "//table[@id='ctl00_cphBody_GridView1']//tbody//tr//th"))
                for r in range(2, rows + 1):
                    for c in range(5, 6):
                        date = self.driver.find_element(By.XPATH, "//table[@id='ctl00_cphBody_GridView1']//tbody//tr["+str(r)+"]//td[2]//span[1]").text
                        newDate = date[0:10]  # 3/27/2021
                        date_time_obj = datetime.strptime(newDate, "%m/%d/%Y")
                        d3 = date_time_obj.strftime("%Y-%m-%d")
                        if a < b > d3:
                            time.sleep(5)
                            view = self.driver.find_element(By.XPATH,"//table[@id='ctl00_cphBody_GridView1']//tbody//tr["+str(r)+"]//td["+str(c)+"]//a")
                            try:
                                ActionChains(self.driver).context_click(view).key_down(Keys.LEFT_CONTROL).click(view).key_up(
                                    Keys.LEFT_CONTROL).perform()
                                time.sleep(5)
                            except:
                                ActionChains(self.driver).context_click(view).key_down(Keys.LEFT_CONTROL).click(view).key_up(
                                    Keys.LEFT_CONTROL).perform()
                                time.sleep(5)
                        else:
                            self.log.info("Date not falling between 7 days")
                self.driver.switch_to.window(window_before)
                time.sleep(5)






















