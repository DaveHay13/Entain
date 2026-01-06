import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_negative(sb):
    home = HomePage(sb)
    login_pg = LoginPage(sb)
    
    home.open()
    home.accept_cookies()
    home.click_login()
    
    
    login_pg.login("nonexistent@user.com", "WrongPassword123!")
    
    
    login_pg.verify_error_visible()
