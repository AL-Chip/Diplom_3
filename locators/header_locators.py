from selenium.webdriver.common.by import By


class StellarBurgersHeader:
    PERSONAL_AREA_BUTTON = (By.XPATH, "//a[.='Личный Кабинет']")  # Кнопка "личный кабинет" в шапке
    LINK_LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")  # Логотип
