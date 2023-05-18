from pages.base import WebPage
from pages.elements import WebElement

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/account_b2c/page?state=b73d4947-b421-4f23-a83a-b7dfe9f988b2&client_id=account_b2c#/'
        super().__init__(web_driver, url)


    password = WebElement(id='password')
    auth_login = WebElement(id="username")
    btn = WebElement(id='kc-login')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    home_card = WebElement(xpath='/html//div[@id="app"]//div[@class="base-card home__info-card"]')
    user_info = WebElement(xpath='/html//div[@id="app"]//div[@class="home"]//div[@class="user-info__name-container"]')
    form_error = WebElement(xpath='/html//span[@id="form-error-message"]')
    forgot_password = WebElement(xpath='/html//a[@id="forgot_password"]')
    forgot_caption = WebElement(xpath='/html//section[@id="page-right"]//h1[@class="card-container__title"]')
    forgot_desc = WebElement(xpath='/html//section[@id="page-right"]//p[@class="card-container__desc"]')