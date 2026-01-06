import pytest
import allure
from pages.home_page import HomePage
from pages.promotions_page import PromotionsPage

@allure.feature("Scenario 2.2: Promotions Page Filtering")
def test_promotions_filters(sb):
    home = HomePage(sb)
    promo = PromotionsPage(sb)

    with allure.step("1. Navigate to Promotions"):
        home.open()
        home.accept_cookies()
        home.go_to_promotions()

    with allure.step("2. Verify Category Filters and Content"):
        
        promo.verify_filters()
