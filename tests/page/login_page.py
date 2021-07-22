import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(object):

    def __init__(self, driver):

        self.driver = driver

    def open_login_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(('id', 'com.ajaxsystems:id/login')))
        self.driver.find_element('id', 'com.ajaxsystems:id/login').click()

    def fill_fields(self, email, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(("id", 'com.ajaxsystems:id/login')))
        self.driver.find_element("id", 'com.ajaxsystems:id/login').clear()
        self.driver.find_element("id", 'com.ajaxsystems:id/login').send_keys(email)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(("id", 'com.ajaxsystems:id/password')))
        self.driver.find_element("id", 'com.ajaxsystems:id/password').send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/next')))
        self.driver.find_element("id", 'com.ajaxsystems:id/next').click()

    def click_back_button(self):
        self.driver.find_element("id", 'com.ajaxsystems:id/back').click()

    def check_error_message(self):
        time.sleep(1)
        #WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/snackbar_action')))
        return self.driver.find_element("id", 'com.ajaxsystems:id/snackbar_text').text
