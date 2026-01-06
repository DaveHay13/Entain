from .base_page import BasePage

class RegistrationPage(BasePage):
    EMAIL_FIELD = "input[name='email']"
    PASSWORD_FIELD = "input[name='password']"
    CHECKBOX_TNC = "span[data-role='checkboxBox']"
    SUBMIT_BUTTON = "button[data-role='signupSubmit']"
    
    ERROR_MESSAGE = "div[class*='error'], .input-error, [data-role*='error']"

    def attempt_registration(self, email, password):
        self.sb.wait_for_element_visible(self.EMAIL_FIELD, timeout=15)
        self.sb.type(self.EMAIL_FIELD, email)
        self.sb.type(self.PASSWORD_FIELD, password)
        self.sb.js_click(self.CHECKBOX_TNC)
        self.sb.click(self.SUBMIT_BUTTON)
