from tests.page.login_page import LoginPage
from tests.page.hub_page import HubPage

from utils.test_utils import logout_user


def test_correct_login(page_manager):
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    login_page.open_login_page()
    login_page.fill_fields('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    login_page.click_login_button()

    hub_page = pm.create_page(HubPage)

    hub_page.skip_push_notification_message()

    # Store value for assert before logout
    # Because i can't create a good working
    # fixture for automating this
    button_on_page_bool = hub_page.check_create_hub_button() > 0

    # Logout user
    logout_user(pm)

    assert button_on_page_bool

def test_incorrect_login(page_manager):
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    login_page.open_login_page()
    login_page.fill_fields('ajax.omation@gmail.com', 'qa_automation_password')
    login_page.click_login_button()

    hub_page = pm.create_page(HubPage)

    button_on_page_bool = hub_page.check_create_hub_button() == 0 and \
        login_page.check_error_message() == 'Невірний логін або пароль'

    login_page.click_back_button()

    assert button_on_page_bool

def test_incorrect_password(page_manager):
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    login_page.open_login_page()
    login_page.fill_fields('qa.ajax.app.automation@gmail.com', '111')
    login_page.click_login_button()

    hub_page = pm.create_page(HubPage)

    button_on_page_bool = hub_page.check_create_hub_button() == 0 and \
        login_page.check_error_message() == 'Невірний логін або пароль'

    login_page.click_back_button()

    assert button_on_page_bool

def test_all_blank_fields(page_manager):
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    login_page.open_login_page()
    login_page.fill_fields('', '')
    login_page.click_login_button()

    hub_page = pm.create_page(HubPage)

    button_on_page_bool = hub_page.check_create_hub_button() == 0 and \
        login_page.check_error_message() == 'Будь ласка, заповніть усі поля'

    login_page.click_back_button()

    assert button_on_page_bool

def test_whitespaces_fields(page_manager):
    pm = page_manager
    
    login_page = pm.create_page(LoginPage)
    login_page.open_login_page()
    login_page.fill_fields('       ', '     ')
    login_page.click_login_button()

    hub_page = pm.create_page(HubPage)

    button_on_page_bool = hub_page.check_create_hub_button() == 0 and \
        login_page.check_error_message() == 'Будь ласка, заповніть усі поля'

    login_page.click_back_button()

    assert button_on_page_bool
