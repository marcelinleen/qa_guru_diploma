from pages.mobile_pages.mobile_login_page import MobileLoginPage


def get_mobile_login(env, login, password):
    login_page = MobileLoginPage()

    login_page.open()
    login_page.fill_login(env, login)
    login_page.fill_password(env, password)
    login_page.submit_form()
    login_page.confirm_connect()
    login_page.close_notification_approve_window()
    login_page.accept_cookie()