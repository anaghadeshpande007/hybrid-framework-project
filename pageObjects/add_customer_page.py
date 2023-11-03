import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:

    # add customer page
    lnk_customer_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnk_customer_menuitem_xpath="//a[@href='/Admin/Customer/List']"
    btn_Addnew_xpath="//a[normalize-space()='Add new']"

    txt_Email_xpath="//input[@id='Email']"
    txt_password_xpath="//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    radiobtn_male_gender_id = "Gender_Male"
    radiobtn_female_gender_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    txt_CustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lst_itemAdministrator_xpath="//li[contains(text(),'Administrators')]"
    lst_itemRegister_xpath="//li[contains(text(),'Registered')]"
    lst_itemGuest_xpath="//li[contains(text(),'Guests')]"
    lst_itemVendor_xpath="//li[contains(text(),'Vendors')]"
    dropdown_manager_of_vendor_xpath="//select[@id='VendorId']"
    txt_admincomment_xpath="//textarea[@id='AdminComment']"
    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(by=By.XPATH,value=self.lnk_customer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(by=By.XPATH,value=self.lnk_customer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_Addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(by=By.XPATH, value=self.txt_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(by=By.XPATH, value=self.txt_password_xpath).send_keys(password)

    def setFirstname(self,fname):
        self.driver.find_element(by=By.XPATH, value=self.txt_FirstName_xpath).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(by=By.XPATH, value=self.txt_LastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(by=By.ID,value=self.radiobtn_male_gender_id).click()
        elif gender=='Female':
            self.driver.find_element(by=By.ID, value=self.radiobtn_female_gender_id).click()
        else:   #default male gender id will be selected
            self.driver.find_element(by=By.ID, value=self.radiobtn_male_gender_id).click()

    def setDob(self, dob):
        self.driver.find_element(by=By.XPATH, value=self.txt_dob_xpath).send_keys(dob)

    def setCompanyName(self, compname):
        self.driver.find_element(by=By.XPATH, value=self.txt_company_name_xpath).send_keys(compname)

    def setCustomerRoles(self,role):    # call this method 2 time if we want use many role
        self.driver.find_element(by=By.XPATH, value=self.txt_CustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lst_itemRegister_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lst_itemAdministrator_xpath)
        elif role=='Guests':        # user can be guest or registered only one out of it
            time.sleep(3)
            self.driver.find_element(by=By.XPATH,value="//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()  # remove selected registerd
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lst_itemGuest_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(by=By.XPATH,value=self.lst_itemRegister_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(by=By.XPATH, value=self.lst_itemVendor_xpath)
        else:   # deafult value guest is selected
            self.listitem = self.driver.find_element(by=By.XPATH, value=self.lst_itemGuest_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].click()',self.listitem)

    def setManagerofVendor(self,value):
        drp=Select(self.driver.find_element(by=By.XPATH,value=self.dropdown_manager_of_vendor_xpath))
        drp.select_by_visible_text(value)


    def setAdminComment(self,comment):
        self.driver.find_element(by=By.XPATH, value=self.txt_admincomment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(by=By.XPATH,value=self.btn_save_xpath).click()








