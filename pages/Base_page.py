import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        time.sleep(1)

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        time.sleep(1)

    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        time.sleep(1)
        return elements

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        time.sleep(1)
        return element.text
