from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
import math
from pages.locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.url = url


    def open(self):
        self.driver.get(self.url)

    def click_on_elem(self, by, selector):
        self.driver.find_element(by, selector).click()


    def get_text(self, by, selector):
        var = self.driver.find_element(by, selector).text
        return var

    def go_to_login_page(self):
        link = self.driver.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
