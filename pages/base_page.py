class BasePage:
    def __init__(self, sb):
        self.sb = sb

    def open_url(self, url):
        
        self.sb.uc_open_with_reconnect(url, reconnect_time=5)
