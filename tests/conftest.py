import pytest

from config import URL
from selenium import webdriver


def _get_driver(name):
    if name == "chrome":
        return webdriver.Chrome()
    elif name == "firefox":
        return webdriver.Firefox()
    else:
        raise TypeError("Driver is not found")


@pytest.fixture(params=["chrome"])
def web_driver(request):
    driver = _get_driver(request.param)
    driver.get(URL)
    yield driver
    driver.quit()
