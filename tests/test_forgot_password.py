import pytest
import allure
import time

from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.reset_password_page import ResetPasswordPage
from locators.reset_password_locators import StellarBurgersResetPasswordLocators
from config import FORGOT_PASSWORD, RESET_PASSWORD


class TestForgotPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_page_opening_forgot_password(self, web_driver):
        login_page = LoginPage(web_driver)
        login_page.open_login_page()
        login_page.click_link_forgot_password()
        url = web_driver.current_url
        assert url == FORGOT_PASSWORD

    @allure.title('Проверка ввода почты на странице восстановления пароля и клика по кнопке «Восстановить»')
    def test_page_enter_email_and_redirect_reset_password(self, web_driver):
        forgot_password = ForgotPasswordPage(web_driver)
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email()
        forgot_password.click_button_restore_password()
        url = web_driver.current_url
        assert url == RESET_PASSWORD

    @allure.title('Проверка отображения скрытого пароля')
    def test_whether_hidden_password(self, web_driver):
        forgot_password = ForgotPasswordPage(web_driver)
        reset_password = ResetPasswordPage(web_driver)
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email()
        forgot_password.click_button_restore_password()
        reset_password.enter_password()
        assert reset_password.get_attribute_password() == "password"

    @allure.title('Проверка отображения видимого пароля')
    def test_whether_visible_password(self, web_driver):
        forgot_password = ForgotPasswordPage(web_driver)
        reset_password = ResetPasswordPage(web_driver)
        forgot_password.open_forgot_password_page()
        forgot_password.enter_email()
        forgot_password.click_button_restore_password()
        reset_password.enter_password()
        reset_password.click_button_action_password()
        assert reset_password.get_attribute_password() == "text"







