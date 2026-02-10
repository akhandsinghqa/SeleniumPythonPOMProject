import pytest
from selenium import webdriver


@pytest.fixture(params=["firefox", "chrome"], scope='class')
def init_driver(request):
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    if request.param == "chrome":
        web_driver = webdriver.Chrome()

    request.cls.driver = web_driver
    yield
    web_driver.close()
