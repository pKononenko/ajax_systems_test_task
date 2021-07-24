
def login_user(login_page, email, password):
    login_page.fill_fields(email, password)
    login_page.click_login_button()
