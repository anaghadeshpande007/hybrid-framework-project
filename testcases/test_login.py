import pytest
from selenium import webdriver
from pageObjects.loginpage import *

from utilities.readProperties import ReadConfig
from utilities.custom_logger import LogGen
import urllib3
from testcases.conftest import *


class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()      # will return logger obj


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***********Test_001_Login**********")
        self.logger.info("*************verifying Home Page Title***************")
        self.driver=setup
        self.driver.get(self.baseurl)
        actual_title=self.driver.title

        if actual_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****************Home Page Title test is Passed********************")

        else:
            self.driver.save_screenshot("E:\\hybrid framework project\\screenshots\\"+"test_homePageTitle.png")

            self.driver.close()
            self.logger.info("*****************Home Page Title test is failed********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*****************verifying test login********************")

        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        actual_title=self.driver.title

        if actual_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*****************test login is passed********************")

        else:

            self.driver.save_screenshot("E:\\hybrid framework project\\screenshots\\" + "test_login.png")

            self.driver.close()
            self.logger.error("*****************test login is Failed********************")
            assert False

