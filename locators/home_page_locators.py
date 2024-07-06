from selenium.webdriver.common.by import By


class StellarBurgersHomePageLocators:
    LOGIN_BUTTON = (By.XPATH, "//section[2]/div/button[text()= 'Войти в аккаунт']") # Кнопка авторизации на главной странице
    CHECKOUT_BUTTON = (By.XPATH, "//section[2]/div/button[text()= 'Оформить заказ']") # Оформить заказ
    DIV_BUNS = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # Тап раздела булки
