from .base_page import BasePage

class HomePage(BasePage):
    COOKIE_ALLOW = "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
    LOGO = "a[class*='logo']"
    JOIN_BUTTON = "button[data-role='signupHeaderButton']"
    LOGIN_BUTTON = "button[data-role='loginHeaderButton']"
    PROMOTIONS_LINK = "a[href*='/promotions']"
    HELP_BUTTON = "a[data-role='topHelp']"
    LANG_SWITCHER = "a[class*='language-menu__label']"

    def open(self):
        self.sb.uc_open_with_reconnect("https://www.optibet.ee/et/", reconnect_time=10)
        # Force a large resolution to ensure header elements aren't hidden
        self.sb.set_window_size(1920, 1080)
        
    def accept_cookies(self):
        if self.sb.is_element_visible(self.COOKIE_ALLOW):
            self.sb.js_click(self.COOKIE_ALLOW)
            self.sb.sleep(2)

    def verify_logo_present(self):
        self.sb.wait_for_element_visible(self.LOGO, timeout=15)
        self.sb.assert_element(self.LOGO)

    def switch_language(self, lang_code, expected_url_part):
        self.sb.wait_for_element_visible(self.LANG_SWITCHER, timeout=15)
        self.sb.click(self.LANG_SWITCHER)
        lang_option = f"a[data-id='langMenuItem-{lang_code.lower()}']"
        self.sb.wait_for_element_visible(lang_option, timeout=10)
        self.sb.click(lang_option)
        self.sb.assert_url_contains(expected_url_part)

    def click_join(self):
        self.sb.wait_for_element_visible(self.JOIN_BUTTON, timeout=15)
        self.sb.click(self.JOIN_BUTTON)

    def click_login(self):
        self.sb.wait_for_element_visible(self.LOGIN_BUTTON, timeout=15)
        self.sb.click(self.LOGIN_BUTTON)

    def go_to_promotions(self):
        self.sb.wait_for_element_visible(self.PROMOTIONS_LINK, timeout=15)
        self.sb.click(self.PROMOTIONS_LINK)

    def click_help(self):
        self.sb.wait_for_element_visible(self.HELP_BUTTON, timeout=15)
        self.sb.click(self.HELP_BUTTON)