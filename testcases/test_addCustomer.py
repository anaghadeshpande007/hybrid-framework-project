import pytest
from selenium.webdriver.common.by import By

from pageObjects.loginpage import Login
from pageObjects.add_customer_page import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.custom_logger import LogGen
import string
import random


def random_generator(size=8,chars=string.ascii_lowercase+string.digits):

    return ''.join(random.choice(chars) for x in range(size))



class Test_003_addcustomer:
    # to click link and enter email and password
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()  # to create log files

    @pytest.mark.sanity
    def test_addCustomer(self,setup):

        self.logger.info("***************** Test_003_addcustomer **********************")
        self.driver=setup   # return browser driver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()    # from loginpage.py file
        self.logger.info("********* login successful *************")
        self.logger.info("************* starting add customer test *******************")

        self.addcust=AddCustomer(self.driver)   #obj of class addcustomer and pass driver to it
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("************ providing customer info ********************")

        self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123456")
        self.addcust.setFirstname("hrushi")
        self.addcust.setLastname("Deshpande")
        self.addcust.setGender("Male")
        self.addcust.setDob("6/5/1968") #date/month/year
        self.addcust.setCompanyName("busyQA")
        self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManagerofVendor("Vendor 1")
        self.addcust.setAdminComment("This is for testing...")

        self.addcust.clickOnSave()

        self.logger.info("************* saving customer info ********************")
        self.logger.info("**************** add customer validation started *********************")

        self.msg=self.driver.find_element(by=By.TAG_NAME,value='body').text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("****** add customer test passed **********")
        else:
            self.driver.save_screenshot("E:\\hybrid framework project\\screenshots\\"+"test_addcustomer.png")
            self.logger.error("***********add customer test failed **********")
            assert True==False

        self.driver.close()
        self.logger.info("************** ending home page title test ***********************")

