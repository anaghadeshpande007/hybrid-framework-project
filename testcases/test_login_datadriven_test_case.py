import time

import pytest
from selenium import webdriver
from pageObjects.loginpage import *
from utilities.readProperties import ReadConfig
from utilities.custom_logger import LogGen
import urllib3
from testcases.conftest import *
from utilities import XLUtilities

class Test_002_DDT_Login:
    baseurl=ReadConfig.getApplicationURL()
    path="E:\\hybrid framework project\\testdata\\LoginData.xlsx"
    logger=LogGen.loggen()      # will return logger obj


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*****************Test_002_DDT_Login********************")
        self.logger.info("*****************verifying test login ddt ********************")
        self.driver=setup
        self.driver.get(self.baseurl)

        self.lp=Login(self.driver)

        self.rows=XLUtilities.getRowCount(self.path,"Sheet1")
        print('no. of rows in excel:',self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
           self.user= XLUtilities.readdata(self.path,'Sheet1',r,1)
           self.password = XLUtilities.readdata(self.path, 'Sheet1', r, 2)
           self.exp = XLUtilities.readdata(self.path, 'Sheet1', r, 3)

           self.lp.setUserName(self.user)
           self.lp.setPassword(self.password)
           self.lp.clicklogin()
           time.sleep(5)

           act_title=self.driver.title
           exp_title="Dashboard / nopCommerce administration"

           if act_title==exp_title:
               if self.exp=="Pass":
                   self.logger.info("******* test is passed************")
                   self.lp.clicklogout()
                   lst_status.append("Pass")

               elif self.exp=='Fail':
                   self.logger.info("******* test is failed************")
                   self.lp.clicklogout()
                   lst_status.append("Fail")

           elif act_title!=exp_title:
               if self.exp=='Pass':
                   self.logger.info("***********failed*******************")
                   lst_status.append('Fail')

               elif self.exp== 'Fail':
                   self.logger.info('********** passed *************')
                   lst_status.append('Pass')


        if 'Fail' not in lst_status:
               self.logger.info("****** login ddt test is passed *************")
               self.driver.close()
               assert True
        else:
               self.logger.info('********* login ddt test is failed ***************')
               self.driver.close()
               assert False

        self.logger.info('************ End of login ddt test **********')
        self.logger.info('************** Completed Test_002_DDT_Login ********************')

