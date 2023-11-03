import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.loginpage import Login
from pageObjects.add_customer_page import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.custom_logger import LogGen
from pageObjects.search_cust_page import SearchCustomers
import string
import random

class Test_004_searchcustomerbyEmail:
    # to click link and enter email and password
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()  # to create log files

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):

        self.logger.info("***************** Test_004_searchcustomerbyEmail **********************")
        self.driver=setup   # return browser driver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()    # from loginpage.py file
        self.logger.info("********* login successful *************")
        self.logger.info("************* starting search custmer by Email *******************")

        self.addcust=AddCustomer(self.driver)   #obj of class addcustomer and pass driver to it
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()


        self.logger.info("************ search customer by email id ********************")

        searchcust=SearchCustomers(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)

        status=searchcust.searchCustomerbyEmail("victoria_victoria@nopCommerce.com")
        assert True==status

        self.logger.info("************* Test_004_searchcustomerbyEmail finished ************************ ")

        self.driver.close()
