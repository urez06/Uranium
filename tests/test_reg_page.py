from pages.reg_page import RegPage
from pages.config import *
from pages.elements import WebElement

def test_reg_data(web_browser):
    page = RegPage(web_browser)
    page.registration.click()
    page.first_name.send_keys(NotCorrectRegName1)
    page.last_name.send_keys(NotCorrectRegLast1)
    assert page.input_name_error1.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    page.email_or_phone_name.send_keys(NotCorrectRegEmail1)
    assert page.input_name_error2.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    page.password.send_keys(NotCorrectRegPass1)
    assert page.input_mail_error.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    page.password_confirm.send_keys(NotCorrectRegPass1)
    assert page.input_password_error1.get_text() == 'Длина пароля должна быть не менее 8 символов'
    page.password.click()
    assert page.input_password_error2.get_text() == 'Длина пароля должна быть не менее 8 символов'

def test_reg_data2(web_browser):
    page = RegPage(web_browser)
    page.registration.click()
    page.first_name.send_keys(NotCorrectRegName2)
    page.last_name.send_keys(NotCorrectRegLast2)
    assert page.input_name_error1.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    page.email_or_phone_name.send_keys(NotCorrectRegEmail2)
    assert page.input_name_error2.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    page.password.send_keys(NotCorrectRegPass2)
    assert page.input_mail_error.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    page.password_confirm.send_keys(NotCorrectRegPass2)
    assert page.input_password_error1.get_text() == 'Пароль должен содержать только латинские буквы'
    page.password.click()
    assert page.input_password_error2.get_text() == 'Пароль должен содержать только латинские буквы'
