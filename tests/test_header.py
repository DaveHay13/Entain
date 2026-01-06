import allure
from pages.home_page import HomePage

@allure.feature("Scenario 2.1: Header and Languages")
def test_header_workflow_linear(sb):
    home = HomePage(sb)
    home.open()
    home.accept_cookies()
    home.verify_logo_present()
    home.switch_language("en", "/en")
    home.switch_language("ru", "/ru")
    home.switch_language("et", "optibet.ee")