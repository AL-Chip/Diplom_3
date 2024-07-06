from page_objects.base_page import BasePage
from locators.home_page_locators import StellarBurgersHomePageLocators
from config import DOMEN


class HomePage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def open_home_page(self):
        self.navigate(DOMEN, StellarBurgersHomePageLocators.DIV_BUNS)
