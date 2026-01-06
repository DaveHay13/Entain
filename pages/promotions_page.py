from .base_page import BasePage

class PromotionsPage(BasePage):
    
    CASINO_TAB = "//button[contains(@class, 'tags__item-button')]//span[text()='Kasiino']"
    SPORTS_TAB = "//button[contains(@class, 'tags__item-button')]//span[text()='Spordiennustus']"
    
    
    OFFER_CARDS = "div[class*='page-content'] a[href*='/promotions/'], div[class*='promotion']"

    def verify_filters(self):
      
        self.sb.wait_for_element_visible(self.CASINO_TAB, timeout=15)
        self.sb.js_click(self.CASINO_TAB)
        print("Clicked Casino - URL moved to /promotions/kasiino")
        
        
        self.sb.sleep(6) 
        self.sb.assert_element(self.OFFER_CARDS, timeout=20)
        
        
        self.sb.wait_for_element_visible(self.SPORTS_TAB, timeout=15)
        self.sb.js_click(self.SPORTS_TAB)
        print("Clicked Sports - URL moving to /promotions/spordiennustus")
        
        self.sb.sleep(6)
        self.sb.assert_element(self.OFFER_CARDS, timeout=20)
