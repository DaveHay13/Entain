from pages.home_page import HomePage
from pages.help_page import HelpPage

def test_navigate_to_help_center(sb):
    home = HomePage(sb)
    help_pg = HelpPage(sb)
    
    home.open()
    home.accept_cookies()
    home.click_help()
    help_pg.verify_help_content()
