from .base_page import BasePage

class HelpPage(BasePage):
    SUPPORT_EMAIL = "a[href='mailto:support@optibet.ee']"
    SUPPORT_PHONE = "a[href='tel:+372 6680309']"

    def verify_help_content(self):
        self.sb.wait_for_element_visible(self.SUPPORT_EMAIL, timeout=15)
        self.sb.assert_element(self.SUPPORT_PHONE)
        self.sb.assert_text_visible("aidata", timeout=5)
