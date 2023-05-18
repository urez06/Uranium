from pages.base import WebPage
from pages.elements import WebElement

class InitPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/account_b2c/page?state=b73d4947-b421-4f23-a83a-b7dfe9f988b2&client_id=account_b2c#/'
        super().__init__(web_driver, url)

    slogan = WebElement(xpath='/html//section[@id="page-left"]//p[@class="what-is__desc"]')
    personal_cabinet = WebElement(xpath='/html//section[@id="page-left"]//h2[@class="what-is__title"]')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    forgot_password = WebElement(xpath='/html//a[@id="forgot_password"]')
    registration = WebElement(xpath='/html//a[@id="kc-register"]')

