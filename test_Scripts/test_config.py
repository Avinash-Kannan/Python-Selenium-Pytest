from selenium import webdriver
import pytest
import datetime
import logging
import logging.handlers
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


dateTime = str(datetime.datetime.now()).strip().split('.')[0]
exp_datetime = dateTime.replace('-', '').replace(':', '')


def driver_setup():
        driver = webdriver.Chrome(
            "C:\\Users\\deepa\\OneDrive\\Documents\\Selenium\\drivers\\chromeDriver\\chromedriver.exe")
        return driver


def take_screenshot(driver,func_name):
        driver.save_screenshot(
            ".\\Screenshots\\" + "screenshot_" + func_name + exp_datetime + "_error.png")


def get_logger():
        logging.basicConfig(filename="Logs/logger_"+exp_datetime+".log", format='%(asctime)s - :%(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler("Logs/logfile_"+exp_datetime+".log",
                                                          maxBytes=1024 * 1024 * 28, backupCount=3)
        logger = logging.getLogger()
        # file_handler = logging.FileHandler("Logs/logfile_"+exp_datetime+".log")
        logger.addHandler(rotate_file)
        # formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # file_handler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger


def explicit_wait(driver,element):
        try:
         WebDriverWait(driver, 10).until(ec.element_to_be_selected(element))
        except Exception as e:
            print("Exception occurred in exp_wait - " + str(e))



def decode_password(password):
    return base64.b64decode(password)





