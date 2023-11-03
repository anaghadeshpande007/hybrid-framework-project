import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchCustomers:
    txt_email_id="SearchEmail"
    txt_firstname_id="SearchFirstName"
    txt_lastname_id="SearchLastName"
    btn_search_id="search-customers"

    #tablesearchResult_Xpath="//div[@class='dataTables_scrollHeadInner']//table[@class='table']"
    table_xpath=" //table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(by=By.ID,value=self.txt_email_id).clear()
        self.driver.find_element(by=By.ID, value=self.txt_email_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(by=By.ID, value=self.txt_firstname_id).clear()
        self.driver.find_element(by=By.ID, value=self.txt_firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(by=By.ID, value=self.txt_lastname_id).clear()
        self.driver.find_element(by=By.ID, value=self.txt_lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(by=By.ID,value=self.btn_search_id).click()

    def getNumofRows(self):
        rows=self.driver.find_elements(by=By.XPATH,value=self.tableRows_xpath)
        print("total rows",len(rows))
        return len(rows)

    def getNumofColumns(self):
        columns=self.driver.find_elements(by=By.XPATH, value=self.tableColumns_xpath)
        return len(columns)

    def searchCustomerbyEmail(self,email):
        flag=False
        for r in range(1,self.getNumofRows()+1):
            table=self.driver.find_element(by=By.XPATH,value=self.table_xpath)
            emailid=table.find_element(by=By.XPATH,value="//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text

            if emailid==email:
                flag =True
                break

        return flag

    def searchCustomerbyName(self, Name):
        flag = False
        for r in range(1, self.getNumofRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            name = table.find_element(by=By.XPATH,
                                         value="//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text

            if name == Name:
                flag = True
                break

        return flag



