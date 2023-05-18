from pages.base import WebPage
from pages.elements import WebElement

class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/account_b2c/page?state=b73d4947-b421-4f23-a83a-b7dfe9f988b2&client_id=account_b2c#/'
        super().__init__(web_driver, url)

    registration = WebElement(xpath='/html//a[@id="kc-register"]')
    first_name = WebElement(css_selector='input[name="firstName"]')
    last_name = WebElement(css_selector='input[name="lastName"]')
    email_or_phone_name = WebElement(id='address')
    password = WebElement(id='password')
    password_confirm = WebElement(id='password-confirm')
    input_mail_error = WebElement(css_selector='.email-or-phone .rt-input-container__meta--error')
    input_password_error1 = WebElement(css_selector='.new-password-container__password .rt-input-container__meta--error')
    input_password_error2 = WebElement(css_selector='.new-password-container__confirmed-password .rt-input-container__meta--error')
    input_name_error1 = WebElement(css_selector='.name-container .rt-input-container--error:nth-of-type(1) .rt-input-container__meta--error')
    input_name_error2 = WebElement(css_selector='.name-container .rt-input-container--error:nth-of-type(2) .rt-input-container__meta--error')