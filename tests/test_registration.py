import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

@pytest.mark.parametrize("email, password", [
    ("test_without_at.com", "SafePass123!"), 
    ("valid@email.com", "123")
])
def test_registration_validation(sb, email, password):
    home = HomePage(sb)
    reg = RegistrationPage(sb)
    
    home.open()
    home.accept_cookies()
    home.click_join()
    
    reg.attempt_registration(email, password)
    
    
    sb.assert_element_visible(reg.ERROR_MESSAGE, timeout=5)
