from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)
        password_repeat_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_FIELD)
        password_repeat_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "It isn't login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form doesn't present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form doesn't present"
