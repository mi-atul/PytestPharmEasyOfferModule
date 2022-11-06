import re
import time

import pytest

from Library.excel_lib import ReadExcle
from Library.config import Configuration


class HealthcareOffer:

    obj_1 = ReadExcle()
    locator_reg = obj_1.read_locator(Configuration.OFFERS_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def TC_Offers_002(self):
        locator = self.locator_reg["offer_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def TC_Offers_004(self):
        locator = self.locator_reg["healthcare_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def TC_Offers_005(self):
        locator = self.locator_reg["coupon_copy_code"]
        self.driver.find_element(*locator).click()
        # self.driver.back()
        time.sleep(5)

    def TC_Offers_007(self):
        try:
            locator = self.locator_reg["coupons"]
            self.driver.find_element(*locator).click()
            time.sleep(5)
        except:
            self.driver.back()
            locator = self.locator_reg["coupons"]
            self.driver.find_element(*locator).click()
            time.sleep(5)
            assert False, "Copy Code button not working properly"

    def TC_Offers_008(self):
        locator = self.locator_reg["copy_code_btn"]
        self.driver.find_element(*locator).click()
        # self.driver.back()
        time.sleep(5)

    def TC_Offers_009(self):
        try:
            locator = self.locator_reg["copy_code_and_proceed_btn"]
            self.driver.find_element(*locator).click()
            time.sleep(5)
        except:
            self.driver.back()
            locator = self.locator_reg["copy_code_and_proceed_btn"]
            self.driver.find_element(*locator).click()
            time.sleep(5)
            assert False, "Coupon's Copy Code button not working properly"
