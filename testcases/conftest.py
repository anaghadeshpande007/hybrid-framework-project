import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pytest_html import hooks
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        service = Service(executable_path="C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        print('launch chrome browser')
    elif browser=='firefox':
        service=Service(executable_path="C:\\Drivers\\firefoxdriver-win64\\geckodriver.exe")
        driver=webdriver.Firefox(service=service)
        print('launch firefox browser')
    else:
        service=Service(executable_path="C:\\Drivers\\internet explorer\\IEDriverServer.exe")
        driver=webdriver.Ie(service=service)
    return driver

def pytest_addoption(parser):    # this will get value from command line prompt
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #this will return browser value to setup method
    return request.config.getoption("--browser")

############# pytest html report##################################################
# it is a hook to add environment info to HTML Report

def pytest_configure(config):
    metadata=config.pluginmanager.getplugin("metadata")
    if metadata:
        config.stash[metadata_key]['Project Name']='nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Anagha'

#It is a hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)