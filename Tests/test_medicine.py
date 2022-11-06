import datetime
import time

from POM.medicine import MedicineOffer
from Library.config import Configuration


class TestMedicine:
    def test_medicine_mod(self, init_driver):
        global driver
        try:
            driver = init_driver
            offer = MedicineOffer(driver)
            offer.TC_Offers_002()

            # offer.TC_Offers_003()

            offer.TC_Offers_004()

            # offer.TC_Offers_005()

            # offer.TC_Offers_006()

            offer.TC_Offers_007()

            offer.TC_Offers_008()

            offer.TC_Offers_009()

        except BaseException:
            td = datetime.datetime.now()
            name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOTS_PATH + name)
            # raise err_msg