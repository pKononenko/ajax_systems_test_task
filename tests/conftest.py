import subprocess
import time

import pytest
from appium import webdriver

from tests.page.page_manager import PagesManager
from utils.android_utils import android_get_desired_cap

from tests.page.login_page import LoginPage
from tests.page.hub_page import HubPage


@pytest.fixture(scope='session')
def setup_appium():

    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(setup_appium):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_cap())

    yield driver


@pytest.fixture(scope='session')
def page_manager(driver):
    return PagesManager(driver)


@pytest.fixture()
def pages_list(page_manager):
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    hub_page = pm.create_page(HubPage)

    return login_page, hub_page


@pytest.yield_fixture(scope="session", autouse=True)
def automate_logout(page_manager):
    # preconds
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    hub_page = pm.create_page(HubPage)

    login_page.open_login_page()
    

    #yield {"login_page": login_page, "hub_page": hub_page}
    yield pages_list


    # postconds
    if hub_page.check_create_hub_button():
        hub_page.click_settings_button()
        hub_page.click_logout_button()
    else:
        login_page.click_back_button()
