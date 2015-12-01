__author__ = 'biswajit'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    context.launch_url = "http://www.tutorialspoint.com/index.htm"
    dc = DesiredCapabilities.CHROME.copy()
    #context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=dc)
    context.driver = webdriver.Chrome(executable_path='/Users/biswajit/selenium_files/chromedriver')
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.execute_script("document.body.style.transform='scale(1)'")

def after_all(context):
    context.driver.quit()
