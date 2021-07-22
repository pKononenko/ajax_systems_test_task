import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HubPage(object):

    def __init__(self, driver):

        self.driver = driver

    def skip_push_notification_message(self):
        time.sleep(5)
        push_notification_modal_button = self.driver.find_elements('id', 'com.ajaxsystems:id/cancel_button')
        print(f"\n\n\n\n\n\n{len(push_notification_modal_button)}\n\n\n\n\n")
        if push_notification_modal_button:
            push_notification_modal_button[0].click()

    def check_create_hub_button(self):
        time.sleep(5)
        return len(self.driver.find_elements('id', 'com.ajaxsystems:id/build'))

    def click_settings_button(self):
        self.driver.find_element('id', 'com.ajaxsystems:id/menuDrawer').click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('id', 'com.ajaxsystems:id/settings')))
        self.driver.find_element('id', 'com.ajaxsystems:id/settings').click()

    def click_logout_button(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(('id', 'com.ajaxsystems:id/logout')))
        self.driver.find_element('id', 'com.ajaxsystems:id/logout').click()
