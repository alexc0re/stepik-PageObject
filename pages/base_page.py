class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_link(self):
        self.browser.get(self.url)

