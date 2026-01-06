from .base_page import BasePage

class LoginPage(BasePage):
    
    USER_FIELD = "input[name='email']"
    PASS_FIELD = "input[name='password']"
    SUBMIT_LOGIN = "button[type='submit']"
    
    LOGIN_ERROR = "div[class*='Notification_message'], [class*='error']"

    def login(self, username, password):
        self.sb.wait_for_element_visible(self.USER_FIELD, timeout=10)
        self.sb.type(self.USER_FIELD, username)
        self.sb.type(self.PASS_FIELD, password)
        self.sb.click(self.SUBMIT_LOGIN)

    def verify_error_visible(self):
        self.sb.assert_element_visible(self.LOGIN_ERROR, timeout=10)
