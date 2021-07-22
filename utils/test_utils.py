from tests.page.hub_page import HubPage


def logout_user(pm):
    hub_page = pm.create_page(HubPage)
    hub_page.click_settings_button()
    hub_page.click_logout_button()
