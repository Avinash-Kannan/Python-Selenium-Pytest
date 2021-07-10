import time
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import datetime
import hashlib
import keyring
from test_Scripts.test_config import driver_setup, take_screenshot, get_logger
from test_pageObjects.loginPage import Login
from test_pageObjects.boardPage import BoardPage
from test_pageObjects.landingPage import LandingPage
from test_pageObjects.cardPage import CardPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import configparser
from selenium.webdriver.chrome.options import Options
configs = configparser.RawConfigParser
# configs.read("Configuration/config.ini")


class TestTrello:

    driver = driver_setup()
    logger = get_logger()

    def test_launch_browser(self):
        try:
            options = webdriver.ChromeOptions
            # self.driver = webdriver.chrome(ChromeDriverManager.install())
            # TestTrello.driver.get(configs.get('common-info', 'url_trello'))
            TestTrello.driver.get("https://trello.com/login")
            TestTrello.driver.implicitly_wait(10)
            TestTrello.driver.maximize_window()
            self.app_title = TestTrello.driver.title
            print(self.app_title)

            if self.app_title == "Log in to Trello":
                assert True
                TestTrello.logger.info(" Navigated to Trello Login page successfully")
            else:
                take_screenshot(TestTrello.driver,inspect.currentframe().f_code.co_name)                
                assert False
        except Exception as e:
            print("Exception occurred - "+str(e))

    def test_login_trello(self):
        try:
            options = webdriver.ChromeOptions
            self.ObjLP = Login(TestTrello.driver)
            time.sleep(3)
            self.ObjLP.set_username("avinashk.mech@gmail.com")
            time.sleep(5)
            self.ObjLP.click_login_button()
            time.sleep(5)
            self.ObjLP.set_password(keyring.get_password("testTrello", "Avinash"))
            self.ObjLP.click_login_submit()
        except Exception as e:
            take_screenshot(TestTrello.driver,inspect.currentframe().f_code.co_name)
            print("Exception occurred - "+str(e))

    def test_landing_trello(self):
        try:
            options = webdriver.ChromeOptions
            self.ObjLanding = LandingPage(TestTrello.driver)
            time.sleep(10)

            self.ObjLanding.click_createboard_icon()
            time.sleep(2)
            self.ObjLanding.click_createboard_option()
            time.sleep(2)
            self.ObjLanding.set_boardtitle_input("Trello Project")
            time.sleep(5)
            self.ObjLanding.click_createboard_button()
            # self.ObjLanding.click_available_board()
        except Exception as e:
            take_screenshot(TestTrello.driver,inspect.currentframe().f_code.co_name)
            print("Exception occurred - "+str(e))

    def test_board_trello(self):
        try:
            time.sleep(5)
            self.ObjBP = BoardPage(TestTrello.driver)
            # self.ObjBP.click_addList_icon()

            self.list_names = ["Not Started", "In Progress", "QA", "Done"]
            for self.title in self.list_names:
                time.sleep(3)
                self.ObjBP.set_listTitle_input(self.title)
                self.ObjBP.click_addList_button()
                time.sleep(3)
            # self.ele = WebDriverWait(TestTrello.driver, 10).until(EC.presence_of_element_located(By.XPATH
            # ("//input[@placeholder='Enter list title…']")))
            # self.ele.send_keys("Not Started")

            self.ObjBP.click_addList_button()
            self.ObjBP.click_addCard_icon()
            for self.i in range(1, 5):
                time.sleep(2)
                self.ObjBP.set_cardTitle_input("card "+str(self.i))
                self.ObjBP.click_addCard_button()
                time.sleep(3)

            self.actions = ActionChains(TestTrello.driver)
            try:
                self.actions.drag_and_drop(self.ObjBP.dragndrop_card2_source(), self.ObjBP.dragndrop_inProgress_target()).perform()
                time.sleep(5)

            except Exception as e:
                print("Exception occurred 1 - "+str(e))
            try:
                time.sleep(5)
                ActionChains(TestTrello.driver).click_and_hold(self.ObjBP.dragndrop_card3_source()).move_to_element(self.ObjBP.dragndrop_qa_target()).release(self.ObjBP.dragndrop_qa_target()).perform()
                # self.actions.drag_and_drop(self.ObjBP.dragndrop_card3_source(),
                # self.ObjBP.dragndrop_qa_target()).perform()
                TestTrello.driver.implicitly_wait(5)
            except Exception as e:
                print("Exception occurred 2 - "+str(e))

            try:
                time.sleep(5)
                ActionChains(TestTrello.driver).click_and_hold(self.ObjBP.dragndrop_card2_source()).move_to_element(
                    self.ObjBP.dragndrop_qa_target()).release(self.ObjBP.dragndrop_qa_target()).perform()
                TestTrello.driver.implicitly_wait(5)
            except Exception as e:
                print("Exception occurred 3 - "+str(e))
        except Exception as e:
            take_screenshot(TestTrello.driver,inspect.currentframe().f_code.co_name)
            print("Exception occurred - "+str(e))

    def test_card_trello(self):
        try:
            time.sleep(3)
            self.ObjCP = CardPage(TestTrello.driver)
            time.sleep(5)
            self.ObjCP.click_card()
            time.sleep(2)
            self.ObjCP.click_addMember()
            time.sleep(3)
            self.ObjCP.select_member()
            time.sleep(2)
            self.ObjCP.close_addMember()
            self.ObjCP.set_comments_input("I'm Done")
            time.sleep(2)
            self.ObjCP.click_saveCard_button()
            self.ObjCP.click_closecrad_button()
        except Exception as e:
            take_screenshot(TestTrello.driver,inspect.currentframe().f_code.co_name)
            print("Exception occurred - "+str(e))







