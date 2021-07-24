from tests.page.login_page import LoginPage
from tests.page.hub_page import HubPage

from utils.test_utils import login_user


class TestAjaxApp:

    def test_correct_login(self, pages_list):
        login_page, hub_page = pages_list

        login_user(login_page, 'qa.ajax.app.automation@gmail.com', 'qa_automation_password')

        hub_page.skip_push_notification_message()

        assert hub_page.check_create_hub_button() > 0

    def test_incorrect_login(self, pages_list):
        login_page, hub_page = pages_list

        login_user(login_page, 'ajax.omation@gmail.com', 'qa_automation_password')

        assert hub_page.check_create_hub_button() == 0 and \
            login_page.check_error_message() == 'Невірний логін або пароль'
    
    def test_incorrect_password(self, pages_list):
        login_page, hub_page = pages_list

        login_user(login_page, 'qa.ajax.app.automation@gmail.com', '111')

        assert hub_page.check_create_hub_button() == 0 and \
            login_page.check_error_message() == 'Невірний логін або пароль'

    def test_all_blank_fields(self, pages_list):
        login_page, hub_page = pages_list
        
        login_user(login_page, '', '')

        assert hub_page.check_create_hub_button() == 0 and \
            login_page.check_error_message() == 'Будь ласка, заповніть усі поля'

    def test_whitespaces_fields(self, pages_list):
        login_page, hub_page = pages_list
        
        login_user(login_page, '     ', '    ')

        assert hub_page.check_create_hub_button() == 0 and \
            login_page.check_error_message() == 'Будь ласка, заповніть усі поля'
