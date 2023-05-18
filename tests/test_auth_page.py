from pages.auth_page import AuthPage
from pages.config import *

def test_auth_phone(web_browser):
        page = AuthPage(web_browser)
        page.password.send_keys(Pass)
        page.tab_phone.wait_to_be_clickable()
        page.auth_login.send_keys(Phone)
        page.btn.click()
        assert page.home_card.is_presented() and page.user_info.is_presented()

def test_auth_mail(web_browser):
         page = AuthPage(web_browser)
         page.tab_mail.click()
         page.password.send_keys(Pass)
         page.auth_login.send_keys(Email)

         page.btn.click()
         page.wait_page_loaded()
         assert page.home_card.is_presented() and page.user_info.is_presented()

def test_auth_phone_incorect(web_browser):
        page = AuthPage(web_browser)
        page.password.send_keys(NotCorrectPass)
        page.tab_phone.wait_to_be_clickable()
        page.auth_login.send_keys(NotCorrectPhone)
        page.btn.click()
        assert page.form_error.is_presented() and \
               ((page.form_error.get_text() == 'Неверный логин или пароль') or \
                (page.form_error.get_text() == 'Неверно введен текст с картинки'))

def test_auth_mail_incorrect(web_browser):
         page = AuthPage(web_browser)
         page.tab_login.click()
         page.password.send_keys(NotCorrectPass)
         page.auth_login.send_keys(NotCorrectEmail)

         page.btn.click()
         page.wait_page_loaded()
         assert page.form_error.is_presented() and \
                ((page.form_error.get_text() == 'Неверный логин или пароль') or \
                 (page.form_error.get_text() == 'Неверно введен текст с картинки'))

def test_forgot_link(web_browser):
         page = AuthPage(web_browser)
         page.forgot_password.click()
         assert   ((page.forgot_caption.get_text() == 'Восстановление пароля') and \
                 (page.forgot_desc.get_text() == 'Введите данные и нажмите «Продолжить»'))
