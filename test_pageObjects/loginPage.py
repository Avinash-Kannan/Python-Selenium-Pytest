

from selenium.webdriver.common.by import By
from selenium import webdriver
from test_pageObjects.locators import Locator
from test_Scripts.test_config import decode_password,explicit_wait


class Login:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self,username):
        explicit_wait(self.driver,Locator.txt_username)
        self.driver.find_element_by_xpath(Locator.txt_username).send_keys(username)

    def set_password(self,pwd):
        # explicit_wait(Locator.txt_password)
        self.driver.find_element_by_xpath(Locator.txt_password).send_keys(pwd)

    def click_login_button(self):
        # explicit_wait(Locator.btn_submit)
        self.driver.find_element_by_xpath(Locator.btn_login).click()

    def click_login_submit(self):
        # explicit_wait(Locator.btn_submit)
        self.driver.find_element_by_xpath(Locator.btn_submit).click()
