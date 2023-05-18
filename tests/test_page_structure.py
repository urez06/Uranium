from pages.init_page import InitPage

def test_page_left_side(web_browser):
        page = InitPage(web_browser)
        page.wait_page_loaded()
        assert page.slogan.get_text() == 'Персональный помощник в цифровом мире Ростелекома'
        assert page.personal_cabinet.get_text() == 'Личный кабинет'

def test_page_right_side(web_browser):
        page = InitPage(web_browser)
        page.wait_page_loaded()
        assert page.tab_login.is_presented() and page.tab_login.is_visible() and page.tab_login.is_clickable()
        assert page.tab_mail.is_presented() and page.tab_mail.is_visible() and page.tab_mail.is_clickable()
        assert page.tab_mail.is_presented() and page.tab_mail.is_visible() and page.tab_mail.is_clickable()
        assert page.tab_mail.is_presented() and page.tab_mail.is_visible() and page.tab_mail.is_clickable()

def test_left_side_reg_page(web_browser):
         page = InitPage(web_browser)
         page.registration.click()
         assert page.slogan.get_text() == 'Персональный помощник в цифровом мире Ростелекома'
         assert page.personal_cabinet.get_text() == 'Личный кабинет'

def test_left_side_forgot_page(web_browser):
         page = InitPage(web_browser)
         page.forgot_password.click()
         assert page.slogan.get_text() == 'Персональный помощник в цифровом мире Ростелекома'
         assert page.personal_cabinet.get_text() == 'Личный кабинет'
