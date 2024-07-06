from page_objects.base_page import BasePage
from locators.login_locators import StellarBurgersLoginLocators
from locators.forgot_password_locators import StellarBurgersForgotPasswordLocators
from config import LOGIN


class LoginPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def open_login_page(self):
        self.navigate(LOGIN, StellarBurgersLoginLocators.TITLE_FORM)

    def click_link_forgot_password(self):
        self.action_click(StellarBurgersLoginLocators.LINK_FORGOT_PASSWORD,
                          StellarBurgersForgotPasswordLocators.BUTTON_RESTORE_PASSWORD)
