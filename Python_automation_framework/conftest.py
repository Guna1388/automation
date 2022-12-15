import json
from urllib import request

from selenium import webdriver
import pytest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def read_jsonfile(path):
    with open(path) as input:  # Loading testdata
        Input_Object = json.load(input)
        input.close()
    return Input_Object


@pytest.fixture(scope="class")
def browser_setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.instance.driver = driver
    yield
    driver.close()
    driver.quit()
